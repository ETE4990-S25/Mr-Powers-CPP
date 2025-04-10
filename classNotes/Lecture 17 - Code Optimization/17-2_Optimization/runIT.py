import time
def medium(): 
    time.sleep(0.01) 
 
def light(): 
    time.sleep(0.001) 
 
def heavy(): 
    for i in range(100): 
        light() 
        medium() 
        medium() 
    time.sleep(2) 
 
def runit(n): 
    for i in range(n): 
        heavy()
