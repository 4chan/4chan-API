4chan API
=========

## Welcome ##

Welcome to 4chan's poorly documented read-only JSON API guide!

JSON representations of threads are exposed at the following URLs:

http(s)://api.4chan.org/**board**/res/**threadnumber**.json

CORS is supported with an origin of http(s)://boards.4chan.org

Request methods supported are: GET, HEAD, OPTIONS

I will update this guide to suck less at a later point in time. If you'd like to rewrite it, be my guest!

Questions? Please e-mail api@4chan.org.

### Post Object ###

**no : integer**  
Post number.  
Possible values: 1-9999999999999

**resto : integer**  
Reply to thread?  
Possible values: 0 (not a reply, is OP), 1-99999999999999

**sticky : integer**  
Is a sticky?  
Possible values: 0 (no), 1 (yes)

**closed : integer**  
Is closed?  
Possible values: 0 (no), 1 (yes)

**now : string**  
Date and time of post.  
Possible values: string (date and time in the following format: MM\/DD\/YY(Day)HH:MM:SS)

**time : integer**  
Date and time of post in UNIX format.  
Possible values: integer (UNIX time)

**name : string**  
Name of poster.  
Possible values: string

**trip : string** *or empty*  
Tripcode of poster.  
Possible values: string (format: !tripcode!!securetripcode)

**id : string**  
ID of poster.  
Possible values: string (8 characters)

**capcode : string**  
Capcode of poster.  
Possible values: string (none, mod, admin, admin_highlight, developer)

**country : string**  
Two-letter country code in ISO 3166-1 alpha-2 format.  
Possible values: string (XX for unknown country, otherwise ISO 3166-1 alpha-2 country codes)

**email : string** *or empty*  
E-mail address.  
Possible values: *empty* (no email), string

**sub : string** *or empty*  
Subject of post.  
Possible values: *empty* (no subject), string

**com : string** *or empty*  
Post comment.  
Possible values: *empty* (no comment), string (escaped and includes HTML formatting)

**tim : integer**  
Image renamed file name.  
Possible values: integer (UNIX time + microseconds)

**filename : string** *or empty*  
Image original file name.  
Possible values: *empty* (no image), string

**ext : string** *or empty*  
Image file extension.  
Possible values: *empty* (no image), string (.jpg, .png, .gif, .svg)

**fsize : integer**  
Image file size in bytes.  
Possible values: 0 (no image), 1-8388608

**md5 : string**  
Image MD5.  
Possible values: *empty* (no image), string (32 character/16 byte MD5 hash)

**w : integer**  
Image width.  
Possible values: 0 (no image), 1-10000

**h : integer**  
Image height.  
Possible values: 0 (no image), 1-10000

**tn\_w : integer**  
Thumbnail width.  
Possible values: 0 (no thumbnail), 1-250


**tn\_h : integer**  
Thumbnail height.  
Possible values: 0 (no thumbnail), 1-250

**filedeleted : integer**  
Has the file been deleted?  
Possible values: 0 (no), 1 (yes)


***Note: country, capcode, and id are optional. sticky and closed only display in OPs.***


### Example thread ###


<pre>
{
   "posts":[
      {
         "no":9001,
         "sticky":1,
         "closed":0,
         "now":"08\/08\/12(Wed)01:11",
         "name":"User",
         "email":"",
         "sub":"This is an OP.",
         "com":"This is a great comment!",
         "filename":"",
         "ext":"",
         "w":0,
         "h":0,
         "tn_w":0,
         "tn_h":0,
         "tim":1344402680740,
         "time":1344402680,
         "md5":"",
         "fsize":0,
         "resto":0,
         "filedeleted":0,
         "trip":"!ozOtJW9BFA"
      },
      {
         "no":33576,
         "now":"08\/09\/12(Thu)23:42",
         "name":"moot",
         "email":"",
         "sub":"This is a reply.",
         "com":"OP is a ___.",
         "filename":"opisa",
         "ext":".jpg",
         "w":500,
         "h":500,
         "tn_w":250,
         "tn_h":250,
         "tim":1344570123425,
         "time":1344570123,
         "md5":"554583e1a577d1b32537c87f72557574",
         "fsize":0,
         "resto":9001,
         "filedeleted":0,
         "capcode":"admin",
         "trip":""
      }
   ]
}
</pre>