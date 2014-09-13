import json
import urllib
import HTMLParser

import web

import selenium_scraper

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())


class hello:        
  def GET(self, url):
    print 'Get request for ', url

    # Url comes as percent encoded.
    url = urllib.unquote(url).decode('utf8')
    if not url:
      return ''

    web.header('Content-Type', 'application/json')

    if url in web.CACHED_MATCHES:
      print 'Cache hit'
      return web.CACHED_MATCHES[url]

    print 'Cache miss'
    try:
      result = selenium_scraper.GetPatternFromGivenUrl(url)
    except:
      print 'Error while scraping, returning []'
      return []

    unescaped_result = []
    for r in result:
      unescaped_result.append(HTMLParser.HTMLParser().unescape(r))

    json_result = json.dumps(unescaped_result)
    web.CACHED_MATCHES[url] = json_result

    return json_result

if __name__ == "__main__":
  web.CACHED_MATCHES = {}
  app.run()