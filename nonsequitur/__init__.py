#nonsequitur.py module
#for generation of non sequitur text
#by aaron montoya-moraga
#part of my nyu itp thesis
#and also final project for class
#reading and writing electronic text
#by professor allison parrish
#april 2017
#v0.0.3

#import modules
import os
from os import system
import time
import string
import random
import urllib

#import unicode_literals
from __future__ import unicode_literals

#import spacy module
import spacy

def


#define function for jokes
def joke(waitTime=5):

    #create a new spaCy object, load english language
    nlp = spacy.load('en')

    #create a new document object
    doc = nlp("All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood. Everyone has the right to life, liberty and security of person.")

    doc3 = nlp(open("genesis.txt").read().decode('utf8'))



    #define premise and punchline
    premise = "this is a premise"
    punchline = "this is a punchline"

    #print premise
    print premise
    # wait
    time.sleep(waitTime)
    #print punchline
    print punchline
