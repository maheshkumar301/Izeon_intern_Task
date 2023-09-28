#--------Traffic lights---------
import time
print("-----TRAFFIC LIGHTS------")
def red():
    print("RED")
def yellow():
    print("YELLOW")
def green():
    print("GREEN")

def traffic_Light(n):
    for i in range(n):
        i=0
        while True:
            i+=1
            if i<10:
                red()
                time.sleep(0.3)
            elif i<14:
                yellow()
                time.sleep(0.3)
            elif i<25:
                green()
                time.sleep(0.3)
            elif i>=25:
                break

ipt=int(input("Enter the duration:"))
traffic_Light(ipt)        
    
    
    
    
    
    
            
