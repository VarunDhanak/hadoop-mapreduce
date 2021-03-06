__author__ = 'alexcomu'
from mrjob.job import MRJob
import re

# Word frequency from book
# File: 04_book.txt

# regular expression used to identify word
WORD_REGEXP = re.compile(r"[\w']+")

class MRWordFrequency(MRJob):

    def mapper(self, _, line):
        # use regex instead simple split
        words = WORD_REGEXP.findall(line)
        for w in words:
            yield w.lower(), 1

    def reducer(self, word, occurrences):
        yield word, sum(occurrences)

