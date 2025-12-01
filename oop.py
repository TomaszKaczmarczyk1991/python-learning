class Synth:
    instrument_type = ["Electronic musical instrument", "Electrophone"]
    num_synths = 0
    def __init__(self, name, brand, presets):
        self.name = name
        self.brand = brand
        self.presets = []
        Synth.num_synths += 1
    def add_preset(self, preset):
        if preset not in self.presets:
            self.presets.append(preset)
        else:
            print('A preset with that name already exists!')

subsequent25 = Synth('Subsequent 25', 'Moog', [])
dx7 = Synth('DX 7', 'Roland', [])
ms20 = Synth('MS 20', 'KORG', [])

print(subsequent25) # <__main__.Synth object at 0x100629d00>

print(subsequent25.name) # Subsequent 25
print(subsequent25.brand) # Moog


print(subsequent25.presets)
subsequent25.add_preset('Classic Lead')
print(subsequent25.presets) # ['Classic Lead']
subsequent25.add_preset('Classic Lead') # A preset with that name already exists!
subsequent25.add_preset('Sub Bass')
print(subsequent25.presets) # ['Classic Lead', 'Sub Bass']

print(subsequent25.instrument_type) # ['Electronic musical instrument', 'Electrophone']
print(Synth.num_synths) # 3

one = Synth('One', 'Moog', [])
print(Synth.num_synths) # 4