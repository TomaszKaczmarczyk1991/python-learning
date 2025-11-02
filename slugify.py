def slugify(text):
    return text.lower().strip().replace(" ", "-")

print(slugify("  I like LEARNING pyThOn   ")) # i-like-learning-python