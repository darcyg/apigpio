#!/usr/bin/python
# This file provides an interface for GPIO pins

def init_pin(pin):
    
    try:
        f= open ('/sys/class/gpio/unexport','w')
        f.write(str(pin))
        f.close()
    except:
        print "Error"
    
    f= open ('/sys/class/gpio/export','w')
    f.write(str(pin))
    f.close()
    
    path = '/sys/class/gpio/gpio' + str(pin) + '/direction'
    f= open (path,'w')
    f.write('out')
    f.close()


def on_pin(pin):
    path = '/sys/class/gpio/gpio' + str(pin) + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    
def off_pin(pin):
    path = '/sys/class/gpio/gpio' + str(pin) + '/value'
    f= open (path,'w')
    f.write('0')
    f.close()
    

def deinit_pin(pin):
    try:
        f= open ('/sys/class/gpio/unexport','w')
        f.write(str(pin))
        f.close()
    except:
        print "Error"


def get_pin(pin):
    '''
    Function to return current value of pin. Pin must be previously inititalized.
    Returns True if 1, False if 0.
    '''
    path = '/sys/class/gpio/gpio' + str(pin) + '/value'
    f= open (path,'w')
    value = f.read()
    f.close()
    if value == '1': return True
    elif value == '0': return False
