#nonsequitur.py module
#for generation of non sequitur text
#by aaron montoya-moraga
#part of my nyu itp thesis
#and also final project for class
#reading and writing electronic text
#by professor allison parrish
#april 2017
#v0.0.4

# special thanks:
# to allison parrish for pytracery, pycorpora, teaching me python and how to read and write digital text
#to kate compton for tracery
#to dariusk for corpora

#import dependencies
import tracery
import pycorpora
import random
from tracery.modifiers import base_english
import os

# definition of america/russia joke
def america_russia():

    # retrieve verbs from pycorpora
    # needs to be parsed
    verbsAll = pycorpora.words.verbs['verbs']

    # create empty lists in order to parse
    verbsPresent = list()
    verbsPast = list()

    # go through every verb and retrieve just the present tense
    for verb in range(len(verbsAll)):
        verbsPresent.append(verbsAll[verb]['present'])
        verbsPast.append(verbsAll[verb]['past'])

    # pytracery rules
    rules = {
        'origin': 'In America, you #verb# #subject#. In Russia, you #verb# #subject#.',
        'verb': verbsPresent,
        'subject': pycorpora.words.strange_words['words']
    }

    # pytracery grammar
    grammar = tracery.Grammar(rules)
    # use english
    grammar.add_modifiers(base_english)
    # print result
    print grammar.flatten("#origin#")

# definition of bar joke

def bar():

    # retrieve verbs from pycorpora
    # needs to be parsed
    verbsAll = pycorpora.words.verbs['verbs']

    # create empty lists in order to parse
    verbsPresent = list()
    verbsPast = list()

    # go through every verb and retrieve just the present tense
    for verb in range(len(verbsAll)):
        verbsPresent.append(verbsAll[verb]['present'])
        verbsPast.append(verbsAll[verb]['past'])

    #number parsing
    numbersInt = pycorpora.mathematics.primes['primes']
    numbersString = list()

    for number in numbersInt:
        numbersString.append(str(number))

    # pytracery rules
    rules = {
        'origin': '#occupation.a.capitalize# walks into a bar and orders a #beer#. When the bartender gets his drink, #gender# asks, "Bartender, how much do I owe you?" The bartender replies "Just #appliance.a# and some #drug#".',
        'verb': verbsPast,
        'countries': pycorpora.geography.countries['countries'],
        'subject': pycorpora.words.strange_words['words'],
        'occupation': pycorpora.humans.occupations['occupations'],
        'gender': ['he', 'she'],
        'number': numbersString,
        'beer': pycorpora.foods.beer_styles['beer_styles'],
        'new_technology': pycorpora.technology.new_technologies['technologies'],
        'appliance': pycorpora.technology.appliances['appliances'],
        'drug': pycorpora.medicine.drugs['drugs']
    }

    # pytracery grammar
    grammar = tracery.Grammar(rules)
    # use english
    grammar.add_modifiers(base_english)
    # print result
    print grammar.flatten("#origin#")

# definition of why did the chicken cross the road joke.
def chicken():

    # retrieve verbs from pycorpora
    # needs to be parsed
    verbsAll = pycorpora.words.verbs['verbs']

    # create empty lists in order to parse
    verbsPresent = list()
    verbsPast = list()

    # go through every verb and retrieve just the present tense
    for verb in range(len(verbsAll)):
        verbsPresent.append(verbsAll[verb]['present'])
        verbsPast.append(verbsAll[verb]['past'])

    # pytracery rules
    rules = {
        'origin': 'Why did the chicken cross the road? Because #gender# #verb# to #subject# the #subject#.',
        'verb': verbsPast,
        'subject': pycorpora.words.strange_words['words'],
        'gender': ['he', 'she']
    }

    # pytracery grammar
    grammar = tracery.Grammar(rules)
    # use english
    grammar.add_modifiers(base_english)
    # print result
    print grammar.flatten("#origin#")

