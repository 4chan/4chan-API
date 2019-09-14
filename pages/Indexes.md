## /[board]/[1-15].json ##
| **Example url** | [`https://a.4cdn.org/po/2.json`](https://a.4cdn.org/po/2.json) | 
|:----------------|:-------------------------------------|
| **Status 200**  | Content-Type: application/json |

`/[board]/[1-15].json` files are a representation of a single index page, which includes each thread on that specific page and the preview replies.

## Thread JSON Structure ##

| **Attribute**   | **Type**       | **Appears**                | **Description** | **Possible values**|
|:----------------|:---------------|:---------------------------|:----------------|:-------------------|
| `no`            | `integer`      | `always` | The numeric post ID | `any positive integer` | 
| `resto`         | `integer`      | `always` | For replies: this is the ID of the thread being replied to. For OP: this value is zero   | `0` or `Any positive integer`|
| `sticky`        | `integer`      | `OP only, if thread is currently stickied` | If the thread is being pinned to the top of the page| `1` or not set|
| `closed`        | `integer`      | `OP only, if thread is currently closed` | If the thread is closed to replies | `1` or not set|
| `now`           | `string`       | `always` | MM/DD/YY(Day)HH:MM (:SS on some boards), EST/EDT timezone | `string` |
| `time`          | `integer`      | `always` | UNIX timestamp the post was created |  `UNIX timestamp` |
| `name`          | `string`       | `always` | Name user posted with. Defaults to `Anonymous` | `any string` |
| `trip`          | `string`       | `if post has tripcode` | The user's tripcode, in format: `!tripcode` or `!!securetripcode`| `any string` |
| `id`            | `string`       | `if post has ID` | The poster's ID | `any 8 characters` |
| `capcode`       | `string`       | `if post has capcode` | The capcode identifier for a post | Not set, `mod`, `admin`, `admin_highlight`, `manager`, `developer`, `founder` |
| `country`       | `string`       | `if country flags are enabled` | Poster's [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | `2 character string` or `XX` if unknown |
| `country_name`  | `string`       | `if country flags are enabled`| Poster's country name | `Name of any country` |
| `sub`           | `string`       | `OP only, if subject was included`| OP Subject text | `any string` |
| `com`           | `string`       | `if comment was included` | Comment (HTML escaped) | `any HTML escaped string` |
| `tim`           | `integer`      | `always if post has attachment` | Unix timestamp + microtime that an image was uploaded | `integer` |
| `filename`      | `string`       | `always if post has attachment` | Filename as it appeared on the poster's device | `any string` |
| `ext`           | `string`       | `always if post has attachment` | Filetype | `.jpg`, `.png`, `.gif`, `.pdf`, `.swf`, `.webm` |
| `fsize`         | `integer`      | `always if post has attachment` | Size of uploaded file in bytes | `any integer` |
| `md5`           | `string`       | `always if post has attachment` | 24 character, packed base64 MD5 hash of file |  |
| `w`             | `integer`      | `always if post has attachment` | Image width dimension | `any integer` |
| `h`             | `integer`      | `always if post has attachment` | Image height dimension | `any integer` |
| `tn_w`          | `integer`      | `always if post has attachment` | Thumbnail image width dimension | `any integer` |
| `tn_h`          | `integer`      | `always if post has attachment` | Thumbnail image height dimension | `any integer` |
| `filedeleted`   | `integer`      | `if post had attachment and attachment is deleted` | If the file was deleted from the post | `1` or not set |
| `spoiler`       | `integer`      | `if post has attachment and attachment is spoilered` | If the image was spoilered or not | `1` or not set |
| `custom_spoiler`| `integer`      | `if post has attachment and attachment is spoilered` | The custom spoiler ID for a spoilered image | `1-10` or not set |
| `omitted_posts` | `integer`      | `OP only` | Number of replies minus the number of previewed replies | `any integer` |
| `omitted_images`| `integer`      | `OP only` | Number of image replies minus the number of previewed image replies | `any integer` |
| `replies`       | `integer`      | `OP only` | Total number of replies to a thread | `any integer` |
| `images`        | `integer`      | `OP only` | Total number of image replies to a thread | `any integer` |
| `bumplimit`     | `integer`      | `OP only, only if bump limit has been reached` | If a thread has reached bumplimit, it will no longer bump | `1` or not set |
| `imagelimit`    | `integer`      | `OP only, only if image limit has been reached` | If an image has reached image limit, no more image replies can be made  | `1` or not set |
| `last_modified` | `integer`      | `OP only` | The UNIX timestamp marking the last time a post was added to or removed from a thread | `UNIX Timestamp` |
| `tag`           | `string`       | `OP only`, `/f/ only` | The category of `.swf` upload |`Game`, `Loop`, etc..|
| `semantic_url`  | `string`       |  `OP only` | SEO URL slug for thread | `string` |
| `since4pass`    | `integer`      | `if poster put 'since4pass' in the options field` | Year 4chan pass bought | `any 4 digit year`|
| `unique_ips`    | `integer`      | `OP only` | Number of unique posters in a thread  | `any integer` | 
| `m_img`         | `integer`      | `any post that has a mobile-optimized image` | Mobile optimized image exists for post | `1` or not set |



## Example file ##

```json
{
	"threads": [{
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
	}, {
		"posts": [{
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
			"omitted_images": 43
		}, {
			"no": 576173,
			"now": "08\/22\/19(Thu)16:58:51",
			"name": "Anonymous",
			"com": "<a href=\"#p576157\" class=\"quotelink\">&gt;&gt;576157<\/a><br>His twitter or Facebook",
			"time": 1566507531,
			"resto": 574933
		}, {
			"no": 576175,
			"now": "08\/22\/19(Thu)17:46:17",
			"name": "Anonymous",
			"com": "this is a comment!",
			"time": 1566510377,
			"resto": 574933
		}, {
			"no": 576176,
			"now": "08\/22\/19(Thu)17:47:46",
			"name": "Anonymous",
			"com": "This is a comment!",
			"time": 1566510466,
			"resto": 574933
		}, {
			"no": 576178,
			"now": "08\/22\/19(Thu)23:25:44",
			"name": "Anonymous",
			"com": "Shape it super",
			"filename": "BBBD43D1-0F83-456C-BB52-C0C1733D601A",
			"ext": ".jpg",
			"w": 750,
			"h": 681,
			"tn_w": 125,
			"tn_h": 113,
			"tim": 1566530744175,
			"time": 1566530744,
			"md5": "Qa8LJta3IgvgtBPCkCwvPw==",
			"fsize": 87848,
			"resto": 574933
		}, {
			"no": 576181,
			"now": "08\/22\/19(Thu)23:29:08",
			"name": "Anonymous",
			"filename": "d15eb1b7d0a20cf4ccc5170278094b36aeaf99f7",
			"ext": ".jpg",
			"w": 544,
			"h": 480,
			"tn_w": 125,
			"tn_h": 110,
			"tim": 1566530948220,
			"time": 1566530948,
			"md5": "3uTK8GkgcnxqJzwOXPV05w==",
			"fsize": 36051,
			"resto": 574933
		}]
	}]
}
```
This example file shows an index page with two threads.
