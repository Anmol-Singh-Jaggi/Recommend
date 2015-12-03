MATCH (m:Movie)<-[r:RATED]-(u:User)
WITH m,  COLLECT(r.rating) AS ratings
WITH m,  REDUCE(s=0,i IN ratings | s+i)*1.0/SIZE(ratings) AS avg
SET m.avg_rating = avg
// RETURN m
// ORDER BY m.movieID
;