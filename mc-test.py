#!/usr/bin/env python

from pymarkovchain import MarkovChain
# Create an instance of the markov chain. By default, it uses MarkovChain.py's location to
# store and load its database files to. You probably want to give it another location, like so:
mc = MarkovChain("/home/awp066/markovchain")
# To generate the markov chain's language model, in case it's not present
mc.generateDatabase("It is nice to meet you.  I would like to meet your friend.")
# To let the markov chain generate some text, execute
for i in range(10):
        print(mc.generateString())
