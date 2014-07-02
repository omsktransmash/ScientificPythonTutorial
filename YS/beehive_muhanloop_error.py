import random
import numpy
from matplotlib import pyplot

num_fight_bee=1000
num_worker_bee=1000
num_Ultralisk = 1
num_bees = num_fight_bee + num_worker_bee
GDP = 1000

# Define class 
class Fight_Bee:
    atk = 4
    hp = 100
    mp = 0
    ammo = 1
    panic = False


    def __init__(self):
        self.warmonger = numpy.random.random()

    def be_alert(self,defcon,enemy):
        if defcon >= (1.0-self.warmonger):    ##ATTACK!!!!  # The higher the self.warmonger, the higher the chance to attack.
            self.attack(enemy)

    def attack(self, enemy):
        if self.ammo >0:
            enemy.hp = enemy.hp - self.atk
            self.ammo = self.ammo - 1
        if enemy.hp > 0:
            self.panic = True    ##내가 공격을 했을 때 상대방이 죽지 않았을 경우 panic  (Default for panic is False)

class Worker_Bee:
    hp = 1
    panic = False

    def gain_GDP(self, GDP):
        if num_workerbee >= 500:
            Hive.GDP = Hive.GDP + 100  ##worker bee only affects the hive's GDP. does NOT attack

    
class Hive:
    hp = 1000
    GDP = 500
    alert_level = 0.0
    num_fight_bee=1000
    num_worker_bee=1000
    num_bees = num_fight_bee + num_worker_bee

    def __init__(self, num_fight_bee, num_worker_bee):
        self.bees = []
        for index in range (0, num_fight_bee):
            fbee=Fight_Bee()
            self.bees.append(fbee)
        for index in range (0, num_worker_bee):    
            wbee=Worker_Bee()
            self.bees.append(wbee)

    '''

    def create_bee(self):
        if self.GDP >= 300:
            num_fight_bee = num_fight_bee + 50
            num_worker_bee = num_worker_bee + 50
'''

    def upgrade (self):
        if self.GDP >= 1000:
            self.hp = self.hp + 1000

    def revive (self, step):
        if step == 10:
            self.hp = self.hp +1000
        elif  step == 20:
            self.hp = self.hp + 120
        elif step == 30:
            self.hp = self.hp + 150
            

    
class Ultralisk:
    atk = 1000
    hp = 1000
    mp = 1000
    ammo = 1000
    panic = False

    def __init__(self):
        self.warmonger = numpy.random.random()

    def gg(self, enemy):
        if Hive.hp <= 10:
            self.attack(enemy)
            
    def attack(self, enemy):
        if self.ammo >0:
            enemy.hp = enemy.hp - self.atk
            self.ammo = self.ammo - 1
        if enemy.hp > 0:
            self.panic = True    ##내가 공격을 했을 때 상대방이 죽지 않았을 경우 panic  (Default for panic is False)
        

class Enemy:
    hp = 700
    scariness = 0.01
    atk = 200
    ammo = 1000
    attack = True

    def __init__self():
        self.warmonger = numypy.random.random()

    def attack(self, hive):
        if self.ammo >0:
            hive.hp = hive.hp - self.atk
            self.ammo = self.ammo - 1
'''
class Stronger_Enemy:
    hp = 1400
    scariness = 0.05
    atk = 500
    ammo = 1000
    attack = True

    def __init__self():
        self.warmonger = numpy.random.random()

    def attack(self, hive):
        if Enemy.hp <0:
            if self.ammo>0:
                hive.hp=hive.hp - self.atk
                self.ammo = self.ammo - 1
'''
defcon = 0.0

hive= Hive(num_fight_bee, num_worker_bee)
## bee list 생성

worker_bees = []
for index in range(0,num_worker_bee):
    worker_bee=Worker_Bee()
    worker_bees.append(worker_bee)

fight_bees = []
for index in range(0, num_fight_bee):
    fight_bee = Fight_Bee()
    fight_bees.append(fight_bee)

#generate hive
#hive= Hive(num_bees)
    
#generate enemy    
enemy = Enemy()
defcon = enemy.scariness

steps= []
hps =[]
step = 0




while enemy.hp > 0 :

    prof = Ultralisk()
    prof.gg(enemy)

    enemy = Enemy()
    enemy.attack(hive)
## 적의 hp가 0보다 클 때 계속 공격
    for fight_bee in fight_bees:
        fight_bee.be_alert(defcon, enemy) 

    ## 벌 한마리가 패닉에 빠지면 데프콘 증가
    num_panic = 0
    for bee in fight_bees:
        if bee.panic == True:
            defcon = defcon + 0.0001
            Hive.alert_level = Hive.alert_level + 0.0001
            num_panic = num_panic + 1


    hattcherry = Hive(num_fight_bee, num_worker_bee)
 #   hattcherry.create_bee()
    hattcherry.upgrade()
    hattcherry.revive(step)

    steps.append(step)
    hps.append(enemy.hp)

    
    step = step + 1

pyplot.plot(steps,hps) #(x축 y 축)
pyplot.show()

