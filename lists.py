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

print(friends[1:6]) # ['Tom', 'Joel', 'Jacob', 'Michael', 'Riley']

print(friends[7:]) # ['John', 'Lily', 'Chad']

friends[2:5] = ["Rose"]
print(friends) # ['Eva', 'Tom', 'Rose', 'Riley', 'Lana', 'John', 'Lily', 'Chad']

print(friends[1:5:2]) # ['Tom', 'Riley']

friends[0:1] = []
print(friends) # ['Tom', 'Rose', 'Riley', 'Lana', 'John', 'Lily', 'Chad']

friends.clear()
print(friends) # []

langs.remove("HTML") # removes only the first match!
print(langs) # ['Python', 'C++', 'C#', 'CSS', 'JavaScript', 'SQL', 'PHP', 'Java', 'Rust', 'Go', 'Kotlin', 'Lua']

langs.pop()
print(langs) # ['Python', 'C++', 'C#', 'CSS', 'JavaScript', 'SQL', 'PHP', 'Java', 'Rust', 'Go', 'Kotlin']

# langs.pop(idx)
langs.pop(7)
print(langs) # ['Python', 'C++', 'C#', 'CSS', 'JavaScript', 'SQL', 'PHP', 'Rust', 'Go', 'Kotlin']

android_app_lang = langs.pop()
print(android_app_lang) # Kotlin

del langs[2]
print(langs) # ['Python', 'C++', 'CSS', 'JavaScript', 'SQL', 'PHP', 'Rust', 'Go']

del langs[5:]
print(langs) # ['Python', 'C++', 'CSS', 'JavaScript', 'SQL']

del langs[::2]
print(langs) # ['C++', 'JavaScript']

for team in premier_league_2025:
    print(team)

# Chelsea
# Manchester City
# Brighton
# Aston Villa
# Arsenal
# Crystal Palace
# Brentford
# Newcastle
# Leeds
# Fulham
# West Ham
# Burnley
# Nottingham Forest
# Wolverhampton
# Tottenham
# Liverpool
# Sunderland
# Bournemouth
# Everton
# Manchester United

idx = 0
while idx < len(premier_league_2025):
    print(premier_league_2025[idx])
    idx += 1
    
# Chelsea
# Manchester City
# Brighton
# Aston Villa
# Arsenal
# Crystal Palace
# Brentford
# Newcastle
# Leeds
# Fulham
# West Ham
# Burnley
# Nottingham Forest
# Wolverhampton
# Tottenham
# Liverpool
# Sunderland
# Bournemouth
# Everton
# Manchester United

# List operators

print("Chelsea" in premier_league_2025) # True
print("Bolton" in premier_league_2025) # False

friends.append("Joel")
print(friends + ["Ryan", "Trent"]) # ['Joel', 'Ryan', 'Trent']

# count(), sort(), reverse()

print(friends.count("Joel")) # 1

numbers = [777, 999, -69, 0, 7, 13, 88, 420, 444]
numbers.sort()
print(numbers) # [-69, 0, 7, 13, 88, 420, 444, 777, 999]

numbers.sort(reverse=True)
print(numbers) # [999, 777, 444, 420, 88, 13, 7, 0, -69]

numbers.reverse()
print(numbers) # [-69, 0, 7, 13, 88, 420, 444, 777, 999]