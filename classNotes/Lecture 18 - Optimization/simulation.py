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
 
def runit(): 
    for i in range(5): 
        heavy()
