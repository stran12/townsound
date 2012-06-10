from flask import Flask, request, abort
app = Flask(__name__)

import requests
import json
import sys

from datetime import date
from dateutil.relativedelta import relativedelta
from pymongo import Connection

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/")
def api():
    metro = request.args.get('metro')
    venue = request.args.get('venue')

    if metro is None:
        abort(404)
    metro_id = getMetroId(request.args.get('metro'))

    # Get all artists playing in the next week from SK in that metro_id
    #all_artists = getArtistsFromMetro(metro_id)
    return getMetroEvents(metro_id)


def getArtistsFromMetro(metro_id):
    eventsArr = getMetroEvents(metro_id)



def getMetroEvents(metro_id):
    conn = Connection()
    db = conn.ts_db
    events = db.events
    one_week = str( date.today() + relativedelta( days = +9) )
    print "THIS IS ONE WEEK: " + one_week
    all_events = []
    for e in events.find( { "date": { "$lt": one_week} }, {'_id':0} ):
        all_events.append(e)

    conn.disconnect()
    return json.dumps( all_events )


# Returns a numeral string 
def getMetroId(city):
    r = requests.get('http://api.songkick.com/api/3.0/search/locations.json?query='
        + city + '&apikey=ztnbkV65yjqoqrVW')
    # turn it into JSON
    metro_obj = json.loads(r.text)
    # Grab id
    mid = metro_obj['resultsPage']['results']['location'][0]['metroArea']['id']
    return str(mid)



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