def cows():

    # retrieve verbs from pycorpora
    # needs to be parsed
    verbsAll = pycorpora.words.verbs['verbs']

    # create empty lists in order to parse
    verbsPresent = list()
    verbsPast = list()


    # go through every verb and retrieve just the present tense
    for verb in range(len(verbsAll)):
        verbsPresent.append(verbsAll[verb]['present'])
        verbsPast.append(verbsAll[verb]['past'])

    # pytracery rules
    rules = {
        'origin': '#countries#: you have two cows, the first one is #subject#, the second one is #subject#.',
        'verb': verbsPast,
        'countries': pycorpora.geography.countries['countries'],
        'subject': pycorpora.words.strange_words['words'],
        'gender': ['he', 'she']
    }

    # pytracery grammar
    grammar = tracery.Grammar(rules)
    # use english
    grammar.add_modifiers(base_english)
    # print result
    print grammar.flatten("#origin#")


def knock_knock():

    # retrieve verbs from pycorpora
    # needs to be parsed
    verbsAll = pycorpora.words.verbs['verbs']

    # create empty lists in order to parse
    verbsPresent = list()
    verbsPast = list()

    # go through every verb and retrieve just the present tense
    for verb in range(len(verbsAll)):
        verbsPresent.append(verbsAll[verb]['present'])
        verbsPast.append(verbsAll[verb]['past'])

    # pytracery rules
    rules = {
        'origin': '#[thingy:#subject#]story#',
        'story': '- Knock knock \n- Who\'s there? \n- #thingy#\n- #thingy.capitalize# who?\n- #thingy.capitalize# #object#',
        'verb': verbsPast,
        'countries': pycorpora.geography.countries['countries'],
        'subject': pycorpora.words.strange_words['words'],
        'gender': ['he', 'she'],
        'object': pycorpora.objects.objects['objects']
    }

    # pytracery grammar
    grammar = tracery.Grammar(rules)
    # use english
    grammar.add_modifiers(base_english)
    # print result
    print grammar.flatten("#origin#")

def lightbulb():

    # retrieve verbs from pycorpora
    # needs to be parsed
    verbsAll = pycorpora.words.verbs['verbs']

    # create empty lists in order to parse
    verbsPresent = list()
    verbsPast = list()

    # go through every verb and retrieve just the present tense
    for verb in range(len(verbsAll)):
        verbsPresent.append(verbsAll[verb]['present'])
        verbsPast.append(verbsAll[verb]['past'])

    #number parsing
    numbersInt = pycorpora.mathematics.primes['primes']
    numbersString = list()

    for number in numbersInt:
        numbersString.append(str(number))

    # pytracery rules
    rules = {
        'origin': '- How many #occupation.s# does it take to change a lightbulb?\n- #number#, because of #new_technology.s#.',
        'verb': verbsPast,
        'countries': pycorpora.geography.countries['countries'],
        'subject': pycorpora.words.strange_words['words'],
        'occupation': pycorpora.humans.occupations['occupations'],
        'gender': ['he', 'she'],
        'number': numbersString,
        'new_technology': pycorpora.technology.new_technologies['technologies']
    }

    # pytracery grammar
    grammar = tracery.Grammar(rules)
    # use english
    grammar.add_modifiers(base_english)
    # print result
    print grammar.flatten("#origin#")

#def of violas joke
def violas():

    # retrieve verbs from pycorpora
    # needs to be parsed
    verbsAll = pycorpora.words.verbs['verbs']

    # create empty lists in order to parse
    verbsPresent = list()
    verbsPast = list()

    # go through every verb and retrieve just the present tense
    for verb in range(len(verbsAll)):
        verbsPresent.append(verbsAll[verb]['present'])
        verbsPast.append(verbsAll[verb]['past'])

    #number parsing
    numbersInt = pycorpora.mathematics.primes['primes']
    numbersString = list()

    for number in numbersInt:
        numbersString.append(str(number))

    # pytracery rules
    rules = {
        'origin': 'What is the difference between violas and #object.s#?\nViolas #verb# #adverb#.',
        'verb': verbsPresent,
        'countries': pycorpora.geography.countries['countries'],
        'subject': pycorpora.words.strange_words['words'],
        'occupation': pycorpora.humans.occupations['occupations'],
        'adverb': pycorpora.words.adverbs['adverbs'],
        'gender': ['he', 'she'],
        'number': numbersString,
        'new_technology': pycorpora.technology.new_technologies['technologies'],
        "object": pycorpora.objects.objects['objects']
    }

    # pytracery grammar
    grammar = tracery.Grammar(rules)
    # use english
    grammar.add_modifiers(base_english)
    # print result
    print grammar.flatten("#origin#")

#TODO
# def print_stuff():
#     os.startfile()
