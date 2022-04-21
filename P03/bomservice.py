import requests
from requests.adapters import HTTPAdapter, Retry

class BomService():
    api = 'http://160.85.252.148'

    def get(self):
        try:
            s = requests.Session()
            retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 500, 502, 503, 504 ])
            s.mount('http://', HTTPAdapter(max_retries=retries))
            r = s.get(self.api)
            r.raise_for_status()
            r.encoding = 'UTF-8'
            return self.validate_response_data(r.json())
        except requests.exceptions.HTTPError as errh:
            print ('Http Error:', errh)
        except requests.exceptions.ConnectionError as errc:
            print ('Error Connecting:', errc)
        except requests.exceptions.Timeout as errt:
            print ('Timeout Error:', errt)
        except requests.exceptions.RequestException as err:
            print ('OOps: Something Else', err)

    def validate_response_data(self, response_data):
        validated_data = {}
        for key in response_data:
            try:
                value = int(response_data[key])
                if value > 0:
                    new_key = self.replace_encoding(key)
                    validated_data[new_key] = value
            except ValueError:
                pass
            except TypeError:
                pass
        return validated_data

    def replace_encoding(self, key):
        return key.encode('windows-1252').decode('utf-8')

def main():
    ac = BomService()
    print(ac.get())

if __name__ == '__main__':
    main()