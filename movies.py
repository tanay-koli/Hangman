movie_names = [
    "Sholay", "Deewar", "Lagaan", "Dilwale", "Barfi", "Dangal", "Queen", "Sultan", "Raees", 
    "Chhichhore", "Drishyam", "Joker", "Tamasha", "Thappad", "Badla", "Padman", "Raazi",
    "Sanju", "Simran", "Krrish", "Parineeta",  "Andhadhun", "Piku", 
    "Rocky", "Omkara",  "Kesari", "Kalank", "Jawan", "Fan", "Lootera",
     "Singham", "Ghajini", "Kahaani", "Talaash", "Holiday", "Baahubali", "War",
    "Cocktail",  "Baazigar",  "Shaandaar", "Simmba", "Hera",
    "Housefull", "Aashiqui", "Robot", "Raanjhanaa", "Raavan", "Kites", "Dhoom", "Tumbbad", "Jhund", "Runway",
    "Golmaal",  "Kaabil", "Antim",  "Haider", "Pink", "October", "Sultan",
    "Rocketry", "Neerja",  "Rustom", "Kesari",  "Tamasha", "Talvar", 
]


# Write the movie names into a text file
file_name = "words.txt"
with open(file_name, "w") as file:
    for movie in movie_names:
        file.write(movie.lower() + "\n")