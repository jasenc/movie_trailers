#Import fresh_tomatoes.py in order to use the provided (and altered) website template
import fresh_tomatoes

#Import media.py in order to use the Movie Class
import media

#Instantiate Movie class with first movie drive
drive = media.Movie('Drive',
                    'Ryan Gosling stars as a Los Angeles wheelman for hire, stunt driving for movie productions by day and steering getaway vehicles for armed heists by night.',
                    'http://resizing.flixster.com/wsvgfk1gMjoWAljBtrUAWUtm3H0=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/16/36/11163653_ori.jpg',
                    'https://www.youtube.com/watch?v=Pe6eOqheva8',
                    'Nicolas Winding Refn',
                    'Sep 16, 2011')

# burn_after_reading =
#
# ex_machina =
#
# kingsman =

print drive.synopsis

movies = [drive]

fresh_tomatoes.open_movies_page(movies)
