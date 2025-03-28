# initialize list
favorite_movies = []


# add movies function
def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added ")


# remove movie function
def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed")
    else:
        print(f"Movie '{movie}' not found")


# display movies function
def display_movies():
    print("My Awesome Movie List")
    for movie in favorite_movies:
        print(f" {movie}")


# count movie function
def count_movies():
    for movie in favorite_movies:
        count = favorite_movies.count(movie)
        print(f"{count}")


# find movie function
def find_movie(movie):
    if movie in favorite_movies:
        print(f"{movie} found! ")
    else:
        print(f"{movie} not in movie list!")


# clear movie list function
def clear_movies():
    favorite_movies.clear()
    print(f"Movie List Cleared")


add_movie("Freaky Friday")

display_movies()

count_movies()

clear_movies()

display_movies()
