## threads.json ##
| **Example url** | [`https://a.4cdn.org/po/threads.json`](https://a.4cdn.org/po/threads.json) | 
|:----------------|:-------------------------------------|
| **Status 200**  | Content-Type: application/json |

The `threads.json` file is a comprehensive list of all threads that contains:
 - The thread OP number
 - The index page the thread is currently on
 - A [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) marking the last time the thread was modified
 - The number of replies a thread has


## Archive JSON Structure ##

| **Attribute**   | **Type**       | **Appears**                | **Description** | **Possible values**|
|:----------------|:---------------|:---------------------------|:----------------|:-------------------|
| `page`          | `integer`      | `always` | The page number that the following `threads` array is on | `Any positive integer` |
| `threads`       | `array`        | `always` | The array of thread objects | `array of objects`|
| `no`            | `integer`      | `always` | The OP ID of a thread | `Any positive integer` |
| `last_modified` | `integer`      | `always` | The UNIX timestamp marking the last time the thread was modified (post added/modified/deleted, thread closed/sticky settings modified) | `UNIX Timestamp` |
| `replies`       | `integer`      | `always` | A numeric count of the number of replies in the thread | `Any positive integer` |

* integer 1 = (on) or 0 (off)

## Example file ##

```json
[{
    "page": 1,
    "threads": [{
        "no": 570368,
        "last_modified": 1546294897,
        "replies": 2
    }, {
        "no": 567982,
        "last_modified": 1566438201,
        "replies": 63
    }, {
        "no": 574224,
        "last_modified": 1566456119,
        "replies": 4
    }, {
        "no": 576101,
        "last_modified": 1566406602,
        "replies": 0
    }, {
        "no": 553409,
        "last_modified": 1566391725,
        "replies": 250
    }, {
        "no": 545554,
        "last_modified": 1566367896,
        "replies": 169
    }]
}, {
    "page": 2,
    "threads": [{
        "no": 575972,
        "last_modified": 1566435330,
        "replies": 2
    }, {
        "no": 576045,
        "last_modified": 1566309370,
        "replies": 2
    }, {
        "no": 576048,
        "last_modified": 1566275920,
        "replies": 1
    }]
}]
```
