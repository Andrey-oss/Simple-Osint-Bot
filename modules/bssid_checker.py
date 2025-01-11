import requests

class Bssid_checker:
    def bssid_check(self, bssid):
        result = ""
        lat, long = ['', '']
        r1 = requests.get(f"https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid={bssid}").json()

        if r1['result'] == 400:
            return r1['desc']

        if r1['data']:
            for k, v in r1['data'].items():
                if k == 'lat':
                    lat = v
                if k == 'lon':
                    long = v
                result += f"{k.capitalize()}: {v}\n"
        if 'Lat' in result and 'Lon' in result:
            result += f"Google maps: https://maps.google.com/?q={lat},{long}"
        return result
    
    bssid_check.display_name = "BSSID Checker"
    bssid_check.display_markup = "Enter BSSID (Example: 00:0C:42:1F:65:E9):"