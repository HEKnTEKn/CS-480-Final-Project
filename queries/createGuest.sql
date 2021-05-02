CREATE USER 'guest'@'localhost' IDENTIFIED BY '';

GRANT Select ON championstats TO 'guest'@'localhost';
GRANT Select ON matches2020 TO 'guest'@'localhost';
