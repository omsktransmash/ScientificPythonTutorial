import random
import numpy
import matplotlib.pyplot as plt

#declare constants
num_bees = 1000
warrier_ratio=0.3 #ration of warrier bees
num_warriers = int(num_bees * warrier_ratio)
num_workers = int(num_bees - num_warriers)

#declare running modes
random_hp = False
do_regeneration = False

class Bee:
    at = 1
    hp = 1
    mp = 0
    ammo = 1
    signal_help = False
    

    def __init__(self):
        self.warmonger = numpy.random.power(2)
        #print self.warmonger

        if random_hp:
            self.hp=random.randint(1,5) 

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

class Worker(Bee):
    repair = 1
    
    def __init__(self):
        Bee.__init__(self)

    def regenerate_hive(hive):
        #regenerate hive.
        hive.hp += repair


class Warrier(Bee):
    
    def __init__(self):
        Bee.__init__(self)
        self.at=random.randint(3,10) #3~10 attack power


   

    

class Hive:
    hp = 1000
    alert_level = 0.0
    def __init__(self,num_workers, num_warriers):
        self.bees = []
        for index in range(0,num_workers):
            bee = Worker()
            self.bees.append(bee)

        for index in range(0,num_warriers):
            bee = Warrier()
            self.bees.append(bee)

class Enemy:
    name = "Enemy"
    hp = 800

    def __init__(self, enemy_name):
        self.name = enemy_name
        self.at = random.randint(0,100)
        self.scariness = self.at / 1000.0


    def attack_hive(self, hive):
        hive.hp= hive.hp-self.at
    
    
##generate hive
hive = Hive(num_workers, num_warriers)

##generate enemy
enemies = []
enemies.append(Enemy("Joker"))
enemies.append(Enemy("Golum"))
enemies.append(Enemy("Pooh^^"))






for enemy in enemies:
    steps = [0]
    num_helps = [0]
    step = 0
    
    print enemy.name + " Attacks Hive. ("+str(enemy.scariness)+")"

  

    hive.alert_level = enemy.scariness
    enemy.attack_hive(hive)

    for bee in hive.bees:
        bee.signal_help = False
    
    while enemy.hp > 0 :
        
        
        for bee in hive.bees:
            bee.be_alert(hive,enemy)

        num_help  = 0
        for bee in hive.bees:
            #print bee.status
            if bee.signal_help == True:
                hive.alert_level = hive.alert_level + 0.0001
                num_help = num_help + 1

        #for bee in hive.bees:
        #    if type(bee) is Worker:
        #        bee.regenerate_hive(hive)

        #print enemy.hp, hive.alert_level

        step = step +1

        steps.append(step)
        num_helps.append(num_help)


    print enemy.name + " died. "

    for bee in hive.bees:
        if type(bee) is Worker:
            bee.regenerate_hive(hive)



    lines = plt.plot(steps,num_helps,'o',label=enemy.name)
    
    print steps, num_helps

plt.legend()
plt.show()
