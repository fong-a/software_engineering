# Initialize an empty dictionary for the movie collection
movie_collection = {}

# Add movies to the collection
movie_collection["The Shawshank Redemption"] = {"director": "Frank Darabont", "year_released": 1994, "genre": "Drama"}
movie_collection["The Godfather"] = {"director": "Francis Ford Coppola", "year_released": 1972, "genre": "Crime"}
movie_collection["Pulp Fiction"] = {"director": "Quentin Tarantino", "year_released": 1994, "genre": "Crime"}

# Print the movie collection
for title, details in movie_collection.items():
    print(f"Title: {title}")
    print(f"Director: {details['director']}")
    print(f"Year Released: {details['year_released']}")
    print(f"Genre: {details['genre']}")
    print()
