4chan API
=========

## Welcome ##

Welcome to 4chan's poorly documented read-only JSON API guide!

JSON representations of threads are exposed at the following URLs:

http(s)://api.4chan.org/**board**/res/**threadnumber**.json

*Note: We plan to add indexes and other views at a later date in time.*

CORS is supported with an origin of http(s)://boards.4chan.org

Request methods supported are: GET, HEAD, OPTIONS

I will update this guide to suck less at a later point in time. If you'd like to rewrite it, be my guest!

Questions? Please e-mail api@4chan.org.

### Rules ###

* Do not make more than one request per second.
* Use If-Modified-Since when doing your requests.
* More to come later...

### Post Object ####

| **attribute**   | **value**      | **description**      | **possible values**                        | **example value**     |
|:----------------|:---------------|:---------------------|:-------------------------------------------|:----------------------|
| `no`            | `integer`      | Post number          | 1-9999999999999                            | `9001`                |
| `resto`         | `integer`      | Reply to             | 0 (is thread), 1-9999999999999             | `0`                   |
| `sticky`        | `integer`      | Stickied thread?     | 0 (no), 1 (yes)                            | `1`                   |
| `closed`        | `integer`      | Closed thread?       | 0 (no), 1 (yes)                            | `0`                   |
| `now`           | `string`       | Date and time        | MM\/DD\/YY(Day)HH:MM (:SS on some boards)  | `08\/08\/12(Wed)01:11`|
| `time`          | `integer`      | UNIX timestamp       | UNIX timestamp                             | `1344570123`          |
| `name`          | `string`       | Name                 | text *or empty*                            | `moot`                |
| `trip`          | `string`       | Tripcode             | text (format: !tripcode!!securetripcode)   | `!Ep8pui8Vw2`         |
| `id`            | `string`       | ID                   | text (8 characters), Mod, Admin            | `Admin`               |
| `capcode`       | `string`       | Capcode              | none, mod, admin, admin_highlight, developer | `admin`             |
| `country`       | `string`       | Country code         | text (2 characters, ISO 3166-1 alpha-2), XX (unknown) | `XX`       |
| `country_name`  | `string`       | Country name         | text                                       | `Unknown`             |
| `email`         | `string`       | Email                | text *or empty*                            | `moot@4chan.org`      |
| `sub`           | `string`       | Subject              | text *or empty*                            | `This is a subject`   |
| `com`           | `string`       | Comment              | text (includes escaped HTML) *or empty*    | `This is a comment`   |
| `tim`           | `integer`      | Renamed filename     | UNIX timestamp + microseconds              | `1344402680740`       |
| `filename`      | `string`       | Original filename    | text                                       | `OPisa`               |
| `ext`           | `string`       | File extension       | .jpg, .png, .gif, .pdf, .swf               | `.jpg`                |
| `fsize`         | `integer`      | File size            | 1-8388608                                  | `2500`                |
| `md5`           | `string`       | File MD5             | text (24 character, packed base64 MD5 hash)| `NOetrLVnES3jUn1x5ZPVAg==` |
| `w`             | `integer`      | Image width          | 1-10000                                    | `500`                 |
| `h`             | `integer`      | Image height         | 1-10000                                    | `500`                 |
| `tn_w`          | `integer`      | Thumbnail width      | 1-250                                      | `250`                 |
| `tn_h`          | `integer`      | Thumbnail height     | 1-250                                      | `250`                 |
| `filedeleted`   | `integer`      | File deleted?        | 0 (no), 1 (yes)                            | `0`                   |
| `spoiler`       | `integer`      | Spoiler image?       | 0 (no), 1 (yes)                            | `0`                   |

**Note the following attributes are optional:**  
`sticky` `closed` (only display on OPs)  
`id` (only display when board has DISPLAY_ID set)  
`capcode` (only displays when using a capcode)  
`country` `country_name` (only displays when board uses country flags)  
`filename` (only displays when image uploaded)  
`ext` (only displays when image uploaded)  
`fsize` (only displays when image uploaded)  
`md5` (only displays when image uploaded)  
`w` (only displays when image uploaded)  
`h` (only displays when image uploaded)  
`tn_w` (only displays when image uploaded)  
`tn_h` (only displays when image uploaded)  
`filedeleted` (only displays when image uploaded)  
`spoiler` (only displays when image uploaded)  

### Example Thread ###

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
         "md5":"NOetrLVnES3jUn1x5ZPVAg==",
         "fsize":0,
         "resto":9001,
         "filedeleted":0,
         "capcode":"admin",
         "trip":""
      }
   ]
}
</pre>