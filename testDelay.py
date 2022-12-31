# coding=UTF-8

from mastodon import Mastodon
import datetime
import time

# Set up Mastodon
mastodon = Mastodon(
	access_token = 'tokenHoracat.secret',
	api_base_url = 'https://botsin.space/'
)


mastodon.status_post("Hola,") #1
time.sleep(1)
mastodon.status_post("això") #2
time.sleep(1)
mastodon.status_post("és") #3
time.sleep(1)
mastodon.status_post("una") #4
time.sleep(1)
mastodon.status_post("prova") #5
time.sleep(1)
mastodon.status_post("de") #6
time.sleep(1)
mastodon.status_post("publicació") #7
time.sleep(1)
mastodon.status_post("cada") #8
time.sleep(1)
mastodon.status_post("un") #9
time.sleep(1)
mastodon.status_post("segon.") #10
time.sleep(1)
mastodon.status_post("Disculpeu") #11
time.sleep(1)
mastodon.status_post("les") #12
time.sleep(1)
mastodon.status_post("molèsties " + any)
