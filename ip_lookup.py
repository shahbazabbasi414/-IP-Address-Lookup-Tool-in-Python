import urllib.request as urllib2
import json

def get_ip_details(ip):
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    if values["status"] == "success":
        print(f"\nDetails for IP: {ip}")
        print("IP: " + values["query"])
        print("City: " + values["city"])
        print("ISP: " + values["isp"])
        print("Country: " + values["country"])
        print("Region: " + values["region"])
        print("Timezone: " + values["timezone"])
        print("Organization: " + values["org"])
        print("Country Code: " + values["countryCode"])
    else:
        print("Error retrieving IP information.")

choice = input("Do you want to use your personal computer's IP or another IP? (Enter '1' for personal IP, '2' for another IP): ")

if choice == '1':
    public_ip = urllib2.urlopen('https://api64.ipify.org').read().decode('utf8')
    print(f"\nUsing your personal computer's IP: {public_ip}")
    get_ip_details(public_ip)
elif choice == '2':
    custom_ip = input("\nEnter the IP you want to look up: ")
    get_ip_details(custom_ip)
else:
    print("Invalid choice, please enter '1' or '2'.")





