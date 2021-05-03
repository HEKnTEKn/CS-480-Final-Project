SELECT id, tags as type, hp, mp as mana, movespeed, armor,
       spellblock as magic_resist, attackrange, hpregen, mpregen as manaregen, attackdamage, attackspeed
FROM championstats
WHERE id = '{1}'; #done

-- queries a tag to retrieve all stats in ascending order
# SELECT id, tags as type, hp, mp as mana, movespeed, armor,
#        spellblock as magic_resist, attackrange, hpregen, mpregen as manaregen, attackdamage, attackspeed
# FROM championstats
# WHERE id = 'Ahri';
