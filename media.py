import webbrowser


class Movie():
    """
        This class provides a way to store a movie related information that is
        should be present for all the movies displayed.
    """

    def __init__(self, title, storyline, poster, trailer):
        """
            This function creates a new instance of class Movie, that is, each
            movie is an instance which is assigned the parameter self.
        """

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def view_trailer(self):
        """
            This function opens the URL provided under the trailer parameter
            for each movie instance.
        """

        webbrowser.open(self.trailer_youtube_url)
