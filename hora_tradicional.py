import datetime

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
	17: "les cinc",
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

def un(horaara):
	if horaara == 1:
		return lahora.get(horaara) + " tocada"
	elif horaara == 13:
		return lahora.get(horaara) + " tocada"
	else:
		return lahora.get(horaara) + " tocades"

def tres(horaara):
	if horaara == 1:
		return lahora.get(horaara) + " ben tocada"
	elif horaara == 13:
		return lahora.get(horaara) + " ben tocada"
	else:
		return lahora.get(horaara) + " ben tocades"

def horatradicional():
	#esbrina la hora
	now= datetime.datetime.now()
	hora = now.hour
	minut = now.minute

	horacatalana = {
		0: lahora.get(hora) + " en punt",
		1: un(hora),
		2: un(hora),
		3: tres(hora),
		4: "gairebé " + lahora.get(hora) + " i cinc",
		5: lahora.get(hora) + " i cinc",
		6: "vora mig quart " + dehora.get(hora),
		7: "mig quart " + dehora.get(hora),
		8: "mig quart " + dehora.get(hora),
		9: "gairebé " + lahora.get(hora) + " i deu",
		10: lahora.get(hora) + " i deu",
		11: "vora un quart " + dehora.get(hora),
		12: "vora un quart " + dehora.get(hora),
		13: "vora un quart " + dehora.get(hora),
		14: "gairebé un quart " + dehora.get(hora),
		15: "un quart " + dehora.get(hora),
		16: "un quart tocat " + dehora.get(hora),
		17: "un quart tocat " + dehora.get(hora),
		18: "un quart ben tocat " + dehora.get(hora),
		19: "gairebé un quart i cinc [" + dehora.get(hora) + "]",
		20: "un quart i cinc [" + dehora.get(hora) + "]",
		21: "vora un quart i mig " + dehora.get(hora),
		22: "un quart i mig " + dehora.get(hora),
		23: "un quart i mig " + dehora.get(hora),
		24: "gairebé un quart i deu [" + dehora.get(hora) + "]",
		25: "un quart i deu [" + dehora.get(hora) + "]",
		26: "vora dos quarts " + dehora.get(hora),
		27: "vora dos quarts " + dehora.get(hora),
		28: "vora dos quarts " + dehora.get(hora),
		29: "gairebé dos quarts " + dehora.get(hora),
		30: "dos quarts " + dehora.get(hora),
		31: "dos quarts tocats " + dehora.get(hora),
		32: "dos quarts tocats " + dehora.get(hora),
		33: "dos quarts ben tocats " + dehora.get(hora),
		34: "gairebé dos quarts i cinc [" + dehora.get(hora) + "]",
		35: "dos quarts i cinc [" + dehora.get(hora) + "]",
		36: "vora dos quarts i mig " + dehora.get(hora),
		37: "dos quarts i mig " + dehora.get(hora),
		38: "gairebé dos quarts i deu [" + dehora.get(hora) + "]",
		39: "gairebé dos quarts i deu [" + dehora.get(hora) + "]",
		40: "dos quarts i deu [" + dehora.get(hora) + "]",
		41: "vora tres quarts " + dehora.get(hora),
		42: "vora tres quarts " + dehora.get(hora),
		43: "vora tres quarts " + dehora.get(hora),
		44: "gairebé tres quarts " + dehora.get(hora),
		45: "tres quarts " + dehora.get(hora),
		46: "tres quarts tocats " + dehora.get(hora),
		47: "tres quarts tocats " + dehora.get(hora),
		48: "tres quarts ben tocats " + dehora.get(hora),
		49: "gairebé tres quarts i cinc [" + dehora.get(hora) + "]",
		50: "tres quarts i cinc [" + dehora.get(hora) + "]",
		51: "vora tres quarts i mig " + dehora.get(hora),
		52: "tres quarts i mig " + dehora.get(hora),
		53: "tres quarts i mig " + dehora.get(hora),
		54: "gairebé tres quarts i deu [" + dehora.get(hora) + "]",
		55: "tres quarts i deu [" + dehora.get(hora) + "]",
		56: "vora " + lahorames.get(hora),
		57: "vora " + lahorames.get(hora),
		58: "vora " + lahorames.get(hora),
		59: "a punt de tocar " + lahorames.get(hora)
	}

	return horacatalana.get(minut, "ups! Hi ha hagut un error :(")
