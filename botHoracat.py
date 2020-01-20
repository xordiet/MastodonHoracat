from mastodon import Mastodon
import random
from hora_meva import horameva
from hora_tradicional import horatradicional

# Set up Mastodon
mastodon = Mastodon(
	access_token = 'tokenHoracat.secret',
	api_base_url = 'https://botsin.space/'
)

mostrameva = horameva()
mostratrad = horatradicional()

rand = random.randint(0,6)
if rand == 3:
	random_bit = random.getrandbits(1)
	if random_bit == 1:
		mastodon.status_post(mostratrad)
	else:
		mastodon.status_post(mostrameva)
