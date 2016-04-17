# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:05:42 2016

@author: SuhelSingh
"""

# -*- coding: utf-8 -*-

######### Multiplication Machine #########
######### Suhel Singh ######################

import numpy as np
import time

############################## Initialize Values ################################
l1 = 10
h1 = 99
l2 = 1
h2 = 10

numberlist = dict()
problist = dict()
timelist = []

for r in range(l1,h1):
    for c in range(l2,h2):
        numberlist[ str(r) + ", " + str(c) ] = (r,c)
        problist[ str(r) + ", " + str(c) ] = 100.0


def clearScreen():
    print "\n"*45

def normalize():
    global problist    
    s = sum( problist.values() )   
    problist = { p:q/s for p,q in problist.iteritems() }

normalize()

############################## Start Loop ################################

def printValues():
    global problist, timelist
    np.random.seed( int( time.time() % 100 ) )
    i = np.random.choice( len(numberlist.values() ) , 1, p= list(problist.values()))
    a,b = numberlist.values()[i]
    
    start_time = time.time()
    answer = input(str(a) + " x " + str(b) + " = ")
    timelist.append( time.time() - start_time  )
    
    ##### Penalties for getting something slowly
    
    
    
    
    
    
    ###### Penalties for getting something wrong
    if answer != a*b :
        problist[ str(a) + ", " + str(b) ] = problist[ str(a) + ", " + str(b) ] + 0.2
        normalize()
        print problist[str(a) + ", " + str(b) ]
    else :
        problist[ str(a) + ", " + str(b) ] = problist[ str(a) + ", " + str(b) ]/1.5
        normalize()
        print a*b
        print problist[str(a) + ", " + str(b) ]



navigate = ""
while navigate != "stop":
    clearScreen()
    printValues()
    string = raw_input("continue?")
    if string != "":
        navigate = "stop"




