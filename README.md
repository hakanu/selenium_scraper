Selenium Scraper
================

A python scraper by using selenium which helps to parse the site after being fully loaded (AJAX calls, flash async loads etc).

# Fire up an instance
Not so easy...

## Prereqs
* Ubuntu machine (Preferably latest)
* Not ARM architecture. Can not make this run on my raspberry pi. If somebody has already done, shoot me a mail.
* sudo easy_install selenium
* sudo easy_install pyvirtualdisplay
* sudo apt-get install xvfb

In my case, Firefox and phantomjs are not capable of showing the flash videos. Chrome is the only successful one.

### Install chrome

* http://www.howopensource.com/2011/10/install-google-chrome-in-ubuntu-11-10-11-04-10-10-10-04/
* wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
* sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
* sudo apt-get update
* sudo apt-get install google-chrome-stable
* Make sure chrome is install at /usr/bin/google-chrome

`ls /usr/bin | grep chrome`
* Get chrome driver from [here](http://chromedriver.storage.googleapis.com/index.html) to be able to use selenium with chrome.

`wget http://chromedriver.storage.googleapis.com/2.10/chromedriver_linux64.zip`

`unzip  chromedriver_linux64.zip`

`python selenium_scraper_server.py`

Go to [localhost:8080/url=%url%&p=%pattern%](http://localhost:8080/url=%url%&p=%pattern%)

Eg [localhost:8080/url=hakanu.net&p=hakan](http://localhost:8080/url=hakanu.net&p=hakan)

## Restrictions:
* Pattern and url must be percent encoded.
http://www.url-encode-decode.com/
* Pattern should not use +, instead * should be used. Because there is some confusion between url encoding's + (for space) and regexp +.
