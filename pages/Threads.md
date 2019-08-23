## /[board]/thread/[op ID].json ##
| **Example url** | [`https://a.4cdn.org/po/thread/570368.json`](https://a.4cdn.org/po/thread/570368.json) | 
|:----------------|:-------------------------------------|
| **Status 200**  | Content-Type: application/json |

`/[board]/thread/[op ID].json` files are a representation of a single OP and all the replies, which form a thread.

## Thread JSON Structure ##

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
| `com`           | `string`       | `if comment was included` | | |
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
{
    "posts": [{
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
        "unique_ips": 1
    }, {
        "no": 570370,
        "now": "12\/31\/18(Mon)17:14:56",
        "name": "Anonymous",
        "com": "<b>FAQs about papercraft<\/b><br>\n<br>\n<i>What paper should I use?<\/i><br>\n<br>\nSmall models can be made with light 100 to 150 gsm paper, while large ones are better with heavy 150 to 200+ gsm paper.<br>\n<br>\n<i>Where do I begin with papercraft can I find easy papercrafts?<\/i><br>\n<br>\nPapercraft also requires glue, and cutting tools. A PVA glue stick is works. A pen knife and cutting board is recommended, but otherwise scissors are okay for simple models.<br>\n<br>\nPapercraft normally involves printing and cutting out a number of nets, and and gluing tabs and pieces where appropriate to form a model.<br>\n<br>\nYou can find a variety of papercraft models on this board that may interest you. Ask for some otherwise, and be specific about what you would like. You can search online for \u2018easy papercraft templates\u2019, these links have many.<br>\n<br>\n<a href=\"http:\/\/papercraft.wikidot.com\/papercraft\">http:\/\/papercraft.wikidot.com\/paper<wbr>craft<\/a><br>\n<a href=\"http:\/\/cp.c-ij.com\/en\/categories\/CAT-ST01-0071\/top.html\">http:\/\/cp.c-ij.com\/en\/categories\/CA<wbr>T-ST01-0071\/top.html<\/a><br>\n<br>\n<i>What is Pepakura?<\/i><br>\n<br>\nPepakura Designer is a program that takes 3D models and `unfolds&#039; them to papercraft templates. Using Pepakura in conjunction with a 3D modelling software, such as Blender, you can design your own papercraft models.<br>\n<br>\n<a href=\"https:\/\/elementcrafts.wordpress.com\/2014\/04\/22\/a-complete-beginners-guide-to-papercraft-pepakura-windows-only\/\">https:\/\/elementcrafts.wordpress.com<wbr>\/2014\/04\/22\/a-complete-beginners-gu<wbr>ide-to-papercraft-pepakura-windows-<wbr>only\/<\/a><br>\n<br>\n<i>Hints and tips?<\/i>\n<br>\nGlue accurately for a model to hold well, and practice plenty.<br>\n<br>\n<a href=\"http:\/\/www.papercraftmuseum.com\/advanced-tutorial\/\">http:\/\/www.papercraftmuseum.com\/adv<wbr>anced-tutorial\/<\/a><br>",
        "filename": "papercraft faq",
        "ext": ".png",
        "w": 318,
        "h": 704,
        "tn_w": 56,
        "tn_h": 125,
        "tim": 1546294496751,
        "time": 1546294496,
        "md5": "0EqXBb4gGIyzQiaApMdFAA==",
        "fsize": 285358,
        "resto": 570368,
        "capcode": "mod"
    }, {
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
        "capcode": "mod",
        "xa19l": 2
    }]
}
```
This example file shows a thread with two replies.
