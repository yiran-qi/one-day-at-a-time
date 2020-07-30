import requests
from collections import defaultdict

list_of_events = defaultdict(list)
def getEvents(query, key):
    query = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={key}&postalCode={query}"
    event = requests.get(query).json()
    for num in range(0, 10):
        name = event["_embedded"]["events"][num]["name"]
        info = event["_embedded"]["events"][num]["info"]
        image = event["_embedded"]["events"][num]["images"][1]["url"]
        url = event["_embedded"]["events"][num]["url"]
        list_of_events["events"].append({"name": name, "info": info, "image": image, "url": url})
    return list_of_events

# print(getEvents("28262", "oArnE5AzUFNrwKGW5FNoP3vAaxqXvXPX"))
