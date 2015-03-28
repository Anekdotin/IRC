__author__ = 'ed'
from twisted.test import proto_helpers
from twisted.trial import unittest

from talkback.bot import TalkBackBotFactory

QUOTE = "Nobody minds having what is too good for them. ~ Jane Austen"

class FakePicker(object):
    """
    Always return the same quote.
    """
    def __init__(self, quote):
        self._quote = quote

    def pick(self):
        return self._quote
