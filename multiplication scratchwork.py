# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 22:40:37 2016

@author: SuhelSingh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:05:42 2016

@author: SuhelSingh
"""

# -*- coding: utf-8 -*-

######### Multiplication Machine #########
######### Suhel Singh ######################

import pandas as pd
import numpy as np
import time

############################## Initialize Values ################################
numberlist = dict()
problist = dict()
timelist = []
history = [] #triple of (multiplication combo, time, corrent/incorrect )
place = 0 


############################## Define global functions ################################
def initialize(l1 = 10, h1 = 99, l2 = 1, h2 = 10):
    global numberlist, problist
    #create probability and numberlist
    for r in range(l1,h1):
        for c in range(l2,h2):
            numberlist[ str(r) + ", " + str(c) ] = (r,c)
            problist[ str(r) + ", " + str(c) ] = 100.0
    normalize()

def clearScreen():
    print "\n"*45

def normalize():
    global problist    
    s = sum( problist.values() )   
    problist = { p:q/s for p,q in problist.iteritems() }




############################## Penalty algorithm ################################

def selectNumbers():
    ### Randomly choose multiplication combination
    np.random.seed( int( time.time() % 1000 ) )
    i = np.random.choice( len(numberlist.values() ) , 1, p= list(problist.values()))
    a,b = numberlist.values()[i]
    return (a,b)
    
def prompt(combination ):
    global place    
    #### Prompt for answer and recored time
    a,b = combination    
    start_time = time.time()
    answer = input(str(a) + " x " + str(b) + " = ")
    time_ = time.time() - start_time
    history.append( ( (a,b), time_, answer==a*b  )  )
    place =  len(history)-1 
    
    ###### Penalties for getting something wrong
    ##### Penalties for getting something slowly
def initialResponse( index ):  
    global problist, timelist  
    a,b = history[index][0] ## input valules for 1) multiplicaiton numbers 
    time = history[index][1] ## 2) time it took to answers
    correct = history[index][2] ## 3) whether the answer was correct

    if not correct :
        problist[str(a) + ", " + str(b) ] = problist[ str(a) + ", " + str(b) ] + 0.2
        normalize()
        print "Wrong"
        print "Time: " + str(time)
        print "Probability: " + str( problist[str(a) + ", " + str(b) ] )
        print "The right answer is " + str(a*b)
    else :
        problist[ str(a) + ", " + str(b) ] = problist[ str(a) + ", " + str(b) ]/1.5
        normalize()
        print "Correct"
        print "Time: " + str(time)
        print "Probability: " + str(problist[str(a) + ", " + str(b) ] )




############################## Driver ################################

##### Ongoing loop ######
def practice():    
    initialize()
    navigate = ""
    while navigate != "stop":
        clearScreen()

        prompt(selectNumbers()  ) #Finds numbers, 
        initialResponse(place) #updaes probabilities & responds to answer
        
        string = raw_input("continue?")
        if string != "":
            navigate = "stop"
               
def timedTest(limit = 30):
    initialize()
    initialTime = time.time()
    initialIndex = len(timelist)
    while  time.time() - initialTime <= limit:
        prompt(selectNumbers()  ) #Finds numbers, 
        initialResponse(place) #updaes probabilities & responds to answer
                               #stores statistics 
    print timelist[initialIndex:]

#########  
#timedTest()
  
#practice()




