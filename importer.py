from pymongo import Connection
from time import sleep
from datetime import date
from dateutil.relativedelta import relativedelta

import sys
import requests
import json
import pprint

counter = 1 # For page in get_url for SK API
get_url = 'http://api.songkick.com/api/3.0/metro_areas/17835/calendar.json?apikey=ztnbkV65yjqoqrVW&per_page=50&page='

artists = []

latest_date = str( date.today() )

one_week = str( date.today() + relativedelta( days = +1) )
one_week = str( date.today() )

while ( latest_date <= one_week ):
    print "Querying: " + get_url + str(counter)

    r = requests.get( get_url + str(counter) )
    if r.status_code != 200:
        sys.exit("Got the follow response_code from SK: " + str(r.status_code))

    print "Loading response body into JSON"
    events_obj = json.loads(r.text)

    print "Traversing through response JSON object for events"
    events = events_obj['resultsPage']['results']['event']
    for event in events:
        latest_date = event['start']['date'] 
        for p in event['performance']:
            artists.append( 
                dict(artist=p['artist']['displayName'],
                     date=latest_date,
                     venue=event['venue']['displayName'])
            )
        if( latest_date == one_week ):
            break

    print "This is the latest date: " + latest_date
    print "Found " + str(len(artists)) + " events so far"
    # IMPORTANT!
    counter += 1
    print "The counter is now" + str(counter)
    sleep(5)


connection = Connection()
db = connection.ts_db
events = db.events

for a in artists:
    pprint.pprint(a)
    events.insert(a)

connection.disconnect()
