import requests as r

# This is the class
class Pokemon():
    def __init__(self,name='Pikachu',data='',type='',weight='',abilities=[]):
        self.name = name
        self.data = data
        self.type = type
        self.weight = weight
        self.abilities = abilities


    def call(self):
        call_string = 'https://pokeapi.co/api/v2/pokemon/' + self.name.lower()
        response = r.get(call_string)
        self.data = response.json()
        return self.data

    def get_info(self):
        self.name = self.data['name'].upper()
        self.type = self.data['types'][0]['type']['name']
        self.weight = self.data['weight']
        
        for i in self.data['abilities']:
            self.abilities.append(i['ability']['name'])

# This is creating an object using a class
my_pokemon = Pokemon()

# This is just me using attributes and methods (functions within a class) on my object
print(my_pokemon.name)
print(my_pokemon.call())
print(my_pokemon.data)
my_pokemon.get_info()
print(my_pokemon.name)
print(my_pokemon.type)
print(my_pokemon.abilities)