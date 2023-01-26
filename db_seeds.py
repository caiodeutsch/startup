from utils import create_conn

secret_name_db = 'databases/prod/startup' # String definition of AWS Secrets for Database

engine = create_conn(secret_name_db) # Create database connection

sql = """
CREATE SCHEMA `startup` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
"""
with engine.begin() as conn:
    conn.execute(sql)

sql = """
CREATE TABLE `startup`.`blacklist` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(50) NULL,
  `reason_id` TINYINT(2) NULL,
  `game_id` TINYINT(2) NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));
"""
with engine.begin() as conn:
    conn.execute(sql)


sql = """
CREATE TABLE `startup`.`reasons` (
  `id` INT NOT NULL,
  `desc` VARCHAR(15) NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));
"""
with engine.begin() as conn:
    conn.execute(sql)

sql = """
INSERT INTO `startup`.`reasons` (`id`, `desc`) 
VALUES 
    ('1', 'foul_language'),
    ('2', 'cheating'),
    ('3', 'harassment'),
    ('4', 'other');
"""
with engine.begin() as conn:
    conn.execute(sql)
