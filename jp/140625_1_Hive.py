
import random
import numpy
from matplotlib import pyplot

num_bees = 1000

class Bee:
    at = 1
    hp = 1
    mp = 0
    ammo = 1
    panic = False 

    def __init__ (self):
        self.warmonger = numpy.random.power(2)

    def be_alert(self,defcon,enemy):
        if defcon >= (1.0 - self.warmonger) : #go attack      
            self.attack(enemy)

    def attack(self, enemy):
        if self.ammo > 0 :
            enemy.hp = enemy.hp - self.at
            self.ammo = self.ammo  -1
        if enemy.hp > 0 : 
            self.panic = True 

        

class Enemy:
    hp = 800
    scariness = 0.05

bees = []
for index in range(0,num_bees):
    bee = Bee()
    bees.append(bee)

enemy = Enemy()
defcon = enemy.scariness

steps = []
hps = []

step = 0 

while enemy.hp > 0:

    for bee in bees:
        bee.be_alert(defcon,enemy)

    num_panic = 0 
    for bee in bees:
        if bee.panic == True:
            defcon = defcon + 0.0001
            num_panic = num_panic + 1 

    step=step+1
    steps.append(step)
    hps.append(enemy.hp)
    

print steps, hps
    
pyplot.plot(steps, hps)
pyplot.show()
