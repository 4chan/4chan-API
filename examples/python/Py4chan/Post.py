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

class Py4chanPost(object):
    """ A 4chan post
    """
    POSTOBJECTS = {
                 'no':dict(type = int, name = "Number", desc = "Post Number"),
                 'resto':dict(type = int, name = "ReplyTo", desc = "ReplyTo"),
                 'sticky':dict(type = bool, name = "Sticky", desc = "Stickied Thread"),
                 'closed':dict(type = bool, name = "Closed", desc = "Closed Thread"),
                 'now':dict(type = str, name = "DateTime", desc = "Date & Time"),
                 'time':dict(type = int, name = "UnixDateTime", desc = "Date & Time as a Unix Timestamp"),
                 'name':dict(type = str, name = "Name", desc = "Name"),
                 'trip':dict(type = str, name = "Tripcode", desc = "Tripcode"),
                 'id':dict(type = str, name = "UserType", desc = "User Type"),
                 'capcode':dict(type = str, name = "Capcode", desc = ""),
                 'country':dict(type = str, name = "CountryCode", desc = ""),
                 'country_name':dict(type = str, name = "CountryName", desc = ""),
                 'email':dict(type = str, name = "Email", desc = ""),
                 'sub':dict(type = str, name = "Subject", desc = ""),
                 'com':dict(type = str, name = "Comment", desc = "Comment"),
                 'tim':dict(type = int, name = "RenamedFilename", desc = "Renamed Filename"),
                 'filename':dict(type = str, name = "OrgFilename", desc = "Original Filename"),
                 'ext':dict(type = str, name = "FileExtension", desc = ""),
                 'fsize':dict(type = int, name = "FileSize", desc = "Size of the file in bytes"),
                 'md5':dict(type = str, name = "MD5", desc = ""),
                 'w':dict(type = int, name = "ImageWidth", desc = ""),
                 'h':dict(type = int, name = "ImageHeight", desc = ""),
                 'tn_w':dict(type = int, name = "ThumbnailWidth", desc = ""),
                 'tn_h':dict(type = int, name = "ThumbnailHeight", desc = ""),
                 'filedeleted':dict(type = bool, name = "FileDeleted", desc = ""),
                 'spoiler':dict(type = bool, name = "SpoilerImage", desc = ""),
                 'custom_spoiler':dict(type = int, name = "CustomSpoiler", desc = ""),
                 }
    
    def __init__(self, board, postData = None, proto = 'http'):
        self.Board = board
        self.Proto = proto
        self._rawData = postData
        
        for code, info in self.POSTOBJECTS.items():
            if postData.has_key(code):
                log(5, "Found %r. Set %r to %r", code, info['name'], postData[code])
                setattr(self, info['name'], postData[code])
            else:
                log(5, "Didn't find %r", code)
                setattr(self, info['name'], None)
        
        if self.RenamedFilename:
            self.ImageURL = "%s://images.4chan.org/%s/src/%d.%s" % (self.Proto, self.Board, self.RenamedFilename, self.FileExtension)
            self.ThumbImageURL = "%s://1.thumbs.4chan.org/%s/thumb/%d.jpg" % (self.Proto, self.Board, self.RenamedFilename)


