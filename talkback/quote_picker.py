__author__ = 'ed'
from random import choice

class QuotePicker(object):

    def __init__(self, quotes_filename):
        with open (quotes_filename) as quotes_file:
            self.quotes = quotes_filename.readline()


    def pick(self):
        return choice(self.quotes).strip()

