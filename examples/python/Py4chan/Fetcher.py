''' Fetch 4chan API data in a 4chan-friendly fashion
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

from urllib import urlopen
import datetime
from json import loads
import time

from Errors import NoDataReturnedError

# Keep track of last request
last = {}

class Fetch4chan(object):
    # Min time between requests, in seconds
    MinRequestTime = datetime.timedelta(seconds = 1)
    URL = None
    def __init__(self, proxies = {}, url = None):
        """
        proxies=dict(http="http://www.someproxy.com:3128")
        url='http(s)://api.4chan.org/board/res/threadnumber.json'       
        """
        if self.URL and url:
            log(10, "Overwriting %r with %r" % (self.URL, url))
        if url:
            self.URL = url
        if not self.URL:
            log(40, "No URL defined")
            raise ValueError, "No URL defined"
        self.Proxies = proxies
    
    def fetchText(self, data = '', sleep = True):
        """ Fetch all data from self.URL
        data: A key:value mapping of post data to send with the request
        sleep: Sleep if needed to keep above MinRequestTime. Error otherwise. 
        """
        t = type(self).__name__
        if last.has_key(t):
            log(5, "Last request: %r", last[t])
            delta = datetime.datetime.now() - last[t]
            if delta < datetime.timedelta.min:
                log(10, "Time seems to have gone backwards: %r", delta)
            elif delta < self.MinRequestTime:
                # Time is going forward & we're requesting too quickly
                sleepTime = self.MinRequestTime - delta
                log(10, "Going to quickly, sleeping for %r", sleepTime)
                time.sleep(float(sleepTime.seconds))                                
        else:
            log(5, "First request")
        # Record last request dt
        last[t] = datetime.datetime.now()
        
        try:
            log(5, "Going to open %r", self.URL)
            if data == '':
                data = None
            fHandle = urlopen(url = self.URL, data = data, proxies = self.Proxies)
            log(10, "Successfully opened url: %r", fHandle)
        except Exception, e:
            log(40, "Failed to open %r with %r", self.URL, e)
            raise e
        try:
            log(5, "Starting to read data")
            text = fHandle.read()
            log(10, "Read %d bytes", len(text))
            return text
        finally:
            fHandle.close()
    
    def fetchJSON(self, data = '', sleep = True):
        """ Fetch all JSON from self.URL and return decoded
        data: A key:value mapping of post data to send with the request
        sleep: Sleep if needed to keep above MinRequestTime. Error otherwise. 
        """
        log(10, 'Going to fetch %r as JSON', self.URL)
        text = self.fetchText(data = data, sleep = sleep)
        if len(text) == 0:
            raise NoDataReturnedError, "A zero byte file was returned"
        i = 1
        while i * 50 < len(text):
            log(5, 'Fetched data (line %05d): %r' % (i, text[(i - 1) * 50:i * 50]))
            i += 1
        log(10, "Translating JSON into objects")            
        ret = loads(text)
        log(5, 'Decoded %r', ret)
        return ret

    
