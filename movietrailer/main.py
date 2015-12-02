import movie
import fresh_tomatoes

list_movies = []

#Movie creation
toy_story = movie.Movie("Toy Story","Toy come to life","http://pixar-planet.fr/wp-content/uploads/2010/04/affiche-toy-story-23.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc&ab_channel=MoviesHistory")
mystic_river = movie.Movie("Mystic River", "Revenge story","https://upload.wikimedia.org/wikipedia/en/9/93/Mystic_River_poster.jpg" ,"https://www.youtube.com/watch?v=nmiA24jwlbM&ab_channel=inso99")
kill_bill = movie.Movie("Kill Bill","A woman in a wedding dress, the Bride, lies wounded in a church in El Paso, having been attacked by the Deadly Viper","http://www.impawards.com/2003/posters/kill_bill_ver4_xlg.jpg","https://www.youtube.com/watch?v=ot6C1ZKyiME&ab_channel=gangsterartist007")

#Adding movies to list
list_movies += [toy_story,mystic_river,kill_bill]

#Sending the list to the website
fresh_tomatoes.open_movies_page(list_movies)