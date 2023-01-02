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

if hora = 1 or hora = 13:
	mastodon.status_post("Dong") #1
elif hora = 2 or hora = 14:
	mastodon.status_post("Dong, Dong") #2
elif hora = 3 or hora = 15:
	mastodon.status_post("Dong, Dong, Dong") #3
elif hora = 4 or hora = 16:
	mastodon.status_post("Dong, Dong, Dong, Dong") #4
elif hora = 5 or hora = 17:
	mastodon.status_post("Dong, Dong, Dong, Dong, Dong") #5
elif hora = 6 or hora = 18:
	mastodon.status_post("Dong, Dong, Dong, Dong, Dong, Dong") #6
elif hora = 7 or hora = 19:
	mastodon.status_post("Dong, Dong, Dong, Dong, Dong, Dong, Dong") #7
elif hora = 8 or hora = 20:
	mastodon.status_post("Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong") #8
elif hora = 9 or hora = 21:
	mastodon.status_post("Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong") #9
elif hora = 10 or hora = 22:
	mastodon.status_post("Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong") #10
elif hora = 11 or hora = 23:
	mastodon.status_post("Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong") #11
elif hora = 12 or hora = 0:
	mastodon.status_post("Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong, Dong") #12
else:
	mastodon.status_post("Error al tocar les campanades, aviseu al campaner")

# fi
