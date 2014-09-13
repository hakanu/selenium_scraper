"""Very simple handler for routing scraping requests to selenium_scraper module.

"""

__author__ = 'Hakan'

import json
import urllib
import HTMLParser

import web

import selenium_scraper

_DEBUG = False
urls = (
    '/url=(.*)&p=(.*)', 'ScrapeApiHandler',
    '/clean', 'CleanCacheHandler'
)
app = web.application(urls, globals())


class CleanCacheHandler:
  """Cache cleanup handler."""
  def GET(self):
    print 'Cleaning match cache.'
    web.CACHED_MATCHES = {}
    return 'Success'


class ScrapeApiHandler:
  """Scraping API handler."""
  def GET(self, url, pattern):
    web.header('Content-Type', 'application/json')
    
    if _DEBUG: 
      print 'Get request for ', url

    # Url comes as percent encoded.
    if not url or not pattern:
      return ''

    # Decode url to process.
    url = urllib.unquote(url).decode('utf8')

    # Hacky way to get rid of +.
    pattern = urllib.unquote(pattern).decode('utf8').replace('+', ' ')

    if url in web.CACHED_MATCHES:
      print 'Cache hit'
      return web.CACHED_MATCHES[url]

    print 'Cache miss'
    try:
      result = selenium_scraper.GetPatternFromGivenUrl(url, pattern)
    except:
      print 'Error while scraping, returning []'
      return []

    unescaped_result = []
    for r in result:
      unescaped_result.append(HTMLParser.HTMLParser().unescape(r))

    json_result = json.dumps(unescaped_result)
    web.CACHED_MATCHES[url] = json_result  # Cache the result for future use.

    return json_result

if __name__ == "__main__":
  web.CACHED_MATCHES = {}  # Initialize cache dict.
  app.run()