import webbrowser


class Movie():
    """This class creates instances of Movie"""
    def __init__(self, movie_title, movie_storyline,
                 movie_release_date, movie_rating,
                 rotten_tomatoes_link, poster_image,
                 trailer_youtube):
        # Assigns the various movie related info to each instance
        self.title = movie_title
        self.storyline = movie_storyline
        self.release_date = movie_release_date
        self.rating = movie_rating
        self.rotten_tomatoes_url=rotten_tomatoes_link
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
