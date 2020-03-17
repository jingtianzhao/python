import tensorflow as tf
import numpy as np
class dog:
    def __init__(self,weight,hight,blood,power):
        self.hight =hight
        self.weight=weight
        self.power=power
        self.blood=blood
    def attach(self,dog2):
        dog2.blood =dog2.blood -self.power
    def bark(self):
        print(f'me blood is {self.blood} my power is {self.power}')#importance
d1 =dog(1,2,10,2)
d2 =dog(1,3,15,3)
d1.bark()
d1.attach(d2)
d2.bark()
