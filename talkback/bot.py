__author__ = 'ed'
from twisted.internet import protocol
from twisted.python import logging
from twisted.words.protocols import irc

class TalkBackBotFactory(protocol.ClientFactory):

    def __init__(self, settings):
        pass