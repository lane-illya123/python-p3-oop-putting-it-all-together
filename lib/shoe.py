#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.repaired = False
        self.condition = 'Used'


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,value):
        if type(value) == int:
            print("The shoe has been repaired.")   
            self._size = value
        else:
            print("size must be an integer")  
          
    def cobble(self):
        self.repaired = True
        self.condition = 'New'
        print("Your shoe is as good as new!")      
        