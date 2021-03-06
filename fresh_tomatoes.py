import webbrowser
import os
import re

# Styles and scripting for the page.
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Jasen's Top Movies</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.5/darkly/bootstrap.min.css">
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,600' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="main.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="script.js"></script>
  </head>
'''

# The main page layout and title bar.
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-default navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Jasen's Top Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template.
movie_tile_content = '''
      <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
        <img src="{poster_image_url}" width="220" height="342">
        <h2>{movie_title}</h2>
        <h5>{movie_release}</h5>
        <h6>{movie_director}</h6>
        <p>{movie_synopsis}</p>
      </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page.
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url.
        youtube_id_match = re.search(r'(?<=v=)[^&#]+',
                                     movie.trailer_youtube_url)
        youtube_id_match = (youtube_id_match or
                            re.search(r'(?<=be/)[^&#]+',
                                      movie.trailer_youtube_url))
        trailer_youtube_id = (youtube_id_match.group(0) if
                              youtube_id_match else None)

        # Append the tile for the movie with its content filled in.
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,

            # Adding custom content.
            movie_director=movie.director,
            movie_release=movie.release_date,
            movie_synopsis=movie.synopsis
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file.
    output_file = open('index.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically
    # generated content.
    rendered_content = main_page_content.format(
                           movie_tiles=create_movie_tiles_content(movies))

    # Output the file.
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser.
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # Open in a new tab, if possible.
