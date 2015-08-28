# Movie Trailer Website

Using Python and server-side code this application dynamically generates a web page to display favorite movies, including their box art imagery, movie trailer URLs, and some additional information. It contains the following files:

* `media.py`: Stores the class Movie for which movie objects can be instantiated from.
* `entertainment_center.py`: Holds all of the data necessary for each movie object.
* `fresh_tomatoes.py`: Dynamically outputs an `index.html` file that references `main.css` and `script.js` after looping through each movie object. Additionally it utilizes the `webbrowser`, `os`, and `re` libraries found in Python.

A preview can be found at [jasencarroll.com/movie_trailers](http://www.jasencarroll.com/movie_trailers/)


## Installation

After ensuring Python is installed on your local or virtual machine, in order to run this program:

1. Navigate to the directory in which you want to install Tournament Results.
2. Clone this repository to that directory.

## Execution & Customization

To successfully run this application, run `python entertainment_center.py`.

To change the movies displayed on the webpage:

1. Open `entertainment_center.py` in your favorite text editor.
2. Edit the movies of your liking, each movie/object must the exact arguments called for in the `__init__` method of the Movie class, found in `media.py`.

## Author

Jasen Carroll  
jasen.c@icloud.com  
July 24th, 2015
