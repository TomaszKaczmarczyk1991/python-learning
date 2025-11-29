class Synth:
    def __init__(self, name, brand, presets):
        self.name = name
        self.brand = brand
        self.presets = []
    def add_preset(self, preset):
        self.presets.append(preset)

subsequent25 = Synth('Subsequent 25', 'Moog', [])
dx7 = Synth('DX 7', 'Roland', [])
ms20 = Synth('MS 20', 'KORG', [])

print(subsequent25) # <__main__.Synth object at 0x100629d00>

print(subsequent25.name) # Subsequent 25
print(subsequent25.brand) # Moog


print(subsequent25.presets)
subsequent25.add_preset('Classic Lead')
print(subsequent25.presets) # ['Classic Lead']

subsequent25.add_preset('Sub Bass')
print(subsequent25.presets) # ['Classic Lead', 'Sub Bass']