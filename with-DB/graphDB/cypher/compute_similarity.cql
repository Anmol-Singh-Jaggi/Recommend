MATCH (u1:User {userID:'?1'})-[x:RATED]->(m:Movie)<-[y:RATED]-(u2:User)
WITH  SUM(x.rating * y.rating) AS xyDotProduct,
      SQRT(REDUCE(xDot = 0.0, a IN COLLECT(x.rating) | xDot + a^2)) AS xLength,
      SQRT(REDUCE(yDot = 0.0, b IN COLLECT(y.rating) | yDot + b^2)) AS yLength,
      u1, u2
MERGE (u1)-[s:SIMILARITY]-(u2)
SET s.similarity = xyDotProduct / (xLength * yLength);
