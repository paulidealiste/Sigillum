import re
import random


def letter_reader(textline):
    '''Return set of unique Latin-2 characters from a line of text.'''
    p1 = "[\u0041-\u007a]+|"
    p2 = "\u0161+|[\u015A-\u0179]+|"
    p3 = "[\u015b-\u017a]+|[\u0105-\u0163]+"
    pattern = re.compile(p1 + p2 + p3)
    return set("".join(re.findall(pattern, textline)).replace(" ", "").lower())


def ruleset_reader(textchunk):
    '''Return ruleset dict depicting mapping of letters to polygons.'''
    rule_list = textchunk.strip().splitlines()
    return dict(map(lambda x: x.split(":"), rule_list))


def rarefy(letterlist, quant):
    '''Randomly rarefy list of letters to quant length.'''
    while len(letterlist) > quant:
        del letterlist[random.randrange(len(letterlist))]
    return letterlist
