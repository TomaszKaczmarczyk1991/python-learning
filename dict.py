pulp_fiction = {
    "title": "Pulp Fiction",
    "director": "Quentin Tarantino",
    "year": 1994,
    "imdb_rating": 8.8,
    "main_cast": [
        "John Travolta",
        "Samuel L. Jackson",
        "Uma Thurman",
        "Bruce Willis",
        "Ving Rhames",
        "Harvey Keitel",
    ],
    "genres": ["Crime", "Drama"],
    "mpaa_rating": "R",
    "awards_summary": {
        "oscars_nominations": ["Best Picture", "Best Actor (Travolta)", "Best Supporting Actor (Jackson)", "Best Original Screenplay"],
        "wins": []
    }
}

# Accessing Data In Dictionaries
print(pulp_fiction["director"]) # Quentin Tarantino
print(pulp_fiction["mpaa_rating"]) # R
print(pulp_fiction["main_cast"]) # ['John Travolta', 'Samuel L. Jackson', 'Uma Thurman', 'Bruce Willis', 'Ving Rhames', 'Harvey Keitel']
print(pulp_fiction["main_cast"][1]) # Samuel L. Jackson


# Adding and Updating Data In Dictionaries
pulp_fiction["is_great"] = True
print(pulp_fiction) # {'title': 'Pulp Fiction', 'director': 'Quentin Tarantino', 'year': 1994, 'imdb_rating': 8.8, 'main_cast': ['John Travolta', 'Samuel L. Jackson', 'Uma Thurman', 'Bruce Willis', 'Ving Rhames', 'Harvey Keitel'], 'genres': ['Crime', 'Drama'], 'mpaa_rating': 'R', 'awards_summary': {'oscars_nominations': ['Best Picture', 'Best Actor (Travolta)', 'Best Supporting Actor (Jackson)', 'Best Original Screenplay'], 'wins': []}, 'is_great': True}
pulp_fiction["imdb_rating"] += 1.0
print(pulp_fiction["imdb_rating"]) # 9.8
pulp_fiction["genres"].append("Comedy")
print(pulp_fiction["genres"]) # ['Crime', 'Drama', 'Comedy']

# pop(), popitem(), clear()

pulp_fiction.pop("awards_summary") # returns item
print(pulp_fiction) # {'title': 'Pulp Fiction', 'director': 'Quentin Tarantino', 'year': 1994, 'imdb_rating': 9.8, 'main_cast': ['John Travolta', 'Samuel L. Jackson', 'Uma Thurman', 'Bruce Willis', 'Ving Rhames', 'Harvey Keitel'], 'genres': ['Crime', 'Drama', 'Comedy'], 'mpaa_rating': 'R', 'is_great': True}

pulp_fiction.popitem() # pops the latest added item
print(pulp_fiction) # {'title': 'Pulp Fiction', 'director': 'Quentin Tarantino', 'year': 1994, 'imdb_rating': 9.8, 'main_cast': ['John Travolta', 'Samuel L. Jackson', 'Uma Thurman', 'Bruce Willis', 'Ving Rhames', 'Harvey Keitel'], 'genres': ['Crime', 'Drama', 'Comedy'], 'mpaa_rating': 'R'}

# Clear
pulp_fiction.clear()
print(pulp_fiction) # {}

# Update
pulp_fiction.update({
    "title": "Pulp Fiction",
    "director": "Quentin Tarantino",
    "year": 1994,
    "imdb_rating": 8.8,
})

print("Updated: ")
print(pulp_fiction)

# **trick
actors = {"main_cast": [
        "John Travolta",
        "Samuel L. Jackson",
        "Uma Thurman",
        "Bruce Willis",
        "Ving Rhames",
        "Harvey Keitel",
    ]}
new_pulp_fiction = {**pulp_fiction, **actors}

print(new_pulp_fiction)

# Union |
imdb = {"imdb_rating": 8.8,}
genres = {"genres": ["Crime", "Drama"]}

new_pulp_fiction = pulp_fiction | imdb | genres
print(new_pulp_fiction)