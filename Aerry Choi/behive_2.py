import random
import numpy

num_bees=1000
num_workers=1000

class Bee:
    at=1
    hp=2
    mp=0
    ammo=1
    panic=False

    def __init__(self):
        self.warmonger=numpy.random.power(2)

    def be_alert(self,defcon,enemy):
        if defcon >= (1.0-self.warmonger):##go attack!
            self.attack(enemy)
        if defcon <= (1.0-self.warmonger):
            self.attacked(enemy)

    def attack(self,enemy):
        if self.ammo>0:            
            enemy.hp=enemy.hp-self.at
            self.ammo=self.ammo-1
            
        if self.hp>0:
            self.panic=True
            
    def attacked(self,enemy):
        if self.at<1:
            self.hp=self.hp-enemy.at
            enemy.hp=enemy.hp-1
        if self.hp<0:
            print 'bee died'
            
        
        
        



class Enemy:
    hp=800
    at=1
    scariness= 0.01
    
    def attack(self, behive):
        if self.hp>0:
            behive.hp=behive.hp-self.at


class Behive:
    hp=10
    
    
##hive

defcon=0.0

bees=[]

for index in range(0, num_bees):
    bee=Bee()
    bees.append(bee)
behive=Behive()
enemy=Enemy()
defcon=enemy.scariness


while enemy.hp>0 and behive.hp>0:
    
    for bee in bees:
        bee.be_alert(defcon,enemy)

    num_panic=0

    for bee in bees:
        if bee.panic==True:
            defcon=defcon+0.0001
            num_panic=num_panic+1
            

    print enemy.hp, behive.hp, defcon, num_panic
   
  
