import media
import fresh_tomatoes

baby_driver = media.Movie("Baby Driver",
                          "Baby is a young and partially hearing impaired getaway driver.",
                          "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/baby-driver-poster.jpg",
                          "https://www.youtube.com/watch?v=z2z857RSfhk")

emoji_movie = media.Movie("The Emoji Movie",
                          "The Emoji Movie unlocks the never-before-seen secret world inside your smartphone.",
                          "http://www.impawards.com/2017/posters/emoji_movie_ver10.jpg",
                          "https://www.youtube.com/watch?v=r8pJt4dK_s4")

pitch_perfect_three = media.Movie("Pitch Perfect 3",
                                  "The farewell tour begins this December. Meet the Pitches.",
                                  "https://movies.universalpictures.com/media/pp3-teaser-onesheet-594da88174a10-1.png",
                                  "https://www.youtube.com/watch?v=Hihto8onbUU")

atomic_blonde = media.Movie("Atomic Blonde",
                            "Agent Lorraine Broughton willing to deploy any of her skills to stay alive on her impossible mission.",
                            "https://filmwonk.files.wordpress.com/2017/07/atomic-blonde-poster.jpg",
                            "https://www.youtube.com/watch?v=yIUube1pSC0")

suicide_squad = media.Movie("Suicide Squad",
                            "Assemble a team of the world's most dangerous Super Villains and send them off to defeat an enigmatic entity.",
                            "https://i.pinimg.com/originals/d9/e0/d2/d9e0d2996919ffb10fbfbd53b7359b48.jpg",
                            "https://www.youtube.com/watch?v=CmRih_VtVAs")

sausage_party = media.Movie("Sausage Party",
                            "The products at Shopwell's Grocery are made to believe a code that gave them happy lives until they move out.",
                            "https://www.moviehd-free.com/wp-content/uploads/2016/12/Sausage-Party-2016-%E0%B8%9B%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%95%E0%B8%B5%E0%B9%89%E0%B9%84%E0%B8%AA%E0%B9%89%E0%B8%81%E0%B8%A3%E0%B8%AD%E0%B8%81-e1482324250306.jpg",
                            "https://www.youtube.com/watch?v=WVAcTZKTgmc")

deadpool = media.Movie("Deadpool",
                       "Armed with new abilities and a twisted humor, Deadpool hunts down the man who destroyed his life.",
                       "http://i0.kym-cdn.com/photos/images/facebook/001/048/695/5e2.jpg",
                       "https://www.youtube.com/watch?v=gtTfd6tISfw")

warcraft = media.Movie("Warcraft",
                       "The peaceful realm of Azeroth stands on the brink of war as it faces a fearsome race of invaders.",
                       "http://wow.zamimg.com/uploads/screenshots/normal/509284.jpg",
                       "https://www.youtube.com/watch?v=2Rxoz13Bthc")

independence_day = media.Movie("Independence Day",
                               "Two decades after the freak alien invasion that nearly destroyed mankind a new threat emerges.",
                               "https://www.leitersburgcinemas.com/sites/leitersburgcinemas.com/files/posters/id42.jpg",
                               "https://www.youtube.com/watch?v=LbduDRH2m2M")

ghostbusters = media.Movie("Ghostbusters",
                           "Following a ghost invasion, paranormal enthusiasts band together to stop the otherworldly threat.",
                           "http://cdn.collider.com/wp-content/uploads/2015/12/ghostbusters-kristen-wiig-poster.jpg",
                           "https://www.youtube.com/watch?v=w3ugHP-yZXw")

# a list of all movie instances
movies = [atomic_blonde, baby_driver, deadpool, emoji_movie, ghostbusters,
          independence_day, pitch_perfect_three, sausage_party, suicide_squad,
          warcraft]

# calls function that creates/generates the html output page using the movie
# instances in the movies list
fresh_tomatoes.open_movies_page(movies)
