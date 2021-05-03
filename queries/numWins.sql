# SELECT sum(
#     (case
#         when (result = 1 AND redteam = 'FunPlus Phoenix') then 1
#         when (result = 0 AND blueTeam = 'FunPlus Phoenix') then 1
#         else 0
#         end
#         ))
# FROM matches2020;


SELECT sum(
    (case
        when (result = 1 AND redteam = {1}) then 1
        when (result = 0 AND blueTeam = {1}) then 1
        else 0
        end
        ))
FROM matches2020;