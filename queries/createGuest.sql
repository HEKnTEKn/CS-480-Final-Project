DROP USER IF EXISTS 'guest'@'localhost';
CREATE USER 'guest'@'localhost' IDENTIFIED BY '';
GRANT Select ON championstats TO 'guest'@'localhost';
GRANT Select ON matches2020 TO 'guest'@'localhost'; #donw
# this query creates the guest role with select permission to give a custom query
