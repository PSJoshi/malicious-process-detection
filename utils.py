#!/usr/bin/env python

from jellyfish import levenshtein_distance, damerau_levenshtein_distance, hamming_distance, jaro_distance, jaro_winkler
import sys

def entropy(string):
    '''
    Calculate Shannon entropy of a string.

    string: A string for which to compute the entropy.
    '''
    # get probability of chars in string
    prob = [ string.count(c) / len(string) for c in dict.fromkeys(list(string)) ]
    # calculate the entropy
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])
    return entropy

def entropy_per_byte(string):
    '''
    Calculate Shannon entropy of a string divided by the total bytes
    in the string.  This is done to normalize entropy values between
    strings of different lengths.
    '''
    computed_entropy = entropy(string)
    return computed_entropy / len(string)

def edit_distance(str1, str2, method="damerau-levenshtein"):
    '''
    Calculate edit distance between 'str1' and 'str2' using different
    algorithms.

    Available algorithms:
        * levenshtein
        * damerau-levenshtein (DEFAULT)
        * hamming
        * jaro
        * jaro-winkler
    It is to be noted that 
    Algorithms - "levenshtein", "damerau-levenshtein" and "hamming" return integers
    whereas algorithms "jaro" and "jaro-winkler" return floats 
    range:
    0.0 (completely different) to 1.0 (identical strings).
    '''
    algos = {
        "levenshtein":levenshtein_distance,
        "damerau-levenshtein":damerau_levenshtein_distance,
        "hamming":hamming_distance,
        "jaro":jaro_distance,
        "jaro-winkler":jaro_winkler
    }

    if not method in list(algos.keys()):
        raise ValueError("Unsupported algorithm type: %s" % method)

    if str1 is None or str2 is None or not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("'Method' arguments must be strings.")

    distance_function = algos[method]

    # Jellyfish library distance functions expect unicode, which is the default
    # for Python3.  If we're running in Python2, we need to convert them.
    python_version = sys.version_info
    if python_version.major == 2:
        str1 = unicode(str1)
        str2 = unicode(str2)

    return distance_function(str1, str2)
