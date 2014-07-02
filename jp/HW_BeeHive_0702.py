import random
import numpy 
import matplotlib.pyplot as plt
from matplotlib.pyplot import pcolor, show, contour 

num_bees = 1000
soldier_portion = 0.1

y = [] 
z = []
two_d_plot = []
r = 0.00025
max_hit = 100

class Soldier_bee:
    at = 2
    hp = 1
    ammo = 1
    victim = 0
    panic = False

    def __init__ (self):
        self.warmonger = random.random()

    def be_alert(self,defcon,enemy):
        if defcon >= (1.0 - self.warmonger) : #go attack      
            self.attack(enemy)


    def attack(self, enemy):
        if self.ammo > 0 :
            enemy.hp = enemy.hp - self.at
            self.ammo = self.ammo  -1
            boolean_attack = True
            if self.ammo == 0:
                self.victim = self.victim+1
        if enemy.hp > 0 : 
            self.panic = True 

class Worker_bee:
    rp = 0.35
    hp = 1
    ammo = 3
    victim = 0
    threshold = 0 
    panic = False

    def __init__ (self):
        self.defence = random.random()#numpy.random.power(2)

    def be_alert(self,defcon,hive):
        if hive.hhp <= 800*(1-self.threshold): ##############################
            if defcon >= (1-self.defence): 
                self.repair(hive)

    def repair(self, hive):
        if self.ammo > 0 :
            hive.hhp = hive.hhp + self.rp
            self.ammo = self.ammo - 1
            if self.ammo == 0:
                self.victim = self.victim+1
        if hive.hhp < 100 :
            self.panic = True

class Hive:
    hhp = 800

class Enemy:
    hp = 800

    scariness = 0.06
    
    def destroy(self, hive):
        hive.hhp = hive.hhp - (self.scariness*1000)

# Threshold of worker_bee participation  
for j in range (0,100):

    nth_row = []

    # Percentage of soldier_bee  
    for i in range (0,100):

        x = []
        soldier_portion = float(i) * 0.01
        x.append(soldier_portion)
        
        num_s_bees = int(num_bees*soldier_portion)
        num_w_bees = int(num_bees*(1-soldier_portion))
        s_bees = []
        w_bees = []
        hive = Hive()
        enemy = Enemy()
        s_victim = 0
        w_victim = 0 

        for index in range(0,num_s_bees):
            s_bee = Soldier_bee()
            s_bees.append(s_bee)

        for index in range(0,num_w_bees):
            w_bee = Worker_bee()
            w_bee.threshold = float(j) * 0.01
            w_bees.append(w_bee)
 

        defcon = enemy.scariness

        step = 0
        prior_enemy_hp = enemy.hp + 1.0

        while (enemy.hp)*(hive.hhp)*(max_hit-step) > 0:

            prior_enemy_hp = enemy.hp

            if hive.hhp > 0 :
                enemy.destroy(hive)
                
                for s_bee in s_bees:
                    s_bee.be_alert(defcon,enemy)
                for w_bee in w_bees:
                    w_bee.be_alert(defcon,hive)
                
                for s_bee in s_bees:
                    if s_bee.panic == True:
                        #print defcon
                        defcon = defcon + r
                        #print defcon, "!"
            step = step +1 

        for s_bee in s_bees:
            if s_bee.ammo == 0:
                s_victim = s_victim + 1

        for w_bee in w_bees:
            if w_bee.ammo == 0:
                w_victim = w_victim + 1

        survivals = 1000 - (w_victim + s_victim)
        nth_row.append(survivals)
        #print j, i
        
    two_d_plot.append(nth_row)


# Result 
print "done"    
pcolor(numpy.array(two_d_plot))
plt.colorbar()
show()

