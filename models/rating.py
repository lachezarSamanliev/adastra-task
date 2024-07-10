class Rating:
    """
    Custom class to represent a rating object with attributes.

    Attributes:
        user_id (int): The ID of the user who made the rating.
        movie_id (int): The ID of the movie being rated.
        rating (float): The user's rating for the movie (e.g., 3.0).
        timestamp (int): The timestamp of the rating (e.g., 1260759179).
    """
    def __init__(self, user_id, movie_id, movie_rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.movie_rating = movie_rating
        self.timestamp = timestamp

    def __repr__(self):
        return f"Rating(user_id={self.user_id}, movie_id={self.movie_id}, rating={self.movie_rating}, timestamp={self.timestamp})"