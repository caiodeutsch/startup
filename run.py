from flask import Flask, request, Response
from utils import create_conn, get_token

def check_possible_reason(reason):
    '''Check if a possible reason is a valid'''
    possible_reasons = ["foul_language", "cheating", "harassment", "other"]
    return True if reason in possible_reasons else False

def check_possible_game_ids(game_id):
    '''Check if game id is in possible range'''
    return True if (game_id <= 10 and game_id >0) else False

def from_to_reason(reason):
    '''Return an id for each reason'''
    from_to_reasons_dict = {
        "foul_language" : 1,
        "cheating" : 2,
        "harassment" : 3,
        "other" : 4
    }    
    return from_to_reasons_dict[reason]

def insert_blacklist_player(json_input):
    '''Insert the player in blacklist table of the database'''
    email = json_input['email']
    reason_id = str(from_to_reason(json_input['reason']))
    game_id = str(json_input['game_id'])

    sql = f"""
        INSERT INTO `startup`.`blacklist` (`email`, `reason_id`, `game_id`) VALUES ('{email}', '{reason_id}', '{game_id}');
    """
    with engine.begin() as conn:
        conn.execute(sql)

def get_player_info(json_input):
    '''Return the information from database to fetch in the API'''
    email = json_input['email']

    sql = f"""
        SELECT tt1.desc, tt1.count, tt2.count_games
        FROM (
            SELECT 1 AS tag, t2.desc, COUNT(*) AS count
            FROM startup.blacklist AS t1
            LEFT JOIN startup.reasons AS t2
            ON t1.reason_id = t2.id
            WHERE t1.email = '{email}' AND t1.created_at >= (NOW() - INTERVAL 90 DAY)
            GROUP BY t2.desc
            ORDER BY count DESC
            LIMIT 1
        ) AS tt1
        LEFT JOIN (SELECT 1 AS tag, COUNT(DISTINCT(game_id)) AS count_games FROM startup.blacklist WHERE email = '{email}') AS tt2
        ON tt1.tag = tt2.tag;
    """

    with engine.begin() as conn:
        rs = conn.execute(sql)
        result_db = rs.fetchall()

    return result_db[0][0], result_db[0][1], result_db[0][2]

secret_name_db    = 'databases/prod/startup'    # String definition of AWS Secrets for Database
secret_name_token = 'bearer/prod/startup'       # String definition of AWS Secrets for Bearer

engine = create_conn(secret_name_db)  # Instance of Database engine
token  = get_token(secret_name_token) # Instance of Bearer token

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/blacklist", methods = ['POST'])
def blacklist():
    """
    Insert a new player to the blacklist

    Parameters
    ----------
        email : str
            The email of the reported player
        reason : str
            The reason for the report. Possible reasons: "foul_language", "cheating", "harassment", "other"
        game_id : integer
            The id of the game where the incident happened. Possible ids: 1 to 10             
    Returns
    -------
        None
    """

    token_user = request.headers.get('Authorization').split()[1] # Token passed from User

    if token != token_user: return Response('Bad token', 401) # Validation if token from User is the same as secrets

    if request.method == 'POST':
        try:
            json_request = request.get_json()

            email = json_request['email']
            reason = json_request['reason']
            game_id = json_request['game_id']

            if not check_possible_reason(reason): return Response('Reason not in list', 400) # Validation if reason passed by user is valid
            if not check_possible_game_ids(game_id): return Response('Game id not in list', 400) # Validation if game id passed by user is valid

            json_input = {
                "email": email,
                "reason": reason,
                "game_id": game_id,
            }
            insert_blacklist_player(json_input)

            return Response('Data inserted!', 200)

        except:
            return Response('Request error', 400)
    else:
        return Response('Request error', 400) 

@app.route("/blacklist/check", methods = ['POST'])
def blacklist_check():
    """
    Return the information about a specific player on the blacklist.

    Parameters
    ----------
        email : str
            Email of the player you want to check
    
    Returns
    -------
        json_response : json 
            A json with the following information:
                Most commonly Reported Ban --> The most commonly reported ban reason for this player
                Times reported             --> Number of times reported in the past 90 days
                Games Reported             --> Number of games where the player has ever been reported
    """

    token_user = request.headers.get('Authorization').split()[1]  # Token passed from User

    if token != token_user: return Response('Bad token', 401) # Validation if token from User is the same as secrets

    if request.method == 'POST':
        try:
            json_request = request.get_json()

            json_input = {
                "email": json_request['email'],
            }
            result_db = get_player_info(json_input) # Return of information to be fetched to API response
            json_response = {
                "Most commonly Reported Ban" : result_db[0],
                "Times reported" : str(result_db[1]),
                "Games Reported" : str(result_db[2])
            }
            return json_response
        except:
            return Response('Request error', 400) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
