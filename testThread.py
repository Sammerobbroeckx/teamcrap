from threading import Thread
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG=20
ECHO=21
TRIG2=19
ECHO2=26

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.output(TRIG, False)
GPIO.output(TRIG2, False)

USLfound = 1
distance = 0
distance2 = 0
rounding = 2

def calculateUSL():
        global distance
        global rounding
        while USLfound > 0:
                GPIO.output(TRIG, False)
                time.sleep(0.1)
                
                GPIO.output(TRIG, True)
                time.sleep(0.00001)
                GPIO.output(TRIG, False)
                
                while GPIO.input(ECHO) == 0:
                        pulse_start = time.time()
                        
                while GPIO.input(ECHO) == 1:
                        pulse_end = time.time()
                        
                pulse_duration = pulse_end - pulse_start
                
                distance = pulse_duration * 17150
                
                distance = round(distance, rounding)

def calculateUSR():
        global distance2
        global rounding
        while USLfound > 0:
                GPIO.output(TRIG2, False)
                time.sleep(0.1)
                
                GPIO.output(TRIG2, True)               
                time.sleep(0.00001)               
                GPIO.output(TRIG2, False)
                
                while GPIO.input(ECHO2) == 0:
                        pulse_start2 = time.time()
                        
                while GPIO.input(ECHO2) == 1:
                        pulse_end2 = time.time()
                        
                pulse_duration2 = pulse_end2 - pulse_start2
                
                distance2 = pulse_duration2 * 17150
                
                distance2 = round(distance2, rounding)
                
                time.sleep(0.06)

def calculateUsAverage():
        global distance
        global distance2
        while USLfound > 0:
                time.sleep(1)
                print("1: " + str(distance)+"\n")
                print("2: " + str(distance2)+"\n")
                print(str(round(((distance + distance2)/2),rounding))+"\n")
                
def Main():
        t1 = Thread(target=calculateUSL, args=())
        t1.start()
        t3 = Thread(target=calculateUSR, args=())
        t3.start()
        t2 = Thread(target=calculateUsAverage, args=()) 
        t2.start()
        print("Main complete \n")

        
if __name__ == "__main__":
        Main()

#GPIO.cleanup()
