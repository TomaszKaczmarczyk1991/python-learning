synth_prices = {
    "Behringer Model D": 189,
    "KORG Minilogue XD": 549,
    "Teenage Engineering OP-XY": 2222,
    "Moog Muse": 3099,
    "Moog Minimoog Model D 2022": 4999,
    "Moog One": 12999
}

print(synth_prices.get("Moog One")) # 12999

# Iterating dicts
print(synth_prices.keys()) # dict_keys(['Behringer Model D', 'KORG Minilogue XD', 'Teenage Engineering OP-XY', 'Moog Muse', 'Moog Minimoog Model D 2022', 'Moog One'])

print(synth_prices.values()) # dict_values([189, 549, 2222, 3099, 4999, 12999])

print(synth_prices.items()) # dict_items([('Behringer Model D', 189), ('KORG Minilogue XD', 549), ('Teenage Engineering OP-XY', 2222), ('Moog Muse', 3099), ('Moog Minimoog Model D 2022', 4999), ('Moog One', 12999)])

# Iterating with unpacking
for key, val in synth_prices.items():
    print(key, val)

# Behringer Model D 189
# KORG Minilogue XD 549
# Teenage Engineering OP-XY 2222
# Moog Muse 3099
# Moog Minimoog Model D 2022 4999
# Moog One 12999

max_price = 0
most_expensive_synth = ""
for model, price in synth_prices.items():
    if price > max_price:
        max_price = price
        most_expensive_synth = model
print(f"The most expensive synth in the shop is {model}! It's ${price}!")
# The most expensive synth in the shop is Moog One! It's $12999!