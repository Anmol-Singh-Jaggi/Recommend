 

import java.io.IOException;

/**
 * Sample Class that instantiates different recommenders for movielens 100K data set
 * and outputs their performance statistics for comparison
 */
public class CompareRecommenders {

	public static void main ( String[] args ) 
			throws IOException	
	{
		BaseRecommender baserec = null;	

		
		System.out.println("Creating data access object...");
		DAO dao = new DAO("data/u1.base", "data/u1.test", "\t");
		System.out.println("Data access object created.");
		
		System.out.println("\nBase Recommender");
		baserec = new BaseRecommender(dao);
		System.out.println("Training...");
		baserec.train();
		System.out.println("Testing...");
		baserec.evaluate("output/baserec.predict");
		
		System.out.println("\nUser User Collaborative Filtering Recommender");
		baserec = new UUCollaborativeFiltering(dao, 378, 12);
		System.out.println("Training...");
		baserec.train();
		System.out.println("Testing...");
		baserec.evaluate("output/uucf.predict");
		dao.userMeanDeNormalize();
		
		System.out.println("\nItem Item Collaborative Filtering Recommender");
		baserec = new IICollaborativeFiltering(dao, 1116, 10);
		System.out.println("Training...");
		baserec.train();
		System.out.println("Testing...");
		baserec.evaluate("output/iicf.predict");
		dao.itemMeanDeNormalize();
		
		// Commented because it takes too much time
		/*
		System.out.println("\nSlope One Recommender");
		baserec = new SlopeOneRecommender(dao);
		System.out.println("Training...");
		baserec.train();
		System.out.println("Testing...");
		baserec.evaluate("output/slopeone.predict");
		*/
		
	}
}
