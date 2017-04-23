#nonsequitur.py module
#for generation of non sequitur text
#by aaron montoya-moraga
#part of my nyu itp thesis
#and also final project for class
#reading and writing electronic text
#by professor allison parrish
#april 2017
#v0.0.2

#import modules
import os
from os import system
import time
import string
import random
import urllib

import spacy

#define function for jokes
def joke(waitTime=5):

    #define premise and punchline
    premise = "this is a premise"
    punchline = "this is a punchline"

    #print premise
    print premise
    # wait
    time.sleep(waitTime)
    #print punchline
    print punchline
