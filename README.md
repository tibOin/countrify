# countrify
Automatically start Tor Proxy to end in specific country.

### Usage
`python countrify.py [countrycode]`

You'll have to configure your browser to connect through the proxy.
It's a Socks5 Proxy turning on your **localhost** at port **9000** by default.
(you could modify it by changing `SOCKS_PORT` value in the script)

### Info
To get a list of country codes :  [wikipedia](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements "ISO_3166-1_alpha - Country Codes")

It needs Tor to work, so visit [Tor Project's website](https://www.torproject.org "Tor Project") for more informations.

To install Tor :
+ if you're under linux : `apt-get install tor`
+ Otherwise, go [here](https://www.torproject.org/download/download-easy.html.en "Tor Project's Download Page")

It will need python modules :
+ [stem] - `pip install stem`
+ [pycurl] - `pip install pycurl`

[stem]: https://stem.torproject.org "Stem website"
[pycurl]: http://pycurl.io/ "PycURL's website"
