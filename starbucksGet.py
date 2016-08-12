import mechanize,re,exceptions
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser

username = raw_input("Username:")
password = raw_input("Password:")

br = mechanize.Browser()
# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36')]

#open the login page
r = br.open('https://www.starbucks.co.uk/account/signin')
html = r.read()


# Attempt login
br.select_form(nr=0)
br.form['Account.UserName']= username
br.form['Account.PassWord']= password
br.submit()


# Read page + Filter html to only show the message content
html = br.response().read()
soup = BeautifulSoup(html)

balancediv = str(soup.find('div', attrs={'class': 'balance-amount numbers'}))

def print_balance(data):
	try:
		bal = float(data)
		print u"\xA3" + str(bal)
	except exceptions.ValueError:
		return

class STBXScraper(HTMLParser):
	def handle_data(self, data):
		print_balance( data )
		
parser = STBXScraper()
parser.feed( balancediv )

raw_input()
