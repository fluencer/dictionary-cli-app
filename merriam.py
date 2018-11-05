# merriam.py ---
#
# Filename: merriam.py
# Description:
# Author: Vidhyalakshmi Sundara Raman
# Created: Mon Nov  5 01:06:14 2018 (-0500)
# Version:
# Packages-Required: ()
# Last-Updated:
#           By:
#     Update #: 0
# Keywords:
# Compatibility:
#
#

# TODO:
# [ ] Lookup for queries with more than a word
# [ ] Get usage examples for query
# [ ] Key in separate folder
#

# Change Log:
#
#
#

# Code:

import json
import sys
import argparse
import urllib.request

keyfile = open("keys.txt", 'r')
keys = keyfile.readline()
parser = argparse.ArgumentParser()
# query = input("Lookup word:")
parser.add_argument("word", type=str)
args = parser.parse_args()
query = args.word
urlfrmt = "https://dictionaryapi.com/api/v3/references/collegiate/json/"+query+"?key=" + keys
response = urllib.request.urlopen(urlfrmt)
jsStruct = json.load(response)

for meaning in jsStruct:
    definitions = meaning['shortdef']
    try:
        print('('+meaning['fl']+')')
        for i, eachDef in enumerate(definitions, 1):
            print(str(i) + ". " + eachDef)
    except KeyError:
        pass

#
# merriam.py ends here
