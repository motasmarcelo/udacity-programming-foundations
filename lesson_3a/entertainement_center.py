#!/bin/env python

import media
import fresh_tomatoes

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

# forrest_gump.show_trailer()

braveheart = media.Movie("Braveheart",
                            "A man fights for his rights and leads a nation to freedom",
                            "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                            "https://www.youtube.com/watch?v=wj0I8xVTV18")

matrix = media.Movie("The Matrix",
                            "If you could  knowing the truth, would you choose it?",
                            "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                            "https://www.youtube.com/watch?v=m8e-FF8MsqU")

interestellar = media.Movie("Interstellar",
                            "Go further.",
                            "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=BYUZhddDbdc")

astral_city = media.Movie("Astral City",
                            "Do you believe in the afterlive?",
                            "https://upload.wikimedia.org/wikipedia/en/9/9f/Nosso_Lar.jpg",
                            "https://www.youtube.com/watch?v=htTPUb5BTIo")


movies = [forrest_gump, braveheart, matrix, interestellar, astral_city, toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)