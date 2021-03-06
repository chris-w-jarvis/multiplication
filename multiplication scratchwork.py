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


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


############################## Initialize Values ################################
numberlist = dict()
problist = dict()
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
    print a, b
    answer = input(str(a) + " x " + str(b) + " = ")
    if not ( isinstance(answer, int) | isinstance(answer, float) ) :
        prompt(combination)
    time_ = time.time() - start_time
    history.append( ( (a,b), time_, answer==a*b  )  )
    
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
        #print "Time: " + str(time)
        #print "Probability: " + str( problist[str(a) + ", " + str(b) ] )
        print "The right answer is " + str(a*b)
    else :
        problist[ str(a) + ", " + str(b) ] = problist[ str(a) + ", " + str(b) ]/1.5
        normalize()
        print "Correct"
        #print "Time: " + str(time)
        #print "Probability: " + str(problist[str(a) + ", " + str(b) ] )

def summarizeStats():
    clearScreen()
    plt.hist( [x[1] for x in history[place:] ] )
    plt.title('Time Histogram')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency (%)')
    print "Accuracy: " + str( 1.0*sum( [x[2] for x in history[place:] ])/(len(history[place:])) )
    print """Right: {}   Wrong: {} """.format( str( sum( [x[2] for x in history[place:] ])) , 
                                                str(  len(history[place:]) - sum( [x[2] for x in history[place:] ]) )   )   
    print "Average Time: " + str( np.mean( [x[2] for x in history[place:]]   ) )           
    

############################## Driver ################################

##### Ongoing loop ######
def practice():    
    global initialtime, place    
    initialize()
    navigate = ""
    while navigate != "stop":
        clearScreen()

        prompt(selectNumbers()  ) #Finds numbers, 
        initialResponse(place) #updaes probabilities & responds to answer
        
        string = raw_input("continue?")
        if string != "":
            navigate = "stop"
    summarizeStats()
        
        
def timedTest(limit = 30):
    global initialtime, place
    initialize()
    initialTime = time.time()
    place = len(history)
    while  time.time() - initialTime <= limit:
        prompt(selectNumbers()  ) #Finds numbers, 
        initialResponse(place) #updaes probabilities & responds to answer
    summarizeStats()                           #stores statistics

def numberTest(n = 20):
    global initialtime, place
    initialize()
    place = len(history)
    for i in range(n):
        prompt(selectNumbers()  ) #Finds numbers, 
        initialResponse(place) #updaes probabilities & responds to answer
    summarizeStats()                           #stores statistics


#########  
#timedTest()
  
#practice()
  
############################## After Running the App ################################
  
  
  
def recordValues(list, filename, sheetname= None):
    frame = pd.DataFrame(list)
    if sheetname != 0 :
        frame.to_excel(filename, sheetname)
    else:
        frame.to_excel(filename)
    
  
def dropVariables():
    global history, numberlist, place, problist
    del history, numberlist, place, problist



