# Create a class named Movie which takes an object.
class Movie(object):

    """ This class provides a way to store movie related information,
    as well as a self updating list to keep track of it's instances. """

    # Creating a list to keep track of all instances of this class
    movies = []

    # Define the initial function, which takes the title, synopsis, box art,
    # trailer, director and release date for a Movie. """

    def __init__(self, title, synopsis, poster_image_url, trailer_youtube_url,
                 director, release_date):

        # Define the objects's attritubutes as the arguments that are passed in
        # during instantiation.
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.director = director
        self.release_date = release_date

        # Append each new instance of the class to the list movies.
        self.movies.append(self)
