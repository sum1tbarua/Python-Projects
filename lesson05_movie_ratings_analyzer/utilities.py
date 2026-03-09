# Function 1 — Get unique users
def get_unique_users(data):
    unique_user_set = {item[0] for item in data}
    
    return sorted(unique_user_set)

# Function 2 — Get unique movies
def get_unique_movies(data):
    unique_movie_set = {item[1] for item in data}
    
    return sorted(unique_movie_set)

# Function 3 — Ratings for a specific movi
def get_movie_ratings(data, movie_name):
    movie_ratings_list = [item[2] for item in data if movie_name == item[1]]
    
    return movie_ratings_list

# Function 4 — Average rating per movie
def average_rating_per_movie(data):
    total_movie_dict = dict()
    total_rating_dict = dict()
    average_rating_dict = dict()
    
    for name, movie, rating in data:
        total_movie_dict[movie] = total_movie_dict.get(movie, 0) + 1
        total_rating_dict[movie] = total_rating_dict.get(movie, 0) + rating
    
    for rating in total_rating_dict:
        average = total_rating_dict[rating] / total_movie_dict[rating]
        average_rating_dict[rating] = round(average, 2)
    
    return average_rating_dict

# Function 5 — Highest rated movie
def highest_rated_movie(data):
    max_movie = None
    max_rating = 0
    
    for key, value in average_rating_per_movie(data).items():
        if value > max_rating:
            max_rating = value
            max_movie = key
    
    return max_movie

# Function 6 — Ratings above threshold
def high_ratings(data, threshold):
    high_ratings_list = [item for item in data if item[2] > threshold]
    
    return high_ratings_list
