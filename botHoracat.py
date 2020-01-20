from mastodon import Mastodon
import random
from hora_meva import horameva

# Set up Mastodon
mastodon = Mastodon(
	access_token = 'tokenHoracat.secret',
	api_base_url = 'https://botsin.space/'
)

mostrahora = horameva()

rand = random.randint(0,6)
if rand == 3:
	mastodon.status_post(mostrahora)
