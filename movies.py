import random
from movie_library import movie_list, movie_summaries, movie_genres

# create a list of all the movie genres
all_genres = sum(movie_genres.values(), [])
all_genres_set = set(all_genres)
all_genres_list = list(all_genres_set)

introduction_text = """The program will ask you to input commands. Following commands are available:
'pick a movie' = prints a random movie from the list and its summary
'pick a date'  = lets user to specify how many and which dates they want a suggestion for
'pick a genre' = prints a list of genres to choose from
'quit'         = exits the program
"""
print(introduction_text)
# create a dictionary to store the movies selected for each date
dates_to_movies = {}
while True:

    # ask the user to enter a command
    command = input("Enter a command: ")

    # user inputs a command

    # command 'pick a movie' will provide random movie from the list
    if command == "pick a movie":
        random_movie = random.choice(movie_list)

        # program prints random movie name and a summary
        print("Recommended movie: " + random_movie)
        print("Summary: " + movie_summaries[random_movie])

    # command 'pick a date' will provide random movie for the specific date(s)'
    elif command == "pick a date":
        num_dates = int(input("How many dates do you want to enter? "))
        for i in range(num_dates):
            date = input("Enter date #" + str(i+1) + ": ")
            random_movie = random.choice(movie_list)
            print("For " + date + ", we recommend: " + random_movie)
            print("Summary: " + movie_summaries[random_movie])

    # command 'choose a genre' provides a list of movie genres
    elif command == "choose a genre":
        print(all_genres_list)
        chosen_genre = input("Please enter the name of the genre you'd like to choose: ")
        if chosen_genre not in all_genres_list:
            print("No movies in that genre.")

        # list for found movies genres
        suggested_movies_from_genres = []

        for movie, genres in movie_genres.items():
            if chosen_genre in genres and movie in movie_list:
                suggested_movies_from_genres.append(movie)
        print(suggested_movies_from_genres)
    
    # command 'quit' will end the program
    elif command == "quit":
        break
    else:
        print("Invalid command. Please enter a valid command.")