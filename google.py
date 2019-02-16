import os
import sys
import json
if sys.version < '3':
    from urllib2 import urlopen
    from urllib import quote as urlquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote as urlquote

URL_SEARCH = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='

class GoogleSearch (object):
  def __init__ (self, title, description, url):
    self.title = title
    self.description = description
    self.url = url
    
  def __str__ (self):
    return '%s: %s (%d)' % (self.title, self.description[:50], '...' if len(self.definition) > 50 else '', self.url)
    
def get_search_json (url):
  raw = urlopen(url).read()
  
  jsonData = json.loads(raw)
  
  results = jsonData
  
  return results
  
def parse_search_json (json):
  results = []
    
  for result in json:
    search = GoogleSearch(str(result['titleNoFormatting']), str(result['content']), str(result['url']))
    
    results.append(search)
    
  return results
    
def search (searchItem):
  json = get_search_json(URL_SEARCH + urlquote(searchItem))
  return parse_search_json(json)
