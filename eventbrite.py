import requests

url = "https://www.eventbriteapi.com/v3/"

response = requests.get(
    url + "users/me/owned_events/?expand=venue",
    headers = {
        "Authorization": "Bearer QDVP7QBIJIWV2FWZ7NQ7",
    }
)

my_events = response.json()['events'][0]
print response.json()['pagination']['page_count']

print my_events['name']['text'] + ': ' + my_events['description']['text']

print my_events

res = requests.post(
	url + "events/",
	headers = {"Authorization": "Bearer QDVP7QBIJIWV2FWZ7NQ7"},
	params = {
	"event.name.html" : "New Event",
	"event.description.html" : "Check out my awesome new event!",
	"event.online_event" : True,
	"event.currency" : "USD",
	"event.start.timezone": "America/Los_Angeles",
	"event.end.timezone": "America/Los_Angeles",
	"event.start.utc" : "2015-11-08T01:00:00Z",
	"event.end.utc" : "2015-11-08T06:00:00Z",
	"event.listed" : False,
	"event.capacity" : 10
	}
)

new_event = res.json()

print new_event

update = requests.post(
	url + "events/18835645924/ticket_classes/",
	headers = {"Authorization": "Bearer QDVP7QBIJIWV2FWZ7NQ7"},
	params = {
	"ticket_class.name" : "General Admission",
	"ticket_class.free" : True,
	"ticket_class.quantity_total" : 10
	}
)

tickets = update.json()

print tickets
