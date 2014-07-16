import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


## Hive + Enemy

num_bees = 10

x=[] #  number of worker
y=[] #  number of warrior
z=[] #  enemy win : 0,  bee win :1

for num_worker in range(0,11):

    for enemy_hp in range(20,31):

        num_warrior=num_bees-num_worker

        alert=False

        class Queen_Bee:
            
            hp=10    
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

            at=1
            dead = False

            def attack(self,enemy):
                enemy.hp=enemy.hp-self.at
                    

        class Worker_Bee:

            dead = False
            def work(self, queen):
                queen.nutrition=queen.nutrition+1
            

        class Enemy:
            
            hp=enemy_hp
            at=3
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



        ## Bee, Enemy »ý¼º


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

        y=enemy.hp
        
        ## Fight


        while enemy.hp>0 and queen.hp>0:

            for worker in worker_bee:
                worker.work(queen)
                
            for warrior in warrior_bee:
                warrior.attack(enemy)

            new_warrior_bee=[]
            for warrior in warrior_bee:
                if warrior.dead==False:
                    new_warrior_bee.append(warrior)
            warrior_bee=new_warrior_bee



            enemy.attack(worker_bee, warrior_bee, queen)

            if len(warrior_bee)<=0:
                alert=True
            else:
                alert=False


            queen.make_bees(worker_bee, warrior_bee)

        print num_warrior
        
        x=num_worker

        if queen.hp<0:
            queen.hp=0
            z.append([x,y,queen.hp])
        else:
            z.append([x,y,queen.hp])
            

print z

plt.figure()
CS=plt.contour(z)         
plt.show()
