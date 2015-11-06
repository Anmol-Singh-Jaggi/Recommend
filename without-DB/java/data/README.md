**Description**  
MovieLens data sets were collected by the GroupLens Research Project at the University of Minnesota.
 
This data set consists of:  
 - 100,000 ratings (1-5) from 943 users on 1682 movies  
 - Each user has rated at least 20 movies  
 - Simple demographic info for the users (age, gender, occupation, zip)  

**Detailed description of the data files**  
 - `u.data`: The full u data set, 100000 ratings by 943 users on 1682 items.  
   - Each user has rated at least 20 movies.  
   - Users and items are numbered consecutively from 1.  
   - The data is randomly ordered.  
   - This is a tab separated list of  user id | item id | rating | timestamp.  
   - The time stamps are unix seconds since 1/1/1970 UTC   
 - `u.info`: The number of users, items, and ratings in the u data set.  
 - `u.item`: Information about the items (movies).  
   - This is a tab-separated list of movie id | movie title | release date | video release date | IMDb URL | unknown | Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy | Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi | Thriller | War | Western.  
   - The last 19 fields are the genres, a 1 indicates the movie is of that genre, a 0 indicates it is not; movies can be in several genres at once.  
   - The movie ids are the ones used in the `u.data` data set.  
 - `u.genre`: A list of the genres.  
 - `u.user`: Demographic information about the users.  
   - This is a tab-separated list of user id | age | gender | occupation | zip code.  
   - The user ids are the ones used in the `u.data` data set.  
 - `u.occupation`: A list of the occupations.  
 - `u[1-5].base/u[1-5].test`: The data sets `u1.base` and `u1.test` through `u5.base` and `u5.test` are 80%/20% splits of the u data into training and test data.  
   - Each of u1, ..., u5 have disjoint test sets; this if for 5 fold cross validation (where you repeat your experiment with each training and test set and average the results).  
   - These data sets can be generated from `u.data` by `mku.sh`.  
 - `u[a-b].base/u[a-b].test`: The data sets `ua.base`, `ua.test`, `ub.base`, and `ub.test` split the u data into a training set and a test set with exactly 10 ratings per user in the test set.  
   - The sets `ua.test` and `ub.test` are disjoint.  
   - These data sets can be generated from `u.data` by `mku.sh`.  
 - `allbut.pl`: The script that generates training and test sets where all but n of a users ratings are in the training data.  
 - `mku.sh`: A shell script to generate all the u data sets from `u.data`.  

