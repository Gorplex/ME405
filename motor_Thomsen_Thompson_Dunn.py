''' @file motor_Thomsen_Thompson_Dunn.py
This class provides a means to drive a motor forward and backwards
using a range from -100 to 100
'''

import pyb

class MotorDriver:
    ''' This is a motor driver class for an Hbridge'''
    
    def __init__ (self, pin1=pyb.Pin.board.PB4, \
                    pin2=pyb.Pin.board.PB5, \
                    enPin = pyb.Pin.board.PA10):
        ''' Creates a motor driver using pin1, pin2, and an enable pin.
            @param pin1 The first pin for controling the motor.
            @param pin2 The second pin for controling the motor.
            @param enPin The pin used to enable the motor driver (always set high)
            motor will always init to stoped
        '''
        print('Creating a motor driver')
        pinIN1a = pyb.Pin (pin1, pyb.Pin.OUT_PP)
        pinIN2a = pyb.Pin (pin2, pyb.Pin.OUT_PP)
        pinENa = pyb.Pin (enPin, pyb.Pin.OUT_PP)
        pinENa.high()
        tim3 = pyb.Timer(3, freq=20000)
        self.__ch1 =tim3.channel(1, pyb.Timer.PWM, pin=pinIN1a)
        self.__ch2 =tim3.channel(2, pyb.Timer.PWM, pin=pinIN2a)
        #to start stoped        
        self.__ch1.pulse_width_percent()
        self.__ch2.pulse_width_percent(0)
    def set_duty_cycle (self,level):
        '''
            This method takes a number from -100 to 100 and sets
            the PWM duty cycle for the motor pins.
        '''
        print('Setting duty cycle to ' + str (level))
        if(level>=0):
            self.__ch1.pulse_width_percent(level)
            self.__ch2.pulse_width_percent(0)
        else:
            self.__ch2.pulse_width_percent(-1*level)
            self.__ch1.pulse_width_percent(0)
            
def test_all():
    '''runs through simple tests '''    
    from time import sleep
    print('start test')
    moe = MotorDriver ()
    sleep(1)
    print('backwards 50')
    moe.set_duty_cycle (-50)
    sleep(1)
    print('backwards 100')
    moe.set_duty_cycle (-100)
    sleep(1)
    print('stop')
    moe.set_duty_cycle (0)
    sleep(1)
    print('forward 50')
    moe.set_duty_cycle (50)
    sleep(1)
    print('forward 100')
    moe.set_duty_cycle (100)
    sleep(1)
    print('stop')
    moe.set_duty_cycle (0)
    sleep(1)
    print('end')  