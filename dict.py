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

