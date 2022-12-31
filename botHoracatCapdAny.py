from mastodon import Mastodon
import datetime
import time

# Set up Mastodon
mastodon = Mastodon(
	access_token = 'tokenHoracat.secret',
	api_base_url = 'https://botsin.space/'
)

#esbrina la hora
now= datetime.datetime.now()
hora = now.hour
minut = now.minute
any = now.year

if hora = 23 and minut = 57:
	mastodon.status_post("Falten tres minuts per acabar l'any " + any + ", prepara el raïm.")

if hora = 23 and minut = 59:
	mastodon.status_post("Darrer minut de l'any " + any)

if hora = 00 and minut = 00:
	mastodon.status_post("Dong") #1
	time.sleep(1)
	mastodon.status_post("Dong") #2
	time.sleep(1)
	mastodon.status_post("Dong") #3
	time.sleep(1)
	mastodon.status_post("Dong") #4
	time.sleep(1)
	mastodon.status_post("Dong") #5
	time.sleep(1)
	mastodon.status_post("Dong") #6
	time.sleep(1)
	mastodon.status_post("Dong") #7
	time.sleep(1)
	mastodon.status_post("Dong") #8
	time.sleep(1)
	mastodon.status_post("Dong") #9
	time.sleep(1)
	mastodon.status_post("Dong") #10
	time.sleep(1)
	mastodon.status_post("Dong") #11
	time.sleep(1)
	mastodon.status_post("Dong") #12
	time.sleep(1)
	mastodon.status_post("Feliç " + any)
