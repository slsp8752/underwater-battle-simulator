import random




#	Monster Name Generator
#x = 0
#while x == 0:

#	adjectives = ["Wrathful", "Raspy", "Lamentable","Quaint","Cold", "Guiltless",
#	"Thick", "Living", "Nebulous", "Mysterious", "Bright", "Toothsome", "Far-flung",
#	"Disillusioned", "Apathetic", "Eldritch", "Vorpal"]

#	animals = ["Barnacle", "Dolphin", "Shark", "Whale", "Barracuda", "Cod",
#	"Squid", "Octopus", "Eel", "Shrimp", "Flounder", "Herring", "Jellyfish",
#	"Sponge", "Lobster"]

#	nouns = ["Doom", "Corruption", "Destruction", "Fondness", "Lard", 
#	"Seduction", "Drastic Proportions", "Sharpness", "Love", "Loathing", 
#	"Hatred", "Autocracy", "the Laundromat", "Worry", "Tickling"]

	
#	random_adjective = adjectives[random.randint(0,14)]
#	random_animal = animals[random.randint(0,14)]
#	random_noun = nouns[random.randint(0,14)]

#	name_format = random.randint(0,1)
	
#	if name_format == 0:
#		name = ("The " + random_adjective + " " + random_animal + " of " + random_noun)
	
#	else: 
		
#		an = random_adjective[0]
	
#		if an == "A" or an == "E" or an == "I" or an == "O" or an == "U":
#			name = ("An " + random_adjective + " " + random_animal)
		
#		else:
#			name = ("A " + random_adjective + " " + random_animal)
		

#	print(name)
#	input()

#


	
def generate_list(file_name):
	
	word_list = open(file_name, "r")
	
	words = []
	word_count = 0
	
	for line in word_list:
		line = line.strip("\n")
		line = line.split(", ")
		
		for value in line:
			words.append(value)
			word_count = word_count + 1
	
	
	return [words, (word_count-1)]

def monster_name():
	
	#	Name Generator - Convert into a text file and use file I/O.

	adjectives = generate_list("adjectives.txt")[0]
	adj_count = generate_list("adjectives.txt")[1]
	
	animals = generate_list("animals.txt")[0]
	ani_count = generate_list("animals.txt")[1]
		
	nouns = generate_list("nouns.txt")[0]
	noun_count = generate_list("nouns.txt")[1]
		
		
	random_adjective = adjectives[random.randint(0, adj_count)]
	random_animal = animals[random.randint(0, ani_count)]
	random_noun = nouns[random.randint(0, noun_count)]

	name_format = random.randint(0,1)
	
	if name_format == 0:
		name = ("The " + random_adjective + " " + random_animal + " of " + random_noun)
			
	else: 
		
		an = random_adjective[0]
	
		if an == "A" or an == "E" or an == "I" or an == "O" or an == "U":
			name = ("An " + random_adjective + " " + random_animal)
		
		else:
			name = ("A " + random_adjective + " " + random_animal)

	nickname = random_animal
	return(name)
x = 0

while x == 0:		

	input()
	name = monster_name()
	
	print(name)
	
