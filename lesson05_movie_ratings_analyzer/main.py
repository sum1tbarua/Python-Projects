from ratings_data import ratings
from utilities import *

if __name__ == '__main__':
    print("=== Movie Ratings Analyzer ===")
    print()

    print("Unique users:")
    print(get_unique_users(ratings))
    print()

    print("Unique movies:")
    print(get_unique_movies(ratings))
    print()

    print("Ratings for Inception:")
    print(get_movie_ratings(ratings,"Inception"))
    print()

    print("Average rating per movie:")
    print(average_rating_per_movie(ratings))
    print()

    print("Highest rated movie:")
    print(highest_rated_movie(ratings))
    print()

    print("Ratings >=9:")
    print(high_ratings(ratings,9))