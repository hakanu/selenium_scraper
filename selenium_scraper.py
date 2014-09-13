from contextlib import closing
from selenium import webdriver
#from selenium.webdriver import Firefox # pip install selenium
#from selenium.webdriver import PhantomJS
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display

import re

display = Display(visible=0, size=(800, 600))
display.start()


def GetPatternFromGivenUrl(
    url='', regex_pattern='<param name="flashvars" value="(.+)" />',
    element_name_to_check='flashvars'):
  """Heavy method to scrape the web pages with ajax calls, lazy loads and flash
  content.
  
  Args:
    url: string.
    regex_pattern: string. Default value is for playwire videos.
  
  Returns:
    list of matched items.
  """
  print 'Started'
  if not url:
    return []

  # use firefox to get page with javascript generated content
  #with closing(Firefox()) as browser:
  #with closing(Chrome()) as browser:  # PhantomJS
  #with closing(webdriver.Remote("http://localhost:9515", desired_capabilities=DesiredCapabilities.CHROME)) as browser:  # Fake chrome.
  # Don't know why it's not working with relative path. Pass absolute!
  with closing(webdriver.Chrome('/home/haku/chromedriver')) as browser:  # Fake chrome.
    browser.get(url)
    WebDriverWait(browser, timeout=30).until(
        EC.presence_of_element_located((By.NAME, element_name_to_check)))
    page_source = browser.page_source
    #print '-----------------\n', page_source
    print 'Finished'

    return re.findall(regex_pattern, page_source)
    