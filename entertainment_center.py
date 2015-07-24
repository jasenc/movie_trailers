#Import fresh_tomatoes.py in order to use the provided (and altered) website template
import fresh_tomatoes

#Import media.py in order to use the Movie Class
import media

#Instantiate Movie class with first movie drive
drive = media.Movie('Drive',
                    'Ryan Gosling stars as a Los Angeles wheelman for hire, stunt driving for movie productions by day and steering getaway vehicles for armed heists by night.',
                    'https://upload.wikimedia.org/wikipedia/en/1/13/Drive2011Poster.jpg',
                    'https://www.youtube.com/watch?v=Pe6eOqheva8',
                    'Nicolas Winding Refn',
                    'Sep 16, 2011')

burn_after_reading = media.Movie('Burn After Reading',
                    'At the headquarters of the Central Intelligence Agency in Arlington, Va., analyst Osborne Cox arrives for a top-secret meeting.',
                    'https://upload.wikimedia.org/wikipedia/en/a/ae/Burn_After_Reading.jpg',
                    'https://www.youtube.com/watch?v=eMWu6i7l5ec',
                    'Coen Brothers',
                    'Aug 27, 2008')

ex_machina = media.Movie('Ex Machina',
            'A programmer at an internet-search giant, wins a competition to spend a week at the private mountain estate of the company\'s brilliant and reclusive CEO',
            'http://t3.gstatic.com/images?q=tbn:ANd9GcQe8L-1PTMlUf-si2Oy6BTd9ZtbWH7BSRSF5k5JGNATxOHzyIdg',
            'https://www.youtube.com/watch?v=EoQuVnKhxaM',
            'Alex Garland',
            'Apr 24, 2015')

kingsman = media.Movie('Kingsman: The Secret Service',
            'A super-secret spy organization that recruits an unrefined but promising street kid into the agency\'s ultra-competitive training program just as a global threat emerges from a twisted tech genius.',
            'http://t3.gstatic.com/images?q=tbn:ANd9GcTn2E6bqcLehK92h215qFnUpCYFqt02Iuwg-N4gVBmixzAXvGfZ',
            'https://www.youtube.com/watch?v=m4NCribDx4U',
            'Matthew Vaughn',
            'Feb 13, 2015')

interstellar = media.Movie('Interstellar',
                'With our time on Earth coming to an end, a team of explorers undertakes the most important mission in human history; traveling beyond this galaxy to discover whether mankind has a future among the stars.',
                'http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB',
                'https://www.youtube.com/watch?v=0vxOhd4qlnA',
                'Christopher Nolan',
                'Nov 7, 2014')

sin_city = media.Movie('Sin City',
            'this violent crime noir paints the picture of the ultimate town without pity through the eyes of its roughest characters.',
            'http://ia.media-imdb.com/images/M/MV5BMTI2NjUyMDUyMV5BMl5BanBnXkFtZTcwMzU0OTkyMQ@@._V1_SX640_SY720_.jpg',
            'https://www.youtube.com/watch?v=r0PDOQglpDQ',
            'Robert Rodriguez, Quentin Tarantino, Frank Miller (II), Frank Miller',
            'Apr 1, 2005')


movies = [drive, burn_after_reading, ex_machina, kingsman, interstellar, sin_city]


fresh_tomatoes.open_movies_page(movies)
