# Google-Search-API
Search Google with a simple Python API

# Integration:
Wanna use this API?? Just add this to your `requirements.txt` (https://pip.pypa.io/en/stable/user_guide/#requirements-files)
```
git://github.com/Dmunch04/Google-Search-API.git
```
Does it not work? Try this:
```
git+git://github.com/Dmunch04/Google-Search-API.git
```

# API:
This is the attributes you can get from the class, GoogleSearch:
- title ; The title of the website/link
- description ; The content of the website. We limit it to be the little description we see on the website block on Google
- url ; The URL for the website

Example of use:
```python
import google as google

def mySearch (searchItem):
  result = google.search(search)[0]
  
  print(result.title)           # Prints the title of the result website
  print(result.description)     # Prints the description of the result website
  print(result.url)             # Prints the URL of the result website
```
