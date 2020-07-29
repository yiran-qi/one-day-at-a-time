import requests
import random

import ticketpy

tm_client = ticketpy.ApiClient('oArnE5AzUFNrwKGW5FNoP3vAaxqXvXPX')

def getEvents(query, key):
    steps = []
    query = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey=oArnE5AzUFNrwKGW5FNoP3vAaxqXvXPX"
    recipe = requests.get(query).json()
    #return recipe["results"][0]["analyzedInstructions"][0]["steps"]
    return steps