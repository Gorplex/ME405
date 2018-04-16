'''@file motor_Thomsen_Thompson_Dunn.py
Created on Tue Apr 10 08:11:51 2018

'''

import pyb
import Globals

class Encoder:
    def __init__(self, timerNumber=4, \
                    pin1=pyb.Pin.board.PB6, \
                    pin2=pyb.Pin.board.PB7):
                        
        self.position = 0
        self.lastCount = 0
               
        encA = pyb.Pin(pin1, pyb.Pin.IN)
        encB = pyb.Pin(pin2, pyb.Pin.IN)        
        
        self.timer = pyb.Timer(timerNumber, prescaler=1, period=0xffff)
        self.__ch1 = self.timer.channel(1, pyb.Timer.ENC_AB, pin=encA)
        self.__ch2 = self.timer.channel(2, pyb.Timer.ENC_AB, pin=encB)       
        
    def read(self):
        tmp = self.timer.counter()
        
        #This line handle wrap around (with modulus) and offsets
        # via the plus  half and minus half 
        self.position += (32768 + tmp - self.lastCount)%65536 - 32768
        self.lastCount = tmp
        return self.position        

    def zero(self):
        self.count = 0
    
def test_all():
    from time import sleep
    print("start test")
    enc = Encoder()
    while True:
        print("Read: "+str(enc.read()))
        sleep(.5)
    