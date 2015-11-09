#Implementation using Neo4j  

**Setup**  
Before doing anything else, first do these steps:  
 - Copy `paths.py.sample` to another file `paths.py` and change the variables in `paths.py` according to your system  
 - Generate a sample graph database: go to `setup_sample_graph/` and read the instructions  

**Requirements**  
 - Neo4j
 - Python 2  

**To-Do**  
 - Add support for generating error-statistics:  
  - Divide the input dataset into 80%/20% train/test dataset  
  - Add the properties `trainRating`, `testRating` to the `:RATED` relationship  
  - Then, let the usual algorithm run on the property `trainRating` and generate the property `predictedRating` for all the relationships having the property `testRating`  
  - The error-statistics can now be generated using `testRating` and `predictedRating` properties  


