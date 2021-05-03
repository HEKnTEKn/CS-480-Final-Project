SELECT id as name, tags as type, hp, mp as mana, movespeed, armor,
       spellblock as magic_resist, attackrange, hpregen, mpregen as manaregen, attackdamage, attackspeed

From championstats
WHERE tags LIKE '%{1}%'
ORDER BY id; #done

-- queries a tag to retrieve all stats in ascending order
# SELECT id as name, tags as type, hp, mp as mana, movespeed, armor,
#        spellblock as magic_resist, attackrange, hpregen, mpregen as manaregen, attackdamage, attackspeed
#
# From championstats
# WHERE tags LIKE '%Assassin%'
# ORDER BY id; #done
#
