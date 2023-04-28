# Calling modules
import requests,os

# Install requests
print("\033[30;43m Install requests \033[0m")
os.system("pip install requests")
os.system("clear")

# Beautify the top
def banner():
	print("""
\033[34m██ ██████         ██████  ███████ ██ ███    ██ ████████
\033[34m██ ██   ██       ██    ██ ██      ██ ████   ██    ██
\033[34m██ ██████  █████ ██    ██ ███████ ██ ██ ██  ██    ██
\033[0m██ ██            ██    ██      ██ ██ ██  ██ ██    ██
\033[0m██ ██             ██████  ███████ ██ ██   ████    ██
\033[30;46m Simple IP OSINT (Open Source Intelligence) \033[0m\n""")
banner()

# Ask the IP that you want to extract
ip = input("\033[30;43m Enter the Target IP \033[0m : ")
# We use the site ipinfo.io
url = "https://ipinfo.io/"+ip+"/json"
respon = requests.get(url)

# If the generated status code is 200, the extraction was successful
if respon.status_code == 200:
	result = respon.json()
	print("\033[3;41m={>>> Information <<<}= \033[0m")
	print("\033[1;32mIP              \033[0m:",result.get("ip"))
	print("\033[1;32mHostname        \033[0m:",result.get("hostname"))
	print("\033[1;32mAnycast         \033[0m:",result.get("anycast"))
	print("\033[1;32mCity            \033[0m:",result.get("city"))
	print("\033[1;32mRegion          \033[0m:",result.get("region"))
	print("\033[1;32mCountry         \033[0m:",result.get("country"))
	print("\033[1;32mLocation        \033[0m:",result.get("loc"))
	print("\033[1;32mOrganization    \033[0m:",result.get("org"))
	print("\033[1;32mZIP/Postal Code \033[0m:",result.get("postal"))
	print("\033[1;32mTime Zone       \033[0m:",result.get("timezone"))
	print("\033[1;32mRead More       \033[0m:",result.get("readme"))
else:
	# Unless the status code is 200, the extraction failed
	print("There is something wrong! The web is unreachable. HTTP Response:",respon.status_code)
