import ast
import pandas as pd

from models.movies_metadata import MoviesMetadata

def read_ratings_to_df_and_analyze(filename):
    """
    Reads movie ratings data from a CSV file and calculates average ratings per movie.

    Args:
        filename (str): Path to the CSV file containing movie ratings data.

    Returns:
        pandas.Series: Series containing average rating per movie (indexed by movieId).
    """
    ratings_data = []
    for chunk in read_csv_chunks(filename):
        ratings_data.append(chunk)

    # Concatenate the chunks into a single DataFrame
    data = pd.concat(ratings_data)
    average_rating_per_movie = data.groupby('movieId')['rating'].mean()
    return average_rating_per_movie

def read_metadata_csv_to_df(filepath):
    """
    Reads movie metadata from a CSV file, ensuring required fields are present and valid.

    Args:
        filepath (str): Path to the CSV file containing movie metadata.

    Returns:
        pandas.DataFrame: DataFrame containing cleaned and validated movie metadata.
    """
    # Define the column names based on CSV structure
    column_names = [
        'adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id', 'imdb_id',
        'original_language', 'original_title', 'overview', 'popularity', 'poster_path',
        'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime',
        'spoken_languages', 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count'
    ]
    
    # Read the CSV file without specifying data types
    chunks = pd.read_csv(filepath, chunksize=10000, skiprows=1, names=column_names)
    
    # Initialize an empty DataFrame to append chunks
    metadata_df = pd.DataFrame()
    
    for chunk in chunks:
        # Handle NaN values in the 'id' column
        chunk['id'] = pd.to_numeric(chunk['id'], errors='coerce')  # Convert to numeric, forcing NaNs for non-convertible values
        chunk = chunk.dropna(subset=['id'])  # Drop rows where 'id' is NaN
        chunk['id'] = chunk['id'].astype(int)  # Convert 'id' to integers

        # Append the chunk to the main DataFrame
        metadata_df = pd.concat([metadata_df, chunk], ignore_index=True)
    
    metadata_df = remove_duplicates_with_data_frames(metadata_df)

    return metadata_df

def read_csv_chunks(filepath):
  """
  Reads a CSV file in chunks using pandas read_csv.

  Args:
      filepath: Path to the CSV file.

  Yields:
      pandas.DataFrame: DataFrames containing chunks of the CSV file.
  """
  for chunk in pd.read_csv(filepath, chunksize=1000, names=['userId', 'movieId', 'rating', 'timestamp'], skiprows=1):
    yield chunk

def extract_top_five_movies_by_vote_average(movies_data):
    """
    Extracts the top 5 movies based on vote average from given movie data.

    Args:
        movies_data (pandas.DataFrame): DataFrame containing movie data including 'vote_average'.

    Returns:
        pandas.DataFrame: DataFrame containing the top 5 highest rated movies.
    """
    top_n = 5
    top_n_movies = movies_data.sort_values(by='vote_average', ascending=False).head(top_n)
    return top_n_movies

def extract_release_date_movies(movies_data):
    """
    Extracts the number of movies released each year from given movie data.

    Args:
        movies_data (pandas.DataFrame): DataFrame containing movie data including 'release_date'.

    Returns:
        pandas.Series: Series containing counts of movies released each year (indexed by year).
    """
    movies_data['release_date'] = pd.to_datetime(movies_data['release_date'], errors='coerce')
    movies_data['release_year'] = movies_data['release_date'].dt.year
    movies_per_year = movies_data['release_year'].value_counts().sort_index()
    return movies_per_year

def extract_genres(movies_data):
    """
    Extracts the number of movies in each genre from given movie data.

    Args:
        movies_data (pandas.DataFrame): DataFrame containing movie data including 'genres'.

    Returns:
        dict: Dictionary containing counts of movies in each genre (key=genre name, value=count).
    """
    genre_counts = count_genres(movies_data)
    return genre_counts

def count_genres(metadata_df):
    """
    Counts the number of movies in each genre from the 'genres' column of movie metadata.

    Args:
        metadata_df (pandas.DataFrame): DataFrame containing movie metadata including 'genres'.

    Returns:
        dict: Dictionary containing counts of movies in each genre (key=genre name, value=count).
    """
    genre_counts = {}

    for genres_str in metadata_df['genres']:
        genres_list = ast.literal_eval(genres_str) if pd.notnull(genres_str) else []
        for genre in genres_list:
            genre_name = genre['name']
            if genre_name in genre_counts:
                genre_counts[genre_name] += 1
            else:
                genre_counts[genre_name] = 1

    return genre_counts

def remove_duplicates_with_data_frames(df):
    """
    Removes duplicate rows from a DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame containing potential duplicate rows.

    Returns:
        pandas.DataFrame: DataFrame with duplicates removed.
    """
    unique_df = df.drop_duplicates()
    return unique_df

def has_duplicates(list):
  """
    Checks for duplicates in a list.

    Args:
        lista (list): Input list to check for duplicates.

    Returns:
        bool: True if duplicates are found, False otherwise.
    """
  seen = set()  # Create an empty set to keep track of seen elements
  duplicates = 0
  for item in list:
    if item not in seen:
      seen.add(item)
    else:
      print(item.title)
      duplicates += 1
  print(duplicates)
  return duplicates > 0  # Return True if duplicates exist, False otherwise

## Method to read csv, convert to List of Python Objects
## Not used for task execution
def read_metadata_to_list_object(filename):
    """
    Reads movie metadata from a CSV file into a list of MoviesMetadata objects.

    Args:
        filename (str): Path to the CSV file containing movie metadata.

    Returns:
        list: List of MoviesMetadata objects representing movie metadata.
    """
    df = pd.read_csv(filename)
    metadata_list = []

    for _, row in df.iterrows():
        # Convert the row to a dictionary and create a MoviesMetadata object
        movie = MoviesMetadata(**row.to_dict())
        metadata_list.append(movie)
    
    print("Len of Metadata List")
    print(len(metadata_list))
    return metadata_list