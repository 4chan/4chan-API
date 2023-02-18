## boards.json ##
| **Example url** | [`https://a.4cdn.org/boards.json`](https://a.4cdn.org/boards.json) | 
|:----------------|:-------------------------------------|
| **Status 200**  | Content-Type: application/json |

The `boards.json` file is a comprehensive list of all boards and their major settings.


## Boards.json Attributes ##

| **Attribute**   | **Type**       | **Appears**                | **Description** | **Possible values**|
|:----------------|:---------------|:---------------------------|:----------------|:-------------------|
| `board`         | `string`       | `always` | The directory the board is located in. | `Any string`
| `title`         | `string`      | `always` | The readable title at the top of the board. | `Any string`|
| `ws_board`      | `integer`      | `always` | Is the board [worksafe](https://4chan.org/faq#worksafe) | `1` or `0` |
| `per_page`      | `integer`      | `always` | How many threads are on a single index page | `Any positive integer` |
| `pages`         | `integer`      | `always` | How many index pages does the board have | `Any positive integer` |
| `max_filesize`  | `integer`      | `always` | Maximum file size allowed for non `.webm` attachments (in KB) | `Any positive integer` |
| `max_webm_filesize`  | `integer` | `always` | Maximum file size allowed for `.webm` attachments (in KB) | `Any positive integer` |
| `max_comment_chars`  | `integer` | `always` | Maximum number of characters allowed in a post comment | `Any positive integer` |
| `max_webm_duration`  | `integer` | `always` | Maximum duration of a `.webm` attachment (in seconds) | `Any positive integer` |
| `bump_limit`    | `integer`      | `always` | Maximum number of replies allowed to a thread before the thread stops [bumping](https://4chan.org/faq#bump) | `Any positive integer`|
| `image_limit`   | `integer`      | `always` | Maximum number of image replies per thread before image replies are discarded | `Any positive integer` |
| `cooldowns`     | `array`        | `always` |  | |
| `meta_description`   | `string` | `always` | SEO [meta description content](https://moz.com/learn/seo/meta-description) for a board | `Any string`|
| `spoilers`      | `integer`      | `only if enabled` | Are [spoilers](https://4chan.org/faq#spoiler) enabled | `1` or `0` |
| `custom_spoilers`    | `integer` | `only if enabled` | How many custom spoilers does the board have | `Any positive integer` |
| `is_archived`   | `integer`      | `only if enabled` | Are [archives](https://4chan.org/faq#archive) enabled for the board | `1` or `0` |
| `board_flags`   | `array`      | `only if enabled` | Array of flag codes mapped to flag names | |
| `country_flags` | `integer`      | `only if enabled` | Are flags showing the poster's country enabled on the board | `1` or `0`|
| `user_ids`      | `integer`      | `only if enabled` | Are poster ID tags enabled on the board | `1` or `0`|
| `oekaki`        | `integer`      | `only if enabled` | Can users submit drawings via browser the Oekaki app | `1` or `0` |
| `sjis_tags`     | `integer`      | `only if enabled` | Can users submit [sjis](https://en.wikipedia.org/wiki/Shift_JIS) drawings using the `[sjis]` tags  | `1` or `0` |
| `code_tags`     | `integer`      | `only if enabled` | Board supports code syntax highlighting using the `[code]` tags  | `1` or `0` |
| `math_tags`     | `integer`      | `only if enabled` | Board supports `[math]` [TeX](https://en.wikipedia.org/wiki/TeX) and `[eqn]` tags | `1` or `0` |
| `text_only`     | `integer`      | `only if enabled` | Is image posting disabled for the board | `1` or `0`|
| `forced_anon`   | `integer`      | `only if enabled` | Is the name field disabled on the board | `1` or `0`|
| `webm_audio`    | `integer`      | `only if enabled` | Are webms with audio allowed? | `1` or `0`|
| `require_subject`    | `integer` | `only if enabled` | Do OPs require a subject | `1` or `0` |
| `min_image_width`    | `integer` | `only if enabled` | What is the minimum image width (in pixels) | `Any positive integer`|
| `min_image_height`   | `integer` | `only if enabled` | What is the minimum image height (in pixels) | `Any positive integer`|

* integer 1 = (on) or 0 (off)

## Example file ##

```json
{
	"boards": [{
		"board": "a",
		"title": "Anime \u0026 Manga",
		"ws_board": 1,
		"per_page": 15,
		"pages": 10,
		"max_filesize": 4194304,
		"max_webm_filesize": 3145728,
		"max_comment_chars": 2000,
		"max_webm_duration": 120,
		"bump_limit": 500,
		"image_limit": 300,
		"cooldowns": {
			"threads": 600,
			"replies": 60,
			"images": 60
		},
		"meta_description": "\u0026quot;\/a\/ - Anime \u0026amp; Manga\u0026quot; is 4chan's imageboard dedicated to the discussion of Japanese animation and manga.",
		"spoilers": 1,
		"custom_spoilers": 1,
		"is_archived": 1
	}, {
		"board": "b",
		"title": "Random",
		"ws_board": 0,
		"per_page": 15,
		"pages": 10,
		"max_filesize": 2097152,
		"max_webm_filesize": 2097152,
		"max_comment_chars": 2000,
		"max_webm_duration": 120,
		"bump_limit": 300,
		"image_limit": 150,
		"cooldowns": {
			"threads": 60,
			"replies": 15,
			"images": 15
		},
		"meta_description": "\u0026quot;\/b\/ - Random\u0026quot; is the birthplace of Anonymous, and where people go to discuss random topics and create memes on 4chan.",
		"forced_anon": 1,
		"board_flags": {
			"AB": "Flag Name AB",
			"XY": "Flag Name XY"
		}
	}],
}

```
