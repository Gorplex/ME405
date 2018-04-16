
import pyb
#from time import sleep
import Globals
import Motor_Thomsen_Thompson_Dunn as Motor
import Encoder_Thomsen_Thompson_Dunn as Encoder

#Globals.DEBUG_MODE = False;

def main():
    Globals.DEBUG_MODE = False
    #Motor.test_all()
    #Motor.setdutycycle(20)
    Encoder.test_all()
     

       
if (__name__ == '__main__'):
    main()
    