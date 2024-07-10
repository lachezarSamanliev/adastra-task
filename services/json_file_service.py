import json
import os

def save_outputs_to_json(movies_average_rating, top_five_rated_movies, movies_per_year, extracted_genres):
    """
    Saves extracted data to JSON files.

    Args:
        movies_average_rating (pandas.Series): Series containing average ratings per movie (indexed by movieId).
        top_five_rated_movies (pandas.DataFrame): DataFrame containing the top 5 highest rated movies.
        movies_per_year (pandas.Series): Series containing counts of movies released each year (indexed by year).
        extracted_genres (dict): Dictionary containing counts of movies in each genre (key=genre name, value=count).
    """
    json_avg_ratings = 'averageRatings.json'
    json_top_five_movies = 'topFive.json'
    json_yearly_releases = 'releases.json'
    json_genres = 'genres.json'

    # write_dataframe_dict_to_json(json_avg_ratings, movies_average_rating)
    # write_dataframe_dict_to_json(json_top_five_movies, top_five_rated_movies)
    # write_dataframe_dict_to_json(json_yearly_releases, movies_per_year)
    write_dataframe_dict_to_json(json_genres, extracted_genres)


def write_dataframe_dict_to_json(json_filename, extracted_data):
    """
    Writes a dictionary (or Series) to a JSON file with specified filename.

    Args:
        json_filename (str): Filename for the JSON file.
        extracted_data (dict or pandas.Series): Data to be written to the JSON file.
    """
    folder_path = 'json'
    os.makedirs(folder_path, exist_ok=True)
    # Construct the full file path
    file_path = os.path.join(folder_path, json_filename)
    
    with open(file_path, 'w') as json_file:
        json.dump(extracted_data, json_file, indent=4)