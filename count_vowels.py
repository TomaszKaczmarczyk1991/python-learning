def count_vowels(text):
    counter = 0
    for ch in text:
        if ch in "aeiou":
            counter += 1
    return counter

print(count_vowels("Hi, mate!")) # 3
print(count_vowels("www.ccc.pl")) # 0