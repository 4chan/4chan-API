# 4chan API #
#### Welcome to the documentation for 4chan's read-only JSON API, originally launched in September of 2012.
----
## Getting started
Data from the 4chan API is exclusively accessible from `a.4cdn.org`, via either `http://` or `https://` protocols. `a.4cdn.org` serves JSON representations of posts made at [`4chan.org`](https://4chan.org/) and [`4channel.org`](https://4channel.org/) boards.  All examples in the documentation for the 4chan API use `https://`.

[CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is supported from origins `boards.4chan.org` or `boards.4channel.org`, via `http://` or `https://`. Requests are accepted when using the following HTTP request types:
  - [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
  - [`OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS)
  - [`HEAD`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD)

### Table of contents ###

| **Documentation Page**   | **Description**      |
|:-------------------------|:---------------------|
| [Endpoints and Site Domains](pages/Endpoints_and_domains.md) | A quick rundown of all 4chan API endpoints and site domains.|
| [Media and Static Content](pages/User_images_and_static_content.md) | Paths and locations for static site content including custom spoiler images, country flags, capcodes and user submitted media |
| [Archive.json](pages/Archive.md) | Documentation for the 4chan native archive and its JSON|
| [Boards.json](pages/Boards.md) | Documentation for the 4chan board list and its attributes. |
| [Catalog.json](pages/Catalog.md) | Documentation for the JSON representation of the 4chan native catalog |
| [Index endpoint](pages/Indexes.md) | Documentation for the JSON representaion of board index (main) pages |
| [Thread endpoint](pages/Threads.md) | Documentation for the JSON representation of specific 4chan threads. |
| [Thread list](pages/Threadlist.md) | Documentation for the board threadlist and its brief stats|

### API Rules ###

1. Do not make more than one request per second. 
2. Thread updating should be set to a minimum of 10 seconds, preferably higher.
3. Use [If-Modified-Since](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since) when doing your requests.
4. Make API requests using the same protocol as the app. Only use SSL when a user is accessing your app over HTTPS.

### API Terms of Service ###

1. You may not use "4chan" in the title of your application, product, or service.
2. You may not use the 4chan name, logo, or brand to promote your application, product, or service.
3. You must disclose the source of the information shown by your application, product, or service as 4chan, and provide a link.
4. You may not market your application, product, or service as being "official" in any way.
5. You may not clone 4chan or its existing features/functionality. Example: Don't suck down our JSON, host it elsewhere, and throw ads around it.
6. These terms are subject to change without notice.

-------

To view a pretty-printed version of our thread, index, and catalog JSON, use [JSONLint](http://jsonlint.com).

Still have questions or concerns? Open an issue or email [api@4chan.org](mailto:api@4chan.org)
