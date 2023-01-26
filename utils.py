from sqlalchemy import create_engine
from boto3 import session
from json import loads

def create_conn(secret_name):
    '''Return database engine connector token store in AWS secrets manager'''
    client = session.Session().client(service_name='secretsmanager', region_name='us-east-1')
    get_secret_value_response = loads(client.get_secret_value(SecretId=secret_name)['SecretString'])
    user = get_secret_value_response['username']
    password = get_secret_value_response['password']
    server = get_secret_value_response['host']
    server = 'database-1.c2dvu2fkb6if.us-east-1.rds.amazonaws.com'
    #database = 'startup'
    #engine = create_engine(f'mysql+pymysql://{user}:{password}@{server}/{database}?charset=utf8', encoding='utf-8')
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{server}?charset=utf8', encoding='utf-8')
    return engine

def get_token(secret_name):
    '''Return Bearer token store in AWS secrets manager'''
    client = session.Session().client(service_name='secretsmanager', region_name='us-east-1')
    get_secret_value_response = loads(client.get_secret_value(SecretId=secret_name)['SecretString'])
    token = get_secret_value_response['Bearer']
    return token
