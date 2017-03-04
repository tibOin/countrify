import sys, io, webbrowser
import pycurl
import stem.process
from stem.util import term

SOCKS_PORT = 9000

# Query() ----------------------------------------------------------------------
def clearquery(url):
  output = io.BytesIO()

  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.WRITEFUNCTION, output.write)

  try:
    query.perform()
    return output.getvalue()
  except pycurl.error as exc:
    return "Unable to reach %s (%s)" % (url, exc)

def torquery(url):
  """
  Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
  """

  output = io.BytesIO()

  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, 'localhost')
  query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
  query.setopt(pycurl.WRITEFUNCTION, output.write)

  try:
    query.perform()
    return output.getvalue()
  except pycurl.error as exc:
    return "Unable to reach %s (%s)" % (url, exc)
# ------------------------------------------------------------------------------

# Start Tor --------------------------------------------------------------------
# Start an instance of Tor configured to only exit through Russia. This prints
# Tor's bootstrap information as it starts. Note that this likely will not
# work if you have another Tor instance running.
def startTorWithExitNodeIn(country):
    # Output Tor's launch status --------------------------------------------#
    def print_bootstrap_lines(line):                                         #
        if "Bootstrapped " in line:                                          #
            if "Done" in line:                                               #
                print(term.format(line, term.Color.GREEN))                   #
            elif "[warn]" in line:                                           #
                print(term.format(line, term.Color.YELLOW))                  #
            elif "[error]" in line:                                          #
                print(term.format(line, term.Color.RED))                     #
            else:                                                            #
                print(term.format(line, term.Color.CYAN))                    #
    # -----------------------------------------------------------------------#

    print(term.format("Starting Tor:\n", term.Attr.BOLD))
    countrycode = '{'+country+'}'

    return stem.process.launch_tor_with_config(
      config = {
        'SocksPort': str(SOCKS_PORT),
        'ExitNodes': countrycode
      },
      init_msg_handler = print_bootstrap_lines,
      take_ownership = True
    )
# ------------------------------------------------------------------------------

# Check ExitNodes --------------------------------------------------------------
def isExitNodeIn(country):
    print(term.format("\nChecking our endpoint:\n", term.Attr.BOLD))

    locale = 'Locale: {0}'.format(country.upper())
    response = torquery("https://www.atagar.com/echo.php")

    if locale in response:
        print(term.format("You new IP is : " + response, term.Color.GREEN))
        return True
    else:
        print(term.format(response, term.Color.RED))
        return False
# ------------------------------------------------------------------------------

# Verify IP --------------------------------------------------------------------
def isYourRealIP():
    real   = clearquery("https://www.atagar.com/echo.php")
    hidden = torquery("https://www.atagar.com/echo.php")
    print term.format('Your real IP is : ' + real, term.Color.YELLOW)
    if real == hidden:
        return True
    else:
        return False

# Main -------------------------------------------------------------------------
def main():
    if len(sys.argv) < 2:
        print 'Usage : python russia.py [countrycode]'
        print 'This script automatically start a Tor proxy allowing you to browse internet as if you were in a specific country'
        print 'To get a list of country codes : ' + term.format('http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2', term.Color.MAGENTA)
        print term.format('You\'ll have to configure your browser to connect through the proxy', term.Color.YELLOW)
    else:
        country = str(sys.argv[1]).lower()
        tor_process = startTorWithExitNodeIn(country)

        while isExitNodeIn(country) == False or isYourRealIP() == True:
            tor_process.kill()
            tor_process = startTorWithExitNodeIn(country)

        socks5str = term.format('Socks5', term.Color.YELLOW)
        hoststr   = term.format("localhost:" + str(SOCKS_PORT), term.Color.YELLOW)
        configstr = "You can now configure your browser to use {} proxy at {}".format(socks5str, hoststr)
        print term.format('Now it\'s up to you...\n', term.Attr.BOLD)
        print term.format(configstr, term.Color.GREEN)
        print term.format("After configuring, reload the page automatically opened and check if infos are the same as above\n", term.Color.GREEN)
        webbrowser.open('https://www.atagar.com/echo.php', new=2)

        raw_input("Press Enter to close Tor...\r")
        print term.format('Killing Tor...', term.Color.RED)
        tor_process.kill()  # stops tor
        print term.format('Tor has been stopped', term.Color.GREEN)
        print term.format('Remember to remove proxy configuration in your browser', term.Color.YELLOW)

main()
