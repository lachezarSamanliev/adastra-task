import logging
from services import csv_file_service, json_file_service

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function executed when the script is run directly.

    """
    FILENAME_RATINGS = 'csv/ratings_small.csv'
    FILENAME_METADATA = 'csv/movies_metadata.csv'

    try:
        # 1. Load the dataset from a CSV file
        movies_data = csv_file_service.read_metadata_csv_to_df(FILENAME_METADATA)
        logging.info("Loaded metadata successfully.")

        # 2. Print the number of the unique movies in the dataset.
        print("\nNumber of Unique Movies in metadata:")
        print(len(movies_data))

        # 3. Print the average rating of all the movies
        movies_average_rating = csv_file_service.read_ratings_to_df_and_analyze(FILENAME_RATINGS)
        # print movie Ids and rating
        # I was not able to correctly find movieIds from result here to movies_metadata ids
        print("\nMovie Ids by Average Rating:")
        for movieId, rating in movies_average_rating.items():
            print(f"{movieId} \t\t {rating:.2f}")
        logging.info("Calculated average ratings successfully.")


        # 4. Print the top 5 highest rated movies
        top_five_rated_movies = csv_file_service.extract_top_five_movies_by_vote_average(movies_data)
        print("\nTop 5 Rated Movies:")
        for index, row in top_five_rated_movies.iterrows():
            print(f"ID: {row['id']} \t Title: {row['title']} \t Vote Average: {row['vote_average']:.2f}")
        logging.info("Extracted top 5 rated movies successfully.")


        # 5. Print the number of movies released each year
        movies_per_year = csv_file_service.extract_release_date_movies(movies_data)
        print("\nNumber of Movies Released Each Year:")
        for year, count in movies_per_year.items():
            print(f"Year: {year} \t Movies Released: {count}")
        logging.info("Extracted movies released per year successfully.")

        # 6. Print the number of movies in each genre
        extracted_genres = csv_file_service.extract_genres(movies_data)
        print("\nNumber of Movies in Each Genre:")
        for genre, count in extracted_genres.items():
            print(f"Genre: {genre} \t Movies: {count}")

        logging.info("Extracted movies per genre successfully.")

        # 7. Save the dataset to a JSON file
        logging.info("Sending Data Frames to json service class.")
        json_file_service.save_outputs_to_json(movies_average_rating, top_five_rated_movies, movies_per_year, extracted_genres)
    
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}", exc_info=True)
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
