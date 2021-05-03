SELECT id, movespeed
FROM championstats
WHERE tags LIKE '%{1}%'
ORDER BY movespeed; #done

-- queries a tag to retrieve movespeed in ascending order
# SELECT id, movespeed
# FROM championstats
# WHERE tags LIKE '%Assassin%'
# ORDER BY movespeed;
