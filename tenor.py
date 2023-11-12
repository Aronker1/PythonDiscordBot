import json
import random
import requests
import os

def getGif(search_term):
  apikey = os.getenv("TENOR_API")
  lmt = 10
  ckey = "my_test_app"
  # get the top 8 GIFs for the search term
  r = requests.get(
    "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey, lmt))
  if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    top_8gifs = json.loads(r.content)
    selection = random.randint(0,len(top_8gifs['results'])-1)
    return top_8gifs['results'][selection]['url']
  else:
    top_8gifs = None

