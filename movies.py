import random

movie_list = ["2gether: The Movie", "Love of Siam", "Yes Or No", "Tootsies and the Fake", "Ghost Lab"]

movie_summaries = {
    "2gether: The Movie": "The film follows the relationship between Tine and Sarawat, two college students who pretend to be in a relationship to win a music competition. As they spend more time together, their feelings for each other become real, but their newfound love is put to the test when they face challenges from their friends, family, and the media.",
    "Love of Siam": "A Thai romantic drama film that tells the story of two childhood friends, Mew and Tong, who are reunited after years apart. As they reconnect, they must navigate their feelings for each other while also dealing with personal issues, family problems, and a mysterious disappearance.",
    "Yes Or No": "Romantic comedy-drama film that tells the story of Pai, a college girl who is openly gay, and her new roommate, Kim, who is initially uncomfortable with Pai's sexuality. As they spend more time together, however, they begin to develop feelings for each other, leading to a complicated relationship. ",
    "Tootsies and the Fake": "Comedy film that tells the story of four gay friends - Song, Kanda, Pong, and Pongsatorn who try to expose a fraudulent psychic medium who has swindled their boss. In order to infiltrate the psychic's inner circle, the friends create new identities as a wealthy family and their servants. As they carry out their plan, they face unexpected challenges and comedic mishaps.",
    "Ghost Lab": "A Thai horror film that follows two doctors, Wee and Gla, who become obsessed with proving the existence of ghosts after experiencing a paranormal encounter during a hospital emergency. They conduct a series of experiments to document and analyze supernatural phenomena, which leads them to confront their own personal demons and the consequences of their actions. "
}

movie_genres = {
    "2gether: The Movie": ["romance", "comedy"],
    "Love of Siam": ["mystery", "Thai"],
    "Yes Or No": ["LGBTQ", "Thai", "romance"],
    "Tootsies and the Fake": ["comedy", "Thai"],
    "Ghost Lab": ["supernatural", "horror"]
}

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

    # command 'quit' will end the program
    elif command == "quit":
        break

    else:
        print("Invalid command. Please enter a valid command.")
