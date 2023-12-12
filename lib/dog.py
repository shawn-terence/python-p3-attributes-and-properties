#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="fido",breed="Corgi"):
        self.name=name
        self.breed=breed
    # breed
    def get_breed(self):
        return self._breed
    def set_breed(self,breed):
        if breed in APPROVED_BREEDS:
            
            self._breed=breed
        else:
            print("Breed must be in list of approved breeds.")
    # name   
    def get_name(self):
        print("getting name")
        return self._name
    
    def set_name(self,name):
        if not isinstance(name,str):
            print("Name must be string between 1 and 25 characters.")
        elif 1<= len(name) <= 25:
            self._name=name
        else:
            print("Name must be string between 1 and 25 characters.")
    name=property(get_name,set_name)
    breed=property(get_breed,set_breed)
    
tp=Dog("","Pointer")

