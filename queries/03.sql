SELECT sum(
    (case
        when (result = 0 AND redteam = '{1}') then 1
        when (result = 1 AND blueTeam = '{1}') then 1
        else 0
        end
        ))
FROM matches2020; #done
# this query takes a team name and returns the number of wins they acquired
# SELECT sum(
#     (case
#         when (result = 0 AND redteam = 'FunPlus Phoenix') then 1
#         when (result = 1 AND blueTeam = 'FunPlus Phoenix') then 1
#         else 0
#         end
#         ))
# FROM matches2020;