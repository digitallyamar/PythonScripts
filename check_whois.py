import sys, whois

def get_whois_record(name):
    return whois.query(name)

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print ("Usage: python3 check_whois.py <domain_name>")
		sys.exit(0)

	name = sys.argv[1]
	print ("Checking domain: " + name)

	whois_record = get_whois_record(name)

	try:
		print('whois_record:')
		print(whois_record.__dict__)
	except:
		print('\n*** !!Domain not registered!! ***\n')
