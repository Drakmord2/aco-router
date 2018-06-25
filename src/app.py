import googlemaps
from datetime import datetime

def main():
    gmaps = googlemaps.Client(key='Add Your Key here')

    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                         "Parramatta, NSW",
                                         mode="transit",
                                         departure_time=now)
    print(directions_result)

if __name__ == '__main__':
    print('\n\t-- ACO Router --')

    main()

# TODO Try catch só no final
#    try:
#        main()
#    except Exception as err:
#        print('- Runtime error: ', err)