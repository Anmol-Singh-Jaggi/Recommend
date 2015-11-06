**Description**  
Implementation of a recommender system as taught in this [course][1] using Java.  

Algorithms included:  
 - User-User collaborative filtering with vector cosine similarity  
 - Item-Item collaborative filtering with vector cosine similarity  
 - Slope one item-based recommender algorithm  

*New algorithms can be developed by extending the BaseRecommender class.*  

**Requirements:**  
 - Java compiler  
 - Perl interpreter (optional; only for recreating the dataset)  
 - GNU Make  

**Installation:**  
 - Generate the dataset by going into `/data` and executing `./mku.sh`.  
 (If it gives an error, try tweaking the Perl location hashbang in `allbut.pl`)  
 - Execute the makefile - `./make`  

**TODO**  
 - Add implementation of the FunkSVD algorithm.  

[1]:https://www.coursera.org/learn/recommender-systems
