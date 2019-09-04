## catalog.json ##
| **Example url** | [`https://a.4cdn.org/boards.json`](https://a.4cdn.org/boards.json) | 
|:----------------|:-------------------------------------|
| **Status 200**  | Content-Type: application/json |

The `catalog.json` file is a comprehensive list of all threads+attributes on a board. Every thread is grouped by `page`. This file is a JSON representation of a board catalog page (example: [https://boards.4channel.org/po/catalog](https://boards.4channel.org/po/catalog).


## Catalog JSON Attributes ##

| **Attribute**   | **Type**       | **Appears**                | **Description** | **Possible values**|
|:----------------|:---------------|:---------------------------|:----------------|:-------------------|
| `no`            | `integer`      | `always` | The numeric post ID | `any positive integer` | 
| `resto`         | `integer`      | `always` | For replies: this is the ID of the thread being replied to. For OP: this value is zero   | `0` or `Any positive integer`|
| `sticky`        | `integer`      | `OP only` | If the thread is being pinned to the top of the page| `1` or not set|
| `closed`        | `integer`      | `only in OP, if thread is closed` | If the thread is closed to replies | `1` or not set|
| `now`           | `string`       | `always` | String date and time, EST timezone | `string` |
| `time`          | `integer`      | `always` | UNIX timestamp the post was created |  `UNIX timestamp` |
| `name`          | `string`       | `always` | Name user posted with. Defaults to `Anonymous` | `any string` |
| `trip`          | `string`       | `if post has tripcode` |  | |
| `id`            | `string`       | `if post has ID` | | |
| `capcode`       | `string`       | `if post has capcode` | | |
| `country`       | `string`       | `if country flags are enabled` | | |
| `country_name`  | `string`       | `if country flags are enabled`| | |
| `sub`           | `string`       | `OP only`| | |
| `com`           | `string`       | `always` | | |
| `tim`           | `integer`      | `if post has attachment` |  | |
| `filename`      | `string`       | `if post has attachment` | | |
| `ext`           | `string`       | `if post has attachment` | | |
| `fsize`         | `integer`      | `if post has attachment` | | |
| `md5`           | `string`       | `if post has attachment` | | |
| `w`             | `integer`      | `if post has attachment` |  | |
| `h`             | `integer`      | `if post has attachment` |  | |
| `tn_w`          | `integer`      | `if post has attachment` |  | |
| `tn_h`          | `integer`      | `if post has attachment` |  | |
| `filedeleted`   | `integer`      | `if post has attachment and attachment is deleted` | | |
| `spoiler`       | `integer`      | `if post has attachment and attachment is spoilered` |  | |
| `custom_spoiler`| `integer`      | `if post has attachment and attachment is spoilered` |  | |
| `omitted_posts` | `integer`      | `OP only` |  | |
| `omitted_images`| `integer`      | `OP only` |  | |
| `replies`       | `integer`      | `OP only` | | |
| `images`        | `integer`      | `OP only` | | |
| `bumplimit`     | `integer`      | `OP only` |  | |
| `imagelimit`    | `integer`      | `OP only` |  | |
| `last_modified` | `integer`      | `OP only` |  | |
| `tag`           | `string`       | `OP only`, `/f/ only` |  | |
| `semantic_url`  | `string`       |  `OP only` |  | |
| `since4pass`    | `integer`      | `conditionally` |  | |


## Example file ##

```json
[{
    "page": 1,
    "threads": [{
        "no": 570368,
        "sticky": 1,
        "closed": 1,
        "now": "12\/31\/18(Mon)17:05:48",
        "name": "Anonymous",
        "sub": "Welcome to \/po\/!",
        "com": "Welcome to \/po\/! We specialize in origami, papercraft, and everything that\u2019s relevant to paper engineering. This board is also an great library of relevant PDF books and instructions, one of the best resource of its kind on the internet.<br><br>Questions and discussions of papercraft and origami are welcome. Threads for topics covered by paper engineering in general are also welcome, such as kirigami, bookbinding, printing technology, sticker making, gift boxes, greeting cards, and more.<br><br>Requesting is permitted, even encouraged if it\u2019s a good request; fulfilled requests strengthens this board\u2019s role as a repository of books and instructions. However do try to keep requests in relevant threads, if you can.<br><br>\/po\/ is a slow board! Do not needlessly bump threads.",
        "filename": "yotsuba_folding",
        "ext": ".png",
        "w": 530,
        "h": 449,
        "tn_w": 250,
        "tn_h": 211,
        "tim": 1546293948883,
        "time": 1546293948,
        "md5": "uZUeZeB14FVR+Mc2ScHvVA==",
        "fsize": 516657,
        "resto": 0,
        "capcode": "mod",
        "semantic_url": "welcome-to-po",
        "replies": 2,
        "images": 2,
        "omitted_posts": 1,
        "omitted_images": 1,
        "last_replies": [{
            "no": 570371,
            "now": "12\/31\/18(Mon)17:21:29",
            "name": "Anonymous",
            "com": "<b>FAQs about origami<\/b><br>\n<br>\n<i>Where do I begin with origami and how can I find easy models?<\/i><br>\n<br>\nTry browsing the board for guides, or other online resources listed below, for models you like and practice folding them.<br>\n<br>\nA great way to begin at origami is to participate in the Let\u2019s Fold Together threads <a href=\"https:\/\/boards.4channel.org\/po\/catalog#s=lft\"><a href=\"\/\/boards.4channel.org\/po\/catalog#s=lft\" class=\"quotelink\">&gt;&gt;&gt;\/po\/lft<\/a><\/a> - open up the PDF file and find a model you like, work on it, and discuss or post results.<br>\n<br>\n<a href=\"http:\/\/en.origami-club.com\">http:\/\/en.origami-club.com<\/a><br>\n<a href=\"https:\/\/origami.me\/diagrams\/\">https:\/\/origami.me\/diagrams\/<\/a><br>\n<a href=\"https:\/\/www.origami-resource-center.com\/free-origami-instructions.html\">https:\/\/www.origami-resource-center<wbr>.com\/free-origami-instructions.html<wbr><\/a><br>\n<a href=\"http:\/\/www.paperfolding.com\/diagrams\/\">http:\/\/www.paperfolding.com\/diagram<wbr>s\/<\/a><br>\n<br>\n<i>What paper should I use?<\/i><br>\n<br>\nIt depends on the model; for smaller models which involved 25 steps or fewer, 15 by 15 cm origami paper from a local craft store will be suitable. For larger models you will need larger or thinner paper, possibly from online shops. Boxpleated models require thin paper, such as sketching paper. Wet folded models require thicker paper, such as elephant hide.<br>\n<br>\n<a href=\"https:\/\/www.origami-shop.com\/en\/\">https:\/\/www.origami-shop.com\/en\/<\/a><br>\n<br>\n<i>Hints and tips?<\/i><br>\n<br>\nFor folding, The best advice is to always fold as cleanly as possible, and take your time. Everything else comes with experience.<br>\n<br>\n<a href=\"https:\/\/origami.me\/beginners-guide\/\">https:\/\/origami.me\/beginners-guide\/<wbr><\/a><br>\n<a href=\"https:\/\/origamiusa.org\/glossary\">https:\/\/origamiusa.org\/glossary<\/a><br>\n<br>\n<i>What are \u2018CPs\u2019?<\/i><br>\n<br>\nCrease patterns are a structural representations of origami models, shown as a schematic of lines; they are essentially origami models unfolded and laid flat. Lines on a crease pattern may be indicated by \u2018mountain\u2019 or \u2018valley\u2019 folds to show how the folds alternate. If you\u2019re particularly skilled at origami, they become useful instructions for building models. A common base fold is usually discernable, all the intermediate details can be worked on from there.<br>\n<br>\n<a href=\"https:\/\/blog.giladnaor.com\/2008\/08\/folding-from-crease-patterns.html\">https:\/\/blog.giladnaor.com\/2008\/08\/<wbr>folding-from-crease-patterns.html<\/a><br>\n<a href=\"http:\/\/www.origamiaustria.at\/articles.php?lang=2#a4\">http:\/\/www.origamiaustria.at\/articl<wbr>es.php?lang=2#a4<\/a><br>",
            "filename": "origami faq",
            "ext": ".jpg",
            "w": 762,
            "h": 762,
            "tn_w": 125,
            "tn_h": 125,
            "tim": 1546294889019,
            "time": 1546294889,
            "md5": "vKWr7+oITdUBu7bUaypuCw==",
            "fsize": 163110,
            "resto": 570368,
            "capcode": "mod"
        }],
        "last_modified": 1546294897
    }, {
        "no": 574933,
        "now": "06\/28\/19(Fri)21:24:42",
        "name": "New Thread on Origami July 2019",
        "com": "Let&#039;s start a new thread since the previous one has been archived",
        "filename": "main-qimg-05ffefcf21e1c8a3f6d7b50b999d0c99-c",
        "ext": ".jpg",
        "w": 500,
        "h": 378,
        "tn_w": 250,
        "tn_h": 189,
        "tim": 1561771482133,
        "time": 1561771482,
        "md5": "sRkYWy2xOCTQ1H\/sHYjFYw==",
        "fsize": 84219,
        "resto": 0,
        "bumplimit": 0,
        "imagelimit": 0,
        "semantic_url": "lets-start-a-new-thread-since-the-previous-one",
        "replies": 228,
        "images": 44,
        "omitted_posts": 223,
        "omitted_images": 43,
        "last_replies": [{
            "no": 576173,
            "now": "08\/22\/19(Thu)16:58:51",
            "name": "Anonymous",
            "com": "Comment",
            "time": 1566507531,
            "resto": 574933
        }, {
            "no": 576175,
            "now": "08\/22\/19(Thu)17:46:17",
            "name": "Anonymous",
            "com": "This is a comment!",
            "time": 1566510377,
            "resto": 574933
        }, {
            "no": 576176,
            "now": "08\/22\/19(Thu)17:47:46",
            "name": "Anonymous",
            "com": "This is a comment!",
            "time": 1566510466,
            "resto": 574933
        }],
        "last_modified": 1566530948
    }]
}, {
    "page": 2,
    "threads": [{
        "no": 568362,
        "now": "10\/05\/18(Fri)13:53:57",
        "name": "Anonymous",
        "com": "This is a comment!",
        "filename": "IMG_20181005_181107-1",
        "ext": ".jpg",
        "w": 373,
        "h": 654,
        "tn_w": 142,
        "tn_h": 250,
        "tim": 1538762037790,
        "time": 1538762037,
        "md5": "HTvheK4HTgbXKRqMQ0vrXA==",
        "fsize": 48770,
        "resto": 0,
        "bumplimit": 0,
        "imagelimit": 0,
        "semantic_url": "my-girlfriends-birthday-and-id-like-to-make-her",
        "replies": 55,
        "images": 7,
        "omitted_posts": 50,
        "omitted_images": 7,
        "last_replies": [{
            "no": 570857,
            "now": "01\/20\/19(Sun)19:18:28",
            "name": "Anonymous",
            "com": "This is a comment!",
            "time": 1548029908,
            "resto": 568362
        }, {
            "no": 570858,
            "now": "01\/20\/19(Sun)19:20:08",
            "name": "Anonymous",
            "com": "https:\/\/youtu.be\/K6BdXq4JDNw",
            "time": 1548030008,
            "resto": 568362
        }, {
            "no": 575363,
            "now": "07\/17\/19(Wed)19:44:45",
            "name": "Anonymous",
            "com": "did u do it?",
            "time": 1563407085,
            "resto": 568362
        }, {
            "no": 575523,
            "now": "07\/28\/19(Sun)08:42:18",
            "name": "Anonymous",
            "com": "This is a comment!",
            "time": 1564317738,
            "resto": 568362
        }, {
            "no": 576085,
            "now": "08\/21\/19(Wed)02:06:59",
            "name": "Anonymous",
            "com": "<a href=\"#p569203\" class=\"quotelink\">&gt;&gt;569203<\/a><br><span class=\"quote\">&gt;&gt;&gt;\/r*ddit\/<\/span>",
            "time": 1566367619,
            "resto": 568362
        }],
        "last_modified": 1566367619
    }, {
        "no": 568442,
        "now": "10\/09\/18(Tue)12:32:32",
        "name": "Anonymous",
        "sub": "Byakuren",
        "com": "This is a comment!",
        "filename": "thumbnail",
        "ext": ".jpg",
        "w": 2550,
        "h": 3509,
        "tn_w": 181,
        "tn_h": 250,
        "tim": 1539102752203,
        "time": 1539102752,
        "md5": "DL0flLfVrgNUNfRX3Lr7sA==",
        "fsize": 1932484,
        "resto": 0,
        "bumplimit": 0,
        "imagelimit": 0,
        "semantic_url": "byakuren",
        "replies": 18,
        "images": 11,
        "omitted_posts": 13,
        "omitted_images": 9,
        "last_replies": [{
            "no": 573591,
            "now": "05\/10\/19(Fri)23:39:05",
            "name": "Anonymous",
            "com": "<a href=\"#p571769\" class=\"quotelink\">&gt;&gt;571769<\/a><br>cute tenko",
            "time": 1557545945,
            "resto": 568442
        }, {
            "no": 574333,
            "now": "06\/17\/19(Mon)02:17:09",
            "name": "Anonymous",
            "com": "<a href=\"#p571480\" class=\"quotelink\">&gt;&gt;571480<\/a><br>cute slacker",
            "time": 1560752229,
            "resto": 568442
        }, {
            "no": 574536,
            "now": "06\/24\/19(Mon)20:49:36",
            "name": "Anonymous",
            "com": "<a href=\"#p570596\" class=\"quotelink\">&gt;&gt;570596<\/a><br>Im gonna have a go at copying and pasting that plant several times as to make the base a sunflower field.",
            "filename": "char wicked",
            "ext": ".jpg",
            "w": 1200,
            "h": 650,
            "tn_w": 125,
            "tn_h": 67,
            "tim": 1561423776791,
            "time": 1561423776,
            "md5": "yIsO5lWpK+6WAn4nq8Ud4w==",
            "fsize": 99836,
            "resto": 568442
        }, {
            "no": 575440,
            "now": "07\/22\/19(Mon)01:39:16",
            "name": "Anonymous",
            "com": "bestest girl passing by!!!",
            "filename": "__hinanawi_tenshi_touhou_drawn_by_hammer_sunset_beach__sample-8a8977c8a78cc7622e07f8085d14042e",
            "ext": ".jpg",
            "w": 850,
            "h": 600,
            "tn_w": 125,
            "tn_h": 88,
            "tim": 1563773956035,
            "time": 1563773956,
            "md5": "vIuWRL\/RVF1TNy0xYSD7Yg==",
            "fsize": 248745,
            "resto": 568442
        }, {
            "no": 576084,
            "now": "08\/21\/19(Wed)02:04:33",
            "name": "Anonymous",
            "com": "This is a comment!",
            "time": 1566367473,
            "resto": 568442
        }],
        "last_modified": 1566367473
    }]
}]
```
