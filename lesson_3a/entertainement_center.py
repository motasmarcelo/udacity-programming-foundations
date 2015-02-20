#!/bin/env python

import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print(toy_story.storyline)
avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()

forrest_gump = media.Movie("Forrest Gump",
                            "Run Forrest, run!!",
                            "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                            "https://www.youtube.com/watch?v=eYSnxZKTZzU")

forrest_gump.show_trailer()