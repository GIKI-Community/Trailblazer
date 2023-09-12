import requests

def main(Url):
	Url = "http://" + Url
	
	req = requests.get(url=Url)
	
	print(f"\n\n{req.headers}",end="\n\n")

	
	#print(f"\n{req.text}",end="\n\n")

	#print(req.headers["Content-Type"])

	if (req.headers["Content-Type"].find("json") != -1):
		print(f"=> {Url} is an api endpoint",end="\n\n")
	else:
		print(f"=> {Url} is not an api endpoint",end="\n\n")


Url = "google.com"
#Url = "csp.withgoogle.com/csp/gws/other-hp"
#Url = "api.shinemonitor.com/public/"

if __name__ == '__main__':
	main(Url)