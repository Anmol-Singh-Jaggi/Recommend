MATCH (u1:User {userID:?1})-[x:RATED]->(m:Movie)<-[y:RATED]-(u2:User) 
WITH SUM((x.rating-u1.avg_rating) * (y.rating-u2.avg_rating)) AS xyDotProduct, 
     SQRT(REDUCE(xDot = 0.0, a IN COLLECT(x.rating) | xDot + (a-u1.avg_rating)^2 )) AS xLength,  
     SQRT(REDUCE(yDot = 0.0, b IN COLLECT(y.rating) | yDot + (b-u2.avg_rating)^2 )) AS yLength,
     u1, u2 
MERGE (u1)-[s:SIMILARITY]-(u2) 
SET s.similarity = 
CASE xLength * yLength 
     WHEN 0
      THEN 0
     ELSE
      xyDotProduct / (xLength * yLength)
END
;