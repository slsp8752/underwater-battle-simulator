
def start():
	# check for valid user input, restart if invalid. 
	user_input = input()
	
	if user_input == "p" or user_input == "P":
		print("\n")
		main()

	elif user_input == "i" or user_input == "I":
		print("\n")
		instructions()
		
	elif user_input == "q" or user_input == "Q":
		print("\n" + "Goodbye!")
	
	else:
		print("Invalid Input.")
		start()
		
def title():
	# Print a Dolphin for the Title Screen.
	print("                                   _________________ ")
	print("                                  |                 |")
	print(" Underwater Battle Simulator      |  Type P         |")
	print("                                  |        to Play  |")
	print("                   YAao,          |_________________|")
	print("                   Y8888b,                  \ /")
	print("                 ,oA8888888b,                V")
	print("             ,aaad8888888888888888bo,")
	print("          ,d888888888888888888888888888b,")
	print("        ,888888888888888888888888888888888b,")
	print("       d8888888888888888888888888888888888888,")
	print("      d888888888888888888888888888888888888888b")
	print("     d888888P'                    `Y888888888888,")
	print("     88888P'                    Ybaaaa8888888888l")
	print("    a8888'                      `Y8888P' `V888888")
	print("  d8888888a                                `Y8888")
	print(" AY/'' `\Y8b                                 ``Y8b")
	print(" Y'      `YP    [Type Q to Quit]")
	print("          `'         [Type I for Instructions]")
	
	start()

# Tell the user how to play the game.

def instructions():
	print("You're a tough warrior, and you like punching sharks!" + "\n"
	+ "Answer the prompts given to perform great feats of oceanic brutality!" + "\n"
	+ "Press enter to go back to the title screen.")
	input()
	title()

# The game

def main():
	
	import random

	# File I/O system for grabbing words from lists
	
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
	
	#	Name Generator - Takes words from 3 lists, combines them, and makes
	#	a variety of names for the monsters.

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
	
		#	For added variety, the names of the monster can either be
		#	The 'adjective' 'animal' of 'noun' (The Bright Sponge of Sharpness)
		#	or A/An 'adjective' 'animal' (A Raspy Trout)
	
		if name_format == 0:
			name = ("The " + random_adjective + " " + random_animal + " of " + random_noun)
			
		else: 
		
			an = random_adjective[0]
	
			if an == "A" or an == "E" or an == "I" or an == "O" or an == "U":
				name = ("An " + random_adjective + " " + random_animal)
		
			else:
				name = ("A " + random_adjective + " " + random_animal)
		nickname = random_animal
		
		return [name, nickname]

	#	start the game
	def	game():
	
		monster_hp = 0
	
		encounter(monster_hp)


#	set level and hp values, generate a monster, and ask the player 
#	what they want to do.

	def encounter(monster_hp):
	
		player_hp = 50
		
		monster_name_sep = monster_name()
		
		name = monster_name_sep[0]
	
		nickname = monster_name_sep[1]
	
		monster_level = random.randint(1, 11)

		hp_modifier = random.randint(-5, 5)

		monster_hp = (monster_level * 3 + hp_modifier)
			
		monster_attack_main = (monster_level + 5)
	
		if monster_hp < 0:
			print("You come across", name, "and its already dead. Good job, hero.")
	
		else:
			print("You cross paths with", name + "!")
			print("Level:",  monster_level, "HP:", monster_hp)
		
	
		while monster_hp > 0 and player_hp > 0:	
			
			print("\n")
			choice = input("Would you like to (a)ttack, do (n)othing, or (r)un? ")


			if choice == "A" or choice == "a":
			
				hps = combat(monster_hp, player_hp, monster_level, name, nickname)
				monster_hp = hps[0]
				player_hp = hps[1]
			
			elif choice == "N" or choice == "n":
				print("\n" + "You twiddle your thumbs a bit." + "\n")
				player_hp = monster_attack(player_hp, monster_level, name, nickname)
			
			elif choice == "R" or choice == "r":
				print("\n" + "You can't run underwater." + "\n")
				player_hp = monster_attack(player_hp, monster_level, name, nickname)
			
			else:
				print("Please select a valid choice.")
	
	
#	set up combat mechanics, ask player what kind of attack to do, decrease monster hp
#	and go to the monster attack phase
		
	def combat(monster_hp, player_hp, monster_level, name, nickname):
	
		player_attack_main = 7
	
		player_attack_modifier = random.randint(-6, 6)
	
		player_attack_special = (player_attack_main + player_attack_modifier)
	
		monster_block = random.randint(0, 7)
	
		block_check = monster_hp
	
		attack_type = input("Would you like to perform a (n)ormal or (s)pecial attack? ")
		
		# Normal Attack - Does a set amount of damage (7)
		
		if attack_type == "N" or attack_type == "n":
			print("\n")
	
			monster_hp = (monster_hp - player_attack_main) + monster_block
	
			if block_check == monster_hp:
				print("The attack was blocked completely!")
				print("The", nickname + "'s", "HP is still", monster_hp, "." + "\n")
			
			elif monster_block > 0:
				print("You deal some damage, but the", nickname, "defended itself a bit.")
				if monster_hp > 0:
					print("The", nickname + "'s", "HP is now", monster_hp, "." + "\n")
	
			else:
				print("You catch the", nickname, "completely off guard!")
				if monster_hp > 0:
					print("The", nickname + "'s", "HP is now", monster_hp, "." + "\n")


#	Speical attack - Does the base amount of damage + a random modifier
#	A bunch of if statements that make sure you know how much damage you've
#	done, or how pathetic you are. 
	
		elif attack_type == "S" or attack_type == "s":
			print("\n")
			if monster_block > monster_hp - player_attack_special:
				monster_hp = (monster_hp - player_attack_special)
			else:
				monster_hp = (monster_hp - player_attack_special) + (monster_block)
			
			if monster_block > 0 and player_attack_modifier < 0:
			
				print("The monster saw that coming from a mile away.\n\
Also, you tripped over your untied shoelace.")	
			
				if monster_hp > 0:
			
					if block_check == monster_hp:
						print("The", nickname + "'s", "HP is still", monster_hp, "." + "\n")
					else:
						print("The", nickname + "'s", "HP is now", monster_hp, "." + "\n")

			elif monster_block == 0 and player_attack_modifier <= 0:
				
				print("The monster wasn't paying attention, but your \
attack was pretty pathetic as well.")	
				
				if monster_hp > 0:
				
					print("The", nickname + "'s", "HP is now", monster_hp, "." + "\n")

			
			else:
			
				if monster_hp > 0:
				
					print("Not only was the monster oblivious, but you dealt \
massive damage! Tubular!")	
					print("The", nickname + "'s", "HP is now", monster_hp, "." + "\n")
	
	
		if monster_hp < 0:
			monster_dead(name)
			return [monster_hp, player_hp]
		else:
			player_hp = monster_attack(player_hp, monster_level, name, nickname)
			return [monster_hp, player_hp]
	
	#	The monster's attack phase, where a quaint eel can exact its
	#	revengeful duties upon the player. Pretty much identical to the 
	#	player's attack phase.

	def monster_attack(player_hp, monster_level, name, nickname):
	
	
		player_block = random.randint(0, 5)
		monster_attack_main = (monster_level + 5)
		monster_attack_modifier = random.randint(0, 4)
		monster_attack_selector = random.randint(0, 1)
		monster_attack_special = (monster_attack_main + monster_attack_modifier)
		block_check = player_hp
	
		if monster_attack_selector == 0:
				player_hp = (player_hp - monster_attack_main) + (player_block)
				if player_hp == block_check:
					print("You evaded the attack")
			
				else:
					print("The", nickname, "deals a swift blow!")
					if player_hp > 0:
						print("Your HP is now ", player_hp, ".")
		
		elif monster_attack_selector == 1 and monster_attack_modifier > 0:
			player_hp = (player_hp - monster_attack_special) + (player_block)
			print("The", nickname, "lands a massive attack!")
			if player_hp > 0:
				print("Your HP is now ", player_hp, ".")
	
		else:
			player_hp_a = (player_hp - monster_attack_special)
			print("The", nickname, "tries to do massive damage, but fails.")
			if player_hp > 0:
				print("Your HP is now ",player_hp, ".")
	
		if player_hp > 0:
			return player_hp
		
		else:
			player_dead(player_hp, name)
			return player_hp
	
	#	The monster is dead	

	def monster_dead(name):
		print("\n" + "You've slain", name + "!", "Loot its body and celebrate!")

	#	The player is dead

	def player_dead(player_hp, name):
		print(name, "completely obliterates you. You will be missed.")
		return player_hp

	
	game() # now that all that stuff is defined, actually run the game function
	
	print("\n")
	
	restart = 0
	
	#	Would you like to play again?
	
	while restart == 0:
		
		restart = input("Would you like to (r)eturn to the title screen, (q)uit, or" + "\n" + "(g)enerate random monster names? ")
		if restart == "r" or restart == "R":
			title()
		elif restart == "q" or restart == "Q":
			print("\n" + "Thanks for playing!")	
		
		elif restart == "g" or restart == "G":
			
			q = 0
			while q == 0:
				x = input("Press enter to generate a name, or type r to return to the title screen.")
				if x == "r" or x == "R":
					q = 1
					title()
				else:
					print("\n")
					name = monster_name()[0]
					print (name + "\n")
			
		else:
			restart = 0
			print("Invalid Input")
			
title()
