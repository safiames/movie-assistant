import random

movie_list = ["Batman", "Harry Potter", "Glass Onion", "Thor", "Superman"]

while True:
    user_input = input("Enter a command: ")
    if user_input == "pick a movie":
        random_movie = random.choice(movie_list)
        print("Your movie is:", random_movie)

    elif user_input == "exit":
        break
