import requests
import ipaddress

class Ip_checker:
    def check_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
        except Exception:
            return "Enter valid IP address!"
        result = ''
        lat, long = ["", ""]
        try:
            r = requests.get(f"https://ipwhois.app/json/{ip}").json()
        except Exception as e:
            return f"Some error occurred: {e}"
        #r = {"ip":"1.2.3.4","success":"OK","type":"IPv4","continent":"Oceania","continent_code":"OC","country":"Australia","country_code":"AU","country_capital":"Canberra","country_phone":"+61","country_neighbours":"","region":"Queensland","city":"Brisbane","latitude":-27.4697707,"longitude":153.0251235,"asn":"","org":"Resource Quality Assurance","isp":"Resource Quality Assurance","timezone":"Australia/Brisbane","timezone_name":"AEST","timezone_dstOffset":0,"timezone_gmtOffset":36000,"timezone_gmt":"+10:00","currency":"Australian Dollar","currency_code":"AUD","currency_symbol":"$","currency_rates":1.515,"currency_plural":"Australian dollars"}
        if r['success'] == True:
            for k, v in r.items():
                if r[k] != '':
                    if k == "latitude":
                        lat = v
                    if k == "longitude":
                        long = v
                    result += f'{k.capitalize()}: {v}\n'
            if 'Latitude' in result and 'Longitude' in result:
                result += f"Google maps: https://maps.google.com/?q={lat},{long}"
            return result
        else:
            return f"Cannot get information from the API: {r['message']}"

    check_ip.display_name = "IP Checker"
    check_ip.display_markup = "Enter IP Address (Example: 1.2.3.4):"