SELECT result,
       IF(matches2020.result = 0, redteam, blueteam) as Team,
       IF(matches2020.result = 0, redtop, bluetop) as Top,
       IF(matches2020.result = 0, redjungle, bluejungle) as Jungle,
       IF(matches2020.result = 0, redmid, bluemid) as Mid,
       IF(matches2020.result = 0, redadc, blueadc) as ADC,
       IF(matches2020.result = 0, redsupport, bluesupport) as Support
FROM matches2020
WHERE gameid = '{1}'; #done

# This query takes 1 game-id and returns the team that won
# SELECT result,
#        IF(matches2020.result = 0, redteam, blueteam) as Team,
#        IF(matches2020.result = 0, redtop, bluetop) as Top,
#        IF(matches2020.result = 0, redjungle, bluejungle) as Jungle,
#        IF(matches2020.result = 0, redmid, bluemid) as Mid,
#        IF(matches2020.result = 0, redadc, blueadc) as ADC,
#        IF(matches2020.result = 0, redsupport, bluesupport) as Support
# FROM matches2020
# WHERE gameid = '5655-7249';