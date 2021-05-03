# SELECT result,
#        IF(matches2020.result = 1, redteam, blueteam) as Team,
#        IF(matches2020.result = 1, redtop, bluetop) as Top,
#        IF(matches2020.result = 1, redjungle, bluejungle) as Jungle,
#        IF(matches2020.result = 1, redmid, bluemid) as Mid,
#        IF(matches2020.result = 1, redadc, blueadc) as ADC,
#        IF(matches2020.result = 1, redsupport, bluesupport) as Support
# FROM matches2020
# WHERE gameid = '5655-7249';

SELECT result,
       IF(matches2020.result = 1, redteam, blueteam) as Team,
       IF(matches2020.result = 1, redtop, bluetop) as Top,
       IF(matches2020.result = 1, redjungle, bluejungle) as Jungle,
       IF(matches2020.result = 1, redmid, bluemid) as Mid,
       IF(matches2020.result = 1, redadc, blueadc) as ADC,
       IF(matches2020.result = 1, redsupport, bluesupport) as Support
FROM matches2020
WHERE gameid = {1};
