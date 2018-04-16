'''@file motor_Thomsen_Thompson_Dunn.py
Created on Tue Apr 10 08:27:46 2018
'''

DEBUG_MODE = True

def debug(string):
    if(DEBUG_MODE):
        print(string)

def sign_extend(value, bits):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)
        
