__author__ = 'ed'
from ConfigParser import ConfigParser

from twisted.application.service import IServiceMaker, Service
from twisted.internet.endpoints import clientFromString
from twisted.plugin import IPlugin
from twisted.python import usage, log
from zope.interface import implementer


class Options(usage.Options):
    pass

class TalkBackBotService(Service):

    def __init__(self, endpoint, channel, nickname, realname, quotesFilename, triggers):
        pass

    def startService(self):
        """Construct a client and connect to server"""
        pass

    def stopService(self):
        """Disconnect"""
        pass

