import media
import fresh_tomatoes
#importing for functionalities included in media and fresh_tomatoes classes
bahubali = media.Movie("Baahubali", "A story of throne", "image/bahubali.jpg",
                       "https://www.youtube.com/watch?v=G62HrubdD6o&t=20s")
#bahubali is instance with four attribues
#media.Movie constructor with four attributes title, description, poster, link to trailer

highway = media.Movie("Highway", "Truth inside houses", "image/highway.jpg",
                      "https://www.youtube.com/watch?v=LSrDD52bx4A")

sherlock = media.Movie("Sherlock Holmes", "A Detective", "image/sherlock.jpg",
                       "https://www.youtube.com/watch?v=DpxtbtnC1u8")

Perks = media.Movie("Perks of being a wallflower", "Truth inside houses",
                    "image/perks.jpg",
                    "https://www.youtube.com/watch?v=baDepG3Zc4s")

harry = media.Movie("Harry Potter Series",
                    "A fiction of magical world",
                    "image/harry.jpg",
                    "https://www.youtube.com/watch?v=K1KPcXRMMo4")

lion = media.Movie("Lion",
                   "A story of belongingness",
                   "image/lion.jpg",
                   "https://www.youtube.com/watch?v=-RNI9o06vqo")
#adding movie instances to a list
movie = [highway, bahubali, sherlock, Perks, harry, lion]
#passing the list to movies_page() function as parameter
fresh_tomatoes.open_movies_page(movie)
