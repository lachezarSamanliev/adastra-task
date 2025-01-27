from dataclasses import dataclass

@dataclass
class MoviesMetadata:
    """
    Data class representing metadata for movies.

    Attributes:
        id (int): Unique identifier for the movie.
        adult (bool): Indicates if the movie is adult-rated. Defaults to False.
        belongs_to_collection (object): Information about the collection the movie belongs to.
        budget (float): Budget of the movie. Defaults to 0.0.
        genres (list): List of genres the movie belongs to, represented as strings.
        homepage (str): URL of the movie's homepage. Defaults to an empty string.
        imdb_id (str): IMDb ID of the movie. Defaults to an empty string.
        original_language (str): Original language of the movie.
        original_title (str): Original title of the movie.
        overview (str): Overview or synopsis of the movie.
        popularity (float): Popularity score of the movie. Defaults to 0.0.
        poster_path (str): Path to the movie's poster image. Defaults to an empty string.
        production_companies (list): List of production companies involved in the movie, represented as strings.
        production_countries (list): List of production countries for the movie, represented as strings.
        release_date (str): Release date of the movie in string format.
        revenue (float): Revenue generated by the movie. Defaults to 0.0.
        runtime (int): Runtime of the movie in minutes. Defaults to 0.
        spoken_languages (list): List of spoken languages in the movie, represented as strings.
        status (str): Status of the movie (e.g., released, in production).
        tagline (str): Tagline of the movie.
        title (str): Title of the movie.
        video (bool): Indicates if the movie is a video. Defaults to False.
        vote_average (float): Average rating of the movie. Defaults to 0.0.
        vote_count (int): Number of votes/ratings received by the movie. Defaults to 0.

    Methods:
        __hash__(): Returns a hash value combining unique attributes (id, title).
        __eq__(other): Checks equality with another MoviesMetadata object based on id and title.
    """
    id: int  # Converted to integer during parsing
    adult: bool = False  # Default to False
    belongs_to_collection: object = None  # Can be various types, keep as object
    budget: float = 0.0  # Default to 0.0
    genres: list = None  # List of genres (strings)
    homepage: str = ""  # Default to empty string
    imdb_id: str = ""  # Can be empty string
    original_language: str = ""
    original_title: str = ""
    overview: str = ""
    popularity: float = 0.0  # Default to 0.0
    poster_path: str = ""  # Can be empty string
    production_companies: list = None  # List of production companies (strings)
    production_countries: list = None  # List of production countries (strings)
    release_date: str = ""  # String representation of date
    revenue: float = 0.0  # Converted to float during parsing
    runtime: int = 0  # Converted to integer during parsing (assuming runtime in minutes)
    spoken_languages: list = None  # List of languages (strings)
    status: str = ""
    tagline: str = ""
    title: str = ""
    video: bool = False  # Default to False
    vote_average: float = 0.0  # Converted to float during parsing
    vote_count: int = 0  # Converted to integer during parsing


    def __hash__(self):
        """
        Returns a hash value combining the id and title attributes.

        Returns:
            int: Hash value representing the object.
        """
        return hash((self.id, self.title))
    
    def __eq__(self, other):
        """
        Checks equality with another MoviesMetadata object based on id and title.

        Args:
            other (MoviesMetadata): Another MoviesMetadata object to compare with.

        Returns:
            bool: True if both objects have the same id and title, False otherwise.
        """
        return self.id==other.id\
           and self.title==other.title