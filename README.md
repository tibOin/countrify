# countrify
Automatically start Tor Proxy to end in specific country.

Allows you to browse the web from everywhere on the planet as if you were in a country of your choice.
Useful to bypass geographic limitations on services you use.
Yes! It's not because you've moved your ass from your home that you can't continue doing what you do!

### Installation
If Tor is not installed on your computer, don't worry!
There are scripts to automate setup.

Platforms :
+ Linux -> `./linux-setup.sh` or `bash linux-setup.sh`
+ macOS -> `bash macos-setup.sh`
+ ~~Windows -> Not yet~~

*Please ensure your terminal is in the countrify's root folder -> `cd path/to/countrify`*


### Usage
`python countrify.py [countrycode]`

+ On macOS, it will configure the system to use Tor proxy automatically. And disable it on exit. (it will ask for root access)
+ On linux, You'll have to configure your browser to connect through the proxy.
It's a Socks Proxy turning on your **localhost** at port **9000** by default.
(you could modify it by changing `SOCKS_PORT` value in the script)
+ ~~On Windows, I don't know yet...~~


### Infos
To get a list of country codes :  [Wikipedia](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements "ISO_3166-1_alpha - Country Codes")

This script uses Tor, so visit [Tor Project's website](https://www.torproject.org "Tor Project") for more informations.

It uses python modules :
+ [stem] - `pip install stem`
+ [pycurl] - `pip install pycurl`

*You don't need to install them yourself if you use setup scripts*

It's mainly based on the *'To Russia With Love'* tutorial from [stem website](https://stem.torproject.org/tutorials/to_russia_with_love.html "To Russia With Love")

[stem]: https://stem.torproject.org "Stem website"
[pycurl]: http://pycurl.io/ "PycURL's website"
