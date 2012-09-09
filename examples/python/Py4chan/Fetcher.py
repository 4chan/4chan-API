''' Fetch 4chan API data in a 4chan-friendly fashion
Created on Sep 9, 2012

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
'''
# Setup logging
import logging
logger = logging.getLogger("Py4chan." + __name__)
log = logger.log

from urllib import urlopen
import datetime
from json import loads
import time

# Keep track of last request
last = {}

class Fetch4chan(object):
    # Min time between requests, in seconds
    MinRequestTime = datetime.timedelta(seconds = 1)
    
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
    
    def fetchText(self, data = {}, sleep = True):
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
                time.sleep(sleepTime)                                
        else:
            log(5, "First request")
        # Record last request dt
        last[t] = datetime.datetime.now()
        
        try:
            log(5, "Going to open %r", self.URL)
            fHandle = urlopen(self.URL, data, proxies = self.Proxies)
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
    
    def fetchJSON(self, data = {}, sleep = True):
        """ Fetch all JSON from self.URL and return decoded
        data: A key:value mapping of post data to send with the request
        sleep: Sleep if needed to keep above MinRequestTime. Error otherwise. 
        """
        log(5, 'Going to fetch %r as JSON', self.URL)
        text = self.fetchText(data = data, sleep = sleep)
        log(5, 'Decoding JSON from %r...', text[:1000])
        ret = loads(text)
        log(5, 'Decoded %r', ret)
        return ret

    
