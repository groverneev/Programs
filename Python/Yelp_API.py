from __future__ import print_function
import geocoder
import requests
import pprint
from urllib.parse import quote
api_key = "insert_api_key_here" #Replace with your Yelp API key
API_KEY= None
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 5
g = geocoder.ip('me')
lat = g.latlng[0]
lng = g.latlng[1]

#<URL>: <HOST>/<ENDPOINT>/<PARAMETERES>

def request(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()

def search(api_key, term, location):
    if b == "c":
        url_params = {
            'term': term.replace(' ', '+'),
            'limit': SEARCH_LIMIT,
            'latitude': lat,
            'longitude': lng
        }
    else:
        url_params = {
            'term': term.replace(' ', '+'),
            'location': location.replace(' ', '+'),
            'limit': SEARCH_LIMIT,
        }

    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    business_path = BUSINESS_PATH + business_id
    return request(API_HOST, business_path, api_key)

def query_api(term, location):
    response = search(API_KEY, term, location)
    businesses = response.get('businesses')

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return

    business_id = businesses[0]['id']

    print(u'{0} businesses found, querying business info ' \
        'for the top result "{1}" ...'.format(
            len(businesses), business_id))
    response = get_business(API_KEY, business_id)

    print(u'Result for business "{0}" found:'.format(business_id))
    pprint.pprint(response, indent=2)
a = input("What type of food are you looking for?")
b = input("Where do you want the buisness to be (or c for current location)?")
try:
    response = search(api_key, a, b)
    for i in range(len(response['businesses'])):
        print("")
        print(response['businesses'][i]['name'])
        test = response['businesses'][i]['location']['display_address']
        for counter in range(len(test)):
            print(test[counter])
        if response['businesses'][i]['is_closed']:
            print("The store is currently closed.")
        else:
            print("The store is currently open.")
except Exception:
    print("Sorry, please enter a valid place or type of food.")