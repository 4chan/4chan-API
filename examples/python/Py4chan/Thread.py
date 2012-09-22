'''
Created on Sep 9, 2012

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
'''
#===============================================================================
#    This file is part of Py4chan. 
#
#    PyPWSafe is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    PyPWSafe is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PyPWSafe.  If not, see http://www.gnu.org/licenses/old-licenses/gpl-2.0.html 
#===============================================================================

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
            
