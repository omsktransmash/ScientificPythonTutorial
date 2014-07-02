import random
import numpy
from matplotlib import pyplot  ## == import matplotlib.pyplot



## Hive + Enemy

num_bees = 1000

num_warrior =numpy.random.randint(1,num_bees+1)
num_worker= num_bees - num_warrior

alert=False

print "num warrior", num_warrior
print "num worker", num_worker
print "\n"


class Queen_Bee:
    
    hp=1000    
    dead = False
    nutrition=0

    def make_bees(self,worker_bee, warrior_bee):
        while self.nutrition>0:
            if alert==True:
                warrior_bee.append(Warrior_Bee())
                self.nutrition=self.nutrition-1
            else:
                worker_bee.append(Worker_Bee())
                self.nutrition=self.nutrition-1
                

#warrior_bee, worker_bee's hp==1

class Warrior_Bee:

    at=2
    dead = False

    def attack(self,enemy):
        enemy.hp=enemy.hp-self.at
            

class Worker_Bee:

    dead = False
    def work(self, queen):
        queen.nutrition=queen.nutrition+1
    

class Enemy:
    
    hp=10000
    at=400
    dead = False

    def attack(self, worker_bee, warrior_bee, queen):

        if len(warrior_bee)>=self.at:
            del warrior_bee[0:self.at]
        elif self.at<=len(warrior_bee)+len(worker_bee) and len(warrior_bee)<self.at:
            del worker_bee[0:self.at-len(warrior_bee)]
            del warrior_bee[:]
        elif self.at>len(warrior_bee)+len(worker_bee):
            queen.hp=queen.hp-self.at+len(warrior_bee)+len(worker_bee)
            del warrior_bee[:]
            del worker_bee[:]



## Bee, Enemy 생성


queen=Queen_Bee()
warrior_bee=[]
worker_bee=[]
        
for index in range(0, num_warrior):
    bee=Warrior_Bee()
    warrior_bee.append(bee)

for index in range(0, num_worker):
    bee=Worker_Bee()
    worker_bee.append(bee)

enemy = Enemy()


## Fight


steps= []
enemy_hps = []
queen_hps=[]
num_worker=[]
num_warrior=[]

step = 0

while enemy.hp>0 and queen.hp>0:

    for worker in worker_bee:
        worker.work(queen)

    print "nutrition before 알", queen.nutrition
        
    for warrior in warrior_bee:
        warrior.attack(enemy)

    new_warrior_bee=[]
    for warrior in warrior_bee:
        if warrior.dead==False:
            new_warrior_bee.append(warrior)
    warrior_bee=new_warrior_bee


    print "enemy hp", enemy.hp
    print "num warrior", len(warrior_bee)
    print "num worker", len(worker_bee)

    enemy.attack(worker_bee, warrior_bee, queen)

    print "num warrior", len(warrior_bee)
    print "num worker", len(worker_bee)
    print "qeen hp", queen.hp


    if len(warrior_bee)<=0:
        alert=True
    else:
        alert=False

    print "alert", alert

    queen.make_bees(worker_bee, warrior_bee)

    print "nutrition after 알", queen.nutrition
    print "num warrior", len(warrior_bee)
    print "num worker", len(worker_bee), "\n"
               


    step=step+1
    steps.append(step)
    enemy_hps.append(enemy.hp)
    queen_hps.append(queen.hp)
    num_worker.append(len(worker_bee))
    num_warrior.append(len(warrior_bee))
    

# print steps, "\n", enemy_hps, "\n"    , queen_hps, "\n" , num_worker, "\n", num_warrior

pyplot.plot(steps, enemy_hps, label="enemy_hps")
pyplot.plot(steps, queen_hps, label="queen_hps")
pyplot.plot(steps, num_worker, label="# of worker bee")
pyplot.plot(steps, num_warrior, label="# of warrior bee")
pyplot.legend()            
pyplot.show()



