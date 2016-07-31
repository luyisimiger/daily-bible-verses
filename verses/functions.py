import httplib2
import json

def get_verse_from_ourmanna(random):
    
    http = httplib2.Http()
    url = "http://www.ourmanna.com/verses/api/get/?format=json"
    
    if random:
        url += "&order=random"
        
    return http.request(url, method="GET")
