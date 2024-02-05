import random
# Collects the user's genres to know where to select the anime items
def get_user_genre(genres):
        genre = []
        try:
          # infinite loop used to continuously ask the user for their genre selection
          # until they decide they are done
          # or until they've selected all available genre selections
           while True:
                    print(', '.join(list(genres)))
                    like = input('Enter a genre you like: ').capitalize()
                    if like in genre:
                         print('You already used that, try another')
                         continue
                    if like not in genres:
                         print("That's not in the genre selection, try again")
                         continue
                    genre.append(like)
                    print(f'You picked: {", ".join(genre)}')
                    if len(genre) == len(genres):
                        print('Max genre amount exceeded')
                        break
                    else:
                        again = input('Wanna enter another? (y for yes, anything else for no): ').lower()
                        if again != 'y':
                            break
           return genre
        except ValueError:
             print('No numbers')


# Gets number amount of animes the user would like recommended to them
def get_anime_amount(genres):
     # infinite loop used in case a ValueError gets raised
     # else, the function exits as normal
    while True:
         try:
              number = int(input('How many animes would you like recommended to you?: '))
              if number > min(len(i) for i in genres.values()):
                   number = min(len(i) for i in genres.values())
              return number
         except ValueError:
              print('Must be a whole number')

# Recommends the animes, with their corresponding streaming platforms
def rec_user_anime(user, num, platforms, genres):
     print()
     for i in user:
          print(f'Since you like {i}, you should try:')
          # creates a randomly sampled list of animes, based on the genre name inside of the "user" list of genres, in the number amount that the user entered for
          # then iterates through that randomly sampled list
          for anime_name in random.sample(genres[i], k=num):
               # list created to contain supported streaming platforms
               platform_list = []
               # iteration for matching case (the streaming platform, list of animes that the platform supports)
               for platform, anime_list in platforms.items():
                    # if the anime name is inside of the platform-supported animes, then it gets appended as an anime that is in fact, supported by the corresponding streaming platform
                    if anime_name in anime_list:
                        platform_list.append(platform)
               # Prints the anime name, along with the streaming platform it can be watched on
               print(f'{anime_name}: {", ".join(platform_list)}')
          print() 