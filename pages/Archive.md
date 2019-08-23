## Archive.json ##
| **Example url** | [`https://a.4cdn.org/po/archive.json`](https://a.4cdn.org/archive.json) | 
|:----------------|:-------------------------------------|
| **Status 200**  | Content-Type: application/json |

Archived threads are read-only threads that are are closed to new replies and images. Threads are archived when they are pushed off the last page of a board. 
Archived threads and their attachments remain viewable for a specific amount of time before they are automatically deleted from 4chan.
It's important to note that not all boards have archives enabled. 


## Archive JSON Structure ##
| **Attribute** | **Type** | **Appears** | **Description** |
|:--------------|:--------------|:--------------|:--------------|
| _no named attribute_ | `array` | `always` | The only structure in archive.json is an array of integers. These are the OP numbers of archived threads|


## Example file ##

```json
[571958,572866,54195,574342,574378,574398,574417,574426,574435,574453,574486,574510,574586,574588]
```

This is a JSON array of archived thread IDs.
