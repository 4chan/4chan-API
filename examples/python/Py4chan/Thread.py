'''
Created on Sep 9, 2012

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
'''
# Setup logging
import logging
logger = logging.getLogger("Py4chan." + __name__)
log = logger.log

from Fetcher import Fetch4chan
from Post import Py4chanPost

class Py4chanThread(Fetch4chan):
    """ Represent a thread from a 4chan board
    
    """    
    def __init__(self, boardID, threadID, proto = 'http', **kw):
        self.Proto = proto
        self.Board = boardID
        self.Thread = threadID
        
        log(10, "Creating %r - board:%r thread:%r", self, boardID, threadID)
        self.URL = '%s://api.4chan.org/%s/res/%d.json' % (self.Proto, self.Board, self.Thread)
        
        Fetch4chan.__init__(self, **kw)
        
        self.update()
        
    def update(self, sleep = True):
        self.Posts = []
        
        json = self.fetchJSON(sleep = sleep)
        for postData in json['posts']:
            self.Posts.append(Py4chanPost(board = self.Board, postData = postData, proto = self.Proto)) 
            
