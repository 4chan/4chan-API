## Endpoints and Domains ##

## Domains

| **Domain**   | **Protocols**      | **Serves**                    | **Description**      |
|:-------------|:-------------------|:----------------------------|:---------------------|
| `a.4cdn.org` | `https`, `http`    | `4chan.org`, `4channel.org` | This domain serves all 4chan API endpoints in the form of static json files. |
| `i.4cdn.org` | `https`, `http`    | `4chan.org`, `4channel.org` | This is the primary content domain used for serving user submitted media attached to posts. |
| `is2.4cdn.org` | `https`, `http`  | `4chan.org`, `4channel.org` | Acts as the secondary content domain used for serving user submitted media attached to posts. |
| `s.4cdn.org` | `https`, `http`    | `4chan.org`, `4channel.org` | Serves all static site content including icons, banners, CSS and JavaScript files.  |


## API Endpoints
All the endpoints that make up the 4chan API. No additional GET parameters are accepted with any of these routes.

| **File name**   | **Description**      | **Documentation page**      | **URL example** |
|:----------------|:---------------------|:-------------------------------|:---------------- |
| `boards.json` | A list of all boards and their attributes. | [Boards](Boards.md) | [https://a.4cdn.org/boards.json](https://a.4cdn.org/boards.json) | 
|`threads.json` | A summarized list of all threads on a board including thread numbers, their modification time and reply count. | [Thread list](Threadlist.md) | [https://a.4cdn.org/po/threads.json](https://a.4cdn.org/po/threads.json) |
|`catalog.json` | A JSON representation of a board [catalog](https://boards.4channel.org/catalog). Includes all OPs and their preview replies. | [Catalog](Catalog.md) | [https://a.4cdn.org/po/catalog.json](https://a.4cdn.org/po/catalog.json) |
|`archive.json` | A list of all closed threads in a board archive. Archived threads no longer receive posts. | [Archive](Archive.md) | [https://a.4cdn.org/po/archive.json](https://a.4cdn.org/po/archive.json) |
| `/<board>/<page#>.json` | A list of threads and their preview replies from a specified index page. Index pages start at `1`. The maximum number of pages (can be found in `boards.json`) may vary depending on the board. | [Indexes](Indexes.md) | [https://a.4cdn.org/po/3.json](https://a.4cdn.org/po/3.json) |
|`/<board>/thread/<OP #>.json`| A full list of posts in a single thread. | [Threads](Threads.md) | [https://a.4cdn.org/po/thread/570368.json](https://a.4cdn.org/po/thread/570368.json) | 

