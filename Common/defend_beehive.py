import random
import numpy
import matplotlib.pyplot as plt

num_bees = 1000

class Bee:
    at = 1
    hp = 1
    mp = 0
    ammo = 1
    signal_help = False
    

    def __init__(self):
        self.warmonger = numpy.random.power(2)
        #print self.warmonger

    def be_alert(self,hive,enemy):
        #print alert_level
        
        if (1.0 - hive.alert_level) <= self.warmonger:
            ##go attack the enemy
            self.attack_enemy(enemy)
            if enemy.hp > 0: ##still alive
                self.signal_help = True

    def attack_enemy(self,enemy):
        if self.ammo > 0:
            self.ammo = self.ammo - 1
            enemy.hp = enemy.hp - self.at

class Hive:
    alert_level = 0.0
    def __init__(self,num_bees):
        self.bees = []
        for index in range(0,num_bees):
            bee = Bee()
            self.bees.append(bee)

class Enemy:
    hp = 800
    scariness = 0.01
    
##generate hive
hive = Hive(num_bees)

##generate enemy
enemy = Enemy()

hive.alert_level = enemy.scariness

steps = []
num_helps = []
step = 0

while enemy.hp > 0:
    for bee in hive.bees:
        bee.be_alert(hive,enemy)

    num_help  = 0
    for bee in hive.bees:
        #print bee.status
        if bee.signal_help == True:
            hive.alert_level = hive.alert_level + 0.0001
            num_help = num_help + 1

    print enemy.hp, hive.alert_level

    steps.append(step)
    num_helps.append(num_help)
    
    step = step +1


plt.plot(steps,num_helps)
plt.show()
