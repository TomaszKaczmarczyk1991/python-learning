# Sets

my_set = {1, 2, 3, 4}

my_set.add(5)
print(my_set) # {1, 2, 3, 4, 5}

my_set.add(-4)
print(my_set) # {1, 2, 3, 4, 5, -4}
# The order of elements may appear random because sets are unordered

print(len(my_set)) # 6

# remove(), discard(), clear()
my_set.remove(3)
print(my_set) # {1, 2, 4, 5, -4}

my_set.discard(-4)
print(my_set) # {1, 2, 4, 5}

my_set.clear()
print(my_set) # set()

# Intersection
first_set = {1, 2, 3, 5}
second_set = {2, 3, 4, 6}

print(first_set & second_set) # {2, 3}

# Union
print(first_set | second_set) # {1, 2, 3, 4, 5, 6}

# Difference
print(first_set - second_set) # {1, 5}
print(second_set - first_set) # {4, 6}