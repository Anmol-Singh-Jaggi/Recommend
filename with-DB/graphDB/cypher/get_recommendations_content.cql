MATCH (u:User {userID:?1})-[r:RATED]->(m:Movie)-[:GENRE]-(g)
WITH u, g, COLLECT(m) AS mlist
WITH u, g, SIZE(mlist) AS msize
WITH u, g, msize ORDER BY msize DESC
WITH u, collect(g)[0..5] AS glist
WITH u, glist
// got favorite genres in glist
MATCH (:User)-[r:RATED]->(m:Movie)-[:GENRE]-(g)
WHERE NOT ((u)-[:RATED]->(m))
WITH g, m, glist,collect(r) AS rlist
WHERE g IN glist AND SIZE(rlist)>3
RETURN m.movieID AS `Movie ID`,  m.name AS `Movie Name`, m.avg_rating AS `Average Rating`
ORDER BY m.avg_rating DESC
;