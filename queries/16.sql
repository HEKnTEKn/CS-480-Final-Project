SELECT red{2} as champion, attack, defense, magic, difficulty, tags, hp, hpperlevel,
       mp, mpperlevel, movespeed, armor, armorperlevel, spellblock, spellblockperlevel, attackrange,
       hpregen, hpregenperlevel, mpregen, mpregenperlevel, crit, critperlevel, attackdamage, attackdamageperlevel,
       attackspeedperlevel, attackspeed
FROM matches2020
JOIN championstats c on matches2020.red{2} = c.id
WHERE redteam = '{1}'
UNION
SELECT blue{2} as champion, attack, defense, magic, difficulty, tags, hp, hpperlevel,
       mp, mpperlevel, movespeed, armor, armorperlevel, spellblock, spellblockperlevel, attackrange,
       hpregen, hpregenperlevel, mpregen, mpregenperlevel, crit, critperlevel, attackdamage, attackdamageperlevel,
       attackspeedperlevel, attackspeed
FROM matches2020
JOIN championstats c on matches2020.blue{2} = c.id
WHERE blueteam = '{1}'
ORDER BY champion, difficulty desc; #done

# SELECT redtop as champion, attack, defense, magic, difficulty, tags, hp, hpperlevel,
#        mp, mpperlevel, movespeed, armor, armorperlevel, spellblock, spellblockperlevel, attackrange,
#        hpregen, hpregenperlevel, mpregen, mpregenperlevel, crit, critperlevel, attackdamage, attackdamageperlevel,
#        attackspeedperlevel, attackspeed
# FROM matches2020
# JOIN championstats c on matches2020.redtop = c.id
# WHERE redteam = 'Fnatic'
# UNION
# SELECT bluetop as champion, attack, defense, magic, difficulty, tags, hp, hpperlevel,
#        mp, mpperlevel, movespeed, armor, armorperlevel, spellblock, spellblockperlevel, attackrange,
#        hpregen, hpregenperlevel, mpregen, mpregenperlevel, crit, critperlevel, attackdamage, attackdamageperlevel,
#        attackspeedperlevel, attackspeed
# FROM matches2020
# JOIN championstats c on matches2020.bluetop = c.id
# WHERE blueteam = 'Fnatic'
# ORDER BY champion, difficulty desc; #done