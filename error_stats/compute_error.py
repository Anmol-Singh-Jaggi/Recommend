import csv
import math

def get_readings(file_path):
    readings = {}
    
    file_handle = open(file_path)
    file_reader = csv.reader(file_handle, delimiter='\t')
    for line in file_reader:
        userID = line[0]
        movieID = line[1]
        rating = line[2]
    	readings.setdefault(userID, {})[movieID] = rating
    
    return readings
    
def main():
    actual_readings = get_readings("data/actual.csv")
    predicted_readings = get_readings("data/predicted.csv")
    
    MAE = 0.0
    RMSE = 0.0
    coverage = 0.0
    readings_total = 0
    readings_compared = 0
    
    for userID, movieID_rating in actual_readings.iteritems():    
        for movieID, rating in movieID_rating.iteritems():
            predicted_rating = predicted_readings.get(userID, {}).get(movieID)
            readings_total += 1
            if not predicted_rating:
                continue
            difference = float(rating) - float(predicted_rating)
            MAE += abs(difference)
            RMSE += difference * difference
            readings_compared += 1
    
    MAE /= readings_compared
    RMSE = math.sqrt(RMSE/readings_compared)
    coverage = (readings_compared * 100.0)/readings_total
    
    print MAE, RMSE, coverage

if __name__ == "__main__":
    main()
    
