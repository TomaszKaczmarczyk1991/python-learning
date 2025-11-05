random_stuff = [True, "Hi", 444, []]

premier_league_2025 = ["Chelsea", "Manchester City", "Brighton", "Aston Villa",
                       "Arsenal", "Crystal Palace", "Brentford", "Newcastle",
                       "Leeds", "Fulham", "West Ham", "Burnley",
                       "Nottingham Forest", "Wolverhampton", "Tottenham",
                       "Liverpool", "Sunderland", "Bournemouth", "Everton",
                       "Manchester United"]

print(len(premier_league_2025)) # 20


pl = list("Premier League")
print(pl) # ['P', 'r', 'e', 'm', 'i', 'e', 'r', ' ', 'L', 'e', 'a', 'g', 'u', 'e']

teams = list(range(1, 21))
print(teams) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


langs = ["Python", "C++", "C#", "HTML", "CSS", "JavaScript", "SQL", "PHP", "Java", "Rust", "Go", "Kotlin", "Lua"]
print(langs[0]) # Python
print(langs[5]) # JavaScript
print(langs[-1]) # Lua
print(langs[-2]) # Kotlink


random_stuff.append("Appended Item")
print(random_stuff) # [True, 'Hi', 444, [], 'Appended Item']

friends = ["Tom", "Jacob", "Michael"]
girls = ["Riley", "Lana", "Lily"]

friends.extend(girls)
print(friends) # ['Tom', 'Jacob', 'Michael', 'Riley', 'Lana', 'Lily']

friends.insert(0, "Eva")
print(friends) # ['Eva', 'Tom', 'Jacob', 'Michael', 'Riley', 'Lana', 'Lily']
friends.insert(2, "Joel")
print(friends) # ['Eva', 'Tom', 'Joel', 'Jacob', 'Michael', 'Riley', 'Lana', 'Lily']
friends.insert(-1, "John")
print(friends) # ['Eva', 'Tom', 'Joel', 'Jacob', 'Michael', 'Riley', 'Lana', 'John', 'Lily']
friends.append("Chad")
print(friends) # ['Eva', 'Tom', 'Joel', 'Jacob', 'Michael', 'Riley', 'Lana', 'John', 'Lily', 'Chad']