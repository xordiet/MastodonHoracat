from mastodon import Mastodon
import datetime
import random

#esbrina la hora
now= datetime.datetime.now()

# Set up Mastodon
mastodon = Mastodon(
	access_token = 'tokenHoracat.secret',
	api_base_url = 'https://botsin.space/'
)
hora = now.hour
minut = now.minute

lahora = {
	0: "les dotze",
	1: "la una",
	2: "les dues",
	3: "les tres",
	4: "les quatre",
	5: "les cinc",
	6: "les sis",
	7: "les set",
	8: "les vuit",
	9: "les nou",
	10: "les deu",
	11: "les onze",
	12: "les dotze",
	13: "la una",
	14: "les dues",
	15: "les tres",
	16: "les quatre",
	18: "les sis",
	19: "les set",
	20: "les vuit",
	21: "les nou",
	22: "les deu",
	23: "les onze",
	24: "les dotze"
}

dehora = {
	0: "d'una",
	1: "de dues",
	2: "de tres",
	3: "de quatre",
	4: "de cinc",
	5: "de sis",
	6: "de set",
	7: "de vuit",
	8: "de nou",
	9: "de deu",
	10: "d'onze",
	11: "de dotze",
	12: "d'una",
	13: "de dues",
	14: "de tres",
	15: "de quatre",
	16: "de cinc",
	17: "de sis",
	18: "de set",
	19: "de vuit",
	20: "de nou",
	21: "de deu",
	22: "d'onze",
	23: "de dotze",
	24: "d'una"
}

lahorames = {
	0: "la una",
	1: "les dues",
	2: "les tres",
	3: "les quatre",
	4: "les cinc",
	5: "les sis",
	6: "les set",
	7: "les vuit",
	8: "les nou",
	9: "les deu",
	10: "les onze",
	11: "les dotze",
	12: "la una",
	13: "les dues",
	14: "les tres",
	15: "les quatre",
	16: "les cinc",
	17: "les sis",
	18: "les set",
	19: "les vuit",
	20: "les nou",
	21: "les deu",
	22: "les onze",
	23: "les dotze",
	24: "la una"
}

horacatalana = {
	0: lahora.get(hora) +  " en punt",
	1: lahora.get(hora) +  " i un minut",
	2: lahora.get(hora) +  " i dos minuts",
	3: lahora.get(hora) +  " i tres minuts",
	4: lahora.get(hora) +  " i quatre minuts",
	5: lahora.get(hora) +  " i cinc minuts",
	6: lahora.get(hora) +  " i sis minuts",
	7: "mig quart " + dehora.get(hora),
	8: lahora.get(hora) +  " i vuit minuts",
	9: lahora.get(hora) +  " i nou minuts",
	10: "d'aquí a cinc minuts serà un quart " + dehora.get(hora),
	11: "d'aquí a quatre minuts serà un quart " + dehora.get(hora),
	12: "d'aquí a tres minuts serà un quart " + dehora.get(hora),
	13: "d'aquí a dos minuts serà un quart " + dehora.get(hora),
	14: "d'aquí a un minut serà un quart " + dehora.get(hora),
	15: "un quart " + dehora.get(hora),
	16: "passa un minut d'un quart " + dehora.get(hora),
	17: "passen dos minuts d'un quart " + dehora.get(hora),
	18: "passen tres minuts d'un quart " + dehora.get(hora),
	19: "passen quatre minuts d'un quart " + dehora.get(hora),
	20: "passen cinc minuts d'un quart " + dehora.get(hora),
	21: "passen sis minuts d'un quart " + dehora.get(hora),
	22: "passen set minuts d'un quart " + dehora.get(hora),
	23: "passen vuit minuts d'un quart " + dehora.get(hora),
	24: "passen nou minuts d'un quart " + dehora.get(hora),
	25: "un quart " + dehora.get(hora) + " i deu minuts",
	26: "un quart " + dehora.get(hora) + " i onze minuts",
	27: "un quart " + dehora.get(hora) + " i dotze minuts",
	28: "un quart " + dehora.get(hora) + " i tretze minuts",
	29: "un quart " + dehora.get(hora) + " i catorze minuts",
	30: "dos quarts " + dehora.get(hora),
	31: "passa un minut de dos quarts " + dehora.get(hora),
	32: "passen dos minuts de dos quarts " + dehora.get(hora),
	33: "passen tres minuts de dos quarts " + dehora.get(hora),
	34: "passen quatre minuts de dos quarts " + dehora.get(hora),
	35: "passen cinc minuts de dos quarts " + dehora.get(hora),
	36: "passen sis minuts de dos quarts " + dehora.get(hora),
	37: "passen set minuts de dos quarts " + dehora.get(hora),
	38: "passen vuit minuts de dos quarts " + dehora.get(hora),
	39: "passen nou minuts de dos quarts " + dehora.get(hora),
	40: "dos quarts " + dehora.get(hora) + " i deu minuts",
	41: "dos quarts " + dehora.get(hora) + " i onze minuts",
	42: "dos quarts " + dehora.get(hora) + " i dotze minuts",
	43: "dos quarts " + dehora.get(hora) + " i tretze minuts",
	44: "dos quarts " + dehora.get(hora) + " i catorze minuts",
	45: "tres quarts " + dehora.get(hora),
	46: "passa un minut de tres quarts " + dehora.get(hora),
	47: "passen dos minuts de tres quarts " + dehora.get(hora),
	48: "passen tres minuts de tres quarts " + dehora.get(hora),
	49: "passen quatre minuts de tres quarts " + dehora.get(hora),
	50: "passen cinc minuts de tres quarts " + dehora.get(hora),
	51: "passen sis minuts de tres quarts " + dehora.get(hora),
	52: "passen set minuts de tres quarts " + dehora.get(hora),
	53: "passen vuit minuts de tres quarts " + dehora.get(hora),
	54: "passen nou minuts de tres quarts " + dehora.get(hora),
	55: "tres quarts " + dehora.get(hora) + " i deu minuts",
	56: "tres quarts " + dehora.get(hora) + " i onze minuts",
	57: "tres quarts " + dehora.get(hora) + " i dotze minuts",
	58: "tres quarts " + dehora.get(hora) + " i tretze minuts",
	59: "tres quarts " + dehora.get(hora) + " i catorze minuts"
}

mostrahora = horacatalana.get(minut, "ups! Hi ha hagut un error :(")

rand = random.randint(0,6)
if rand == 3:
	mastodon.status_post(mostrahora)
