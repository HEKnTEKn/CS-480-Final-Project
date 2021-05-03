SELECT count(case
           when (result = 0 and redteam = '{1}') then 1
           when (result = 1 and blueteam = '{1}') then 1
           else 0
           end
           ) into @G2Wins
FROM matches2020
WHERE redteam = '{1}' AND blueteam = '{2}';
SELECT count(case
           when (result = 0 and redteam = '{2}') then 1
           when (result = 1 and blueteam = '{2}') then 1
           else 0
           end
           ) into @{2}Wins
FROM matches2020
WHERE redteam = '{2}' AND blueteam = '{1}';
SELECT gameid, result, @G2Wins as 'Total {1} wins', @{2}Wins as 'Total {2} wins', redtop, redjungle, redmid, redadc, redsupport, bluetop, bluejungle, bluemid, blueadc, bluesupport
FROM matches2020
WHERE redteam = '{1}' AND blueteam = '{2}'
UNION ALL
SELECT gameid, result, @G2Wins as 'Total {1} wins', @{2}Wins as 'Total {2} wins', redtop, redjungle, redmid, redadc, redsupport, bluetop, bluejungle, bluemid, blueadc, bluesupport
FROM matches2020
WHERE redteam = '{2}' AND blueteam = '{1}'
GROUP BY gameid;




# SELECT count(case
#            when (result = 0 and redteam = 'G2 Esports') then 1
#            when (result = 1 and blueteam = 'G2 Esports') then 1
#            else 0
#            end
#            ) into @G2Wins
# FROM matches2020
# WHERE redteam = 'G2 Esports' AND blueteam = 'Fnatic';
# SELECT count(case
#            when (result = 0 and redteam = 'Fnatic') then 1
#            when (result = 1 and blueteam = 'Fnatic') then 1
#            else 0
#            end
#            ) into @FnaticWins
# FROM matches2020
# WHERE redteam = 'Fnatic' AND blueteam = 'G2 Esports';
# SELECT gameid, result, @G2Wins as 'Total G2 Esports wins', @FnaticWins as 'Total Fnatic wins', redtop, redjungle, redmid, redadc, redsupport, bluetop, bluejungle, bluemid, blueadc, bluesupport
# FROM matches2020
# WHERE redteam = 'G2 Esports' AND blueteam = 'Fnatic'
# UNION ALL
# SELECT gameid, result, @G2Wins as 'Total G2 Esports wins', @FnaticWins as 'Total Fnatic wins', redtop, redjungle, redmid, redadc, redsupport, bluetop, bluejungle, bluemid, blueadc, bluesupport
# FROM matches2020
# WHERE redteam = 'Fnatic' AND blueteam = 'G2 Esports'
# GROUP BY gameid;

