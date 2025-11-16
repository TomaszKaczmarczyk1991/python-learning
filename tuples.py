# tuples

moogs = ("DFAM", "Subharmonicon", "Labyrinth", "Spectravox", "Mother 32")
t = (True, False, 88, "Text", [])

# empty_tuple = ()
# empty_tuple = tuple()

# single_tuple = "Single",
# single_tuple = ("Single",)

print(moogs[0]) # DFAM
print(moogs[2]) # Labyrinth

print(len(moogs)) # 5

# slice
moog_sound_studio = moogs[:3]
print(moog_sound_studio) # ('DFAM', 'Subharmonicon', 'Labyrinth')

# moog_sound_studio[2] = 'Behringer Edge'
# TypeError: 'tuple' object does not support item assignment

# index method
print(moog_sound_studio.index('Subharmonicon')) # 1

# count method
print(moog_sound_studio.count('DFAM')) # 1

# in operator
print('Behringer Edge' in moog_sound_studio) # False
print('Labyrinth' in moog_sound_studio) # True

# for
for synth in moog_sound_studio:
    print(synth)
# DFAM
# Subharmonicon
# Labyrinth

# t = (True, False, 88, "Text", [])
t[4].append('LOL') # (True, False, 88, 'Text', ['LOL'])
print(t)

coordinates = {(43.3991, 16.2066): "Maslinica"}
print(coordinates[(43.3991, 16.2066)]) # Maslinica


