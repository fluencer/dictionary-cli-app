# merriam.py ---
#
# Filename: merriam.py
# Description:
# Author: Vidhyalakshmi Sundara Raman
# Created: Mon Nov  5 01:06:14 2018 (-0500)

# TODO:
# [ ] Lookup for queries with more than a word
# [X] Get usage examples for query
# [ ] Key in separate folder
#

# Test cases: hello, please, love

# Code:

import json
import argparse
import urllib.request
import re

keyfile = open("/Users/vsr/myprojects/pyDumb/dictionary-app/keys.txt", 'r')
keys = keyfile.readline()
parser = argparse.ArgumentParser()
parser.add_argument("word", type=str)
args = parser.parse_args()
query = args.word
urlfrmt = "https://dictionaryapi.com/api/v3/references/collegiate/json/"+query+"?key=" + keys
response = urllib.request.urlopen(urlfrmt)
jsStruct = json.load(response)

for meaning in jsStruct:
    definitions = meaning['shortdef']
    if meaning['meta']['id'] != query:
        print("\n"+meaning['meta']['id'])
    try:
        print('('+meaning['fl']+')')
        for i, eachDef in enumerate(definitions, 1):
            print(str(i) + ". " + eachDef)
    except KeyError:
        pass

print("\nUsage")

for usage in jsStruct:
    try:
        longdefs = usage['def']
        for i, eachDef in enumerate(longdefs, 1):
            if 'sseq' in eachDef:
                # test[*][0][1]['dt'] - gives list of illustrations
                for ill in eachDef['sseq']:
                    if 'dt' in ill[0][1]:
                        for illus in ill[0][1]['dt']:
                            if illus[0] == 'vis':
                                # enumerate
                                for ii in range(1, len(illus)):
                                    L = len(illus[ii])
                                    for jj in range(L):
                                        if 't' in illus[ii][jj]:
                                            # remove everything within braces before printing
                                            print("* "+illus[ii][jj]['t'])
    except KeyError:
        pass
            
            
        
# function to strip formatted strings like {a_link|pleasure} to pleasure
def stripString(query, sentence):
    # if the query is surrounded by brackets
    pass
    
    
# # the first word can be anything
#
# merriam.py ends here
