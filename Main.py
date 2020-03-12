# Donald Browney
# My Integration Project
# A Mad Lib story utilizing the opening crawls for Star Wars Episodes 1 through 9 preceded with a short quiz on Star Wars facts

# Credit is due to Leonard Stern and Roger Price who invented Mad Libs in 1953
# Opening crawls were taken directly from the Star Wars movies whose rights belong to Disney

# So far, coding help has only come from w3schools.com, class assignments, and the Mobile App "SoloLearn"

#import os
#os.startfile("C:\\Users\\Browney\\Desktop\\starwars.mp3")

import time
print("******** *********   *****   *********   *** *** ***   *****   ********* ********")
time.sleep(1)
print("******** ********* ***   *** ***   ***   *** *** *** ***   *** ***   *** ********")
time.sleep(1)
print("***         ***    ***   *** ***   ***   *** *** *** ***   *** ***   *** ***     ")
time.sleep(1)
print("********    ***    ********* *********   *** *** *** ********* ********* ********")
time.sleep(1)
print("********    ***    ********* ********    *** *** *** ********* ********  ********")
time.sleep(1)
print("     ***    ***    ***   *** *** ***     *** *** *** ***   *** *** ***        ***")
time.sleep(1)
print("********    ***    ***   *** ***  ***    *********** ***   *** ***  ***  ********")
time.sleep(1)
print("********    ***    ***   *** ***   ***   *********** ***   *** ***   *** ********")
time.sleep(2)

print("\nHELLO...and welcome to the newest story in the Star Wars saga!")
time.sleep(2)
print("\nBefore we start we need to test and see if your midichlorian level is high enough!!!\n")
time.sleep(3)
question1 = input("What is the first name of Boba Fett's father? ")
answer1 = "JANGO"
if question1.upper() == answer1:
    print("Correct")
    question1 = 5
else:
    print("Incorrect")
    question1 = 0
question2 = input("What color was Jedi Master Mace Windu's lightsaber? ")
answer2 = "PURPLE"
if question2.upper() == answer2:
    print("Correct")
    question2 = 5
else:
    print("Incorrect")
    question2 = 0
question3 = input("What was Princess Leia's adopted last name? ")
answer3 = "ORGANA"
if question3.upper() == answer3:
    print("Correct")
    question3 = 5
else:
    print("Incorrect")
    question3 = 0
question4 = input("What type of crystal powers a lightsaber? ")
answer4 = "KYBER"
if question4.upper() == answer4:
    print("Correct")
    question4 = 5
else:
    print("Incorrect")
    question4 = 0
question5 = input("Cloud City was a mining colony on what planet? ")
answer5 = "BESPIN"
if question5.upper() == answer5:
    print("Correct")
    question5 = 5
else:
    print("Incorrect")
    question5 = 0
question6 = input("What were the small, teddy bear-like creatures called in 'Return of the Jedi'? ")
answer6 = "EWOKS"
if question6.upper() == answer6:
    print("Correct")
    question6 = 5
else:
    print("Incorrect")
    question6 = 0
question7 = input("What is the mysterious energy field created by life that binds the galaxy together? ")
answer7_1 = "THE FORCE"
answer7_2 = "FORCE"
if question7.upper() == answer7_1:
    print("Correct")
    question7 = 5
elif question7.upper() == answer7_2:
    print("Correct")
    question7 = 5
else:
    print("Incorrect")
    question7 = 0
question8 = input("What is the Sith name for Emperor Palpatine? ")
answer8 = "DARTH SIDIOUS"
if question8.upper() == answer8:
    print("Correct")
    question8 = 5
else:
    print("Incorrect")
    question8 = 0
question9 = input("Luke Skywalker grew up on which planet? ")
answer9 = "TATOOINE"
if question9.upper() == answer9:
    print("Correct")
    question9 = 5
else:
    print("Incorrect")
    question9 = 0
question10 = input("What is the name of Han Solo's starship? ")
answer10 = "MILLENIUM FALCON"
if question10.upper() == answer10:
    print("Correct")
    question10 = 5
else:
    print("Incorrect")
    question10 = 0

question_easy = (question6 + question7 + question9 + question10) * 5
#print(question_easy) #used for testing purposes
question_medium = (question3 + question5 + question8) * 9
#print(question_medium) #used for testing purposes
question_hard = (question1 + question2 + question4) * 15
#print(question_hard) #used for testing purposes

test1 = question_easy + question_medium + question_hard
#print(test1) #used for testing purposes
test1 *= 45
#print(test1) #used for testing purposes
print("\n20,001 and above = THE CHOSEN ONE!")
print("15,001 to 20,000 = Jedi Master")
print("10,001 to 15,000 = Padawan")
print("5,001 to 10,000  = Youngling")
print("5,000 and below  = Force-sensitive\n")
print("Your Score =", test1)

retryStory = "s"
while retryStory == "s":
    if test1 >= 0: # thinking about a way to only allow certain number inputs depending on test results
        print("\nChoose your adventure carefully and may the Force be with you!")
        num_choice = int(input("Pick a whole number from 1-9: "))
        if num_choice == 1:
            episode1_title = "\nEpisode I \nTHE PHANTOM "
            noun1 = input("\nEnter a singular NOUN: ")
            noun2 = input("Enter another singular NOUN: ")
            adjective1 = input("Enter an ADJECTIVE: ")
            adjective2 = input("Enter another ADJECTIVE: ")
            noun3 = input("Enter a plural NOUN: ")
            adjective3 = input("Enter another ADJECTIVE: ")
            verb1 = input("Enter a past tense VERB: ")
            noun4 = input("Enter another plural NOUN: ")
            adverb1 = input("Enter an ADVERB: ")
            verb2 = input("Enter a present tense VERB: ")
            adjective4 = input("Enter another ADJECTIVE: ")
            noun5 = input("Enter another plural NOUN: ")
            adjective5 = input("Enter another ADJECTIVE: ")
            verb3 = input("Enter a past tense VERB: ")
            num_adj1 = input("Enter any whole number greater than 1: ")
            noun6 = input("Enter another plural NOUN: ")
            noun7 = input("Enter another plural NOUN: ")
            print(episode1_title + noun1)
            print("Turmoil has engulfed the")
            print("Galactic", noun2 + ".", "The taxation")
            print("of", adjective1, "routes to outlying", adjective2)
            print("systems is in dispute.")
            print("\nHoping to resolve the matter")
            print("with a blockade of deadly")
            print(noun3 + ",", "the", adjective3, "Trade")
            print("Federation has", verb1, "all")
            print(noun4, "to the", adjective4, "planet")
            print("of Naboo.")
            print("\nWhile the Congress of the")
            print("Republic", adverb1, verb2)
            print("this alarming chain of", noun5 + ",")
            print("the", adjective5, "Chancellor has")
            print("secretly", verb3, num_adj1, "Jedi")
            print("Knights, the guardians of")
            print(noun6, "and", noun7, "in the")
            print("galaxy, to settle the conflict....")
        elif num_choice == 2:
            episode2_title = "\nEpisode II \nATTACK OF THE "
            noun8 = input("\nEnter a plural NOUN: ")
            num_adj2 = input("Enter any whole number greater than 1: ")
            verb4 = input("Enter a past tense VERB: ")
            verb5 = input("Enter a present tense VERB: ")
            adjective6 = input("Enter an ADJECTIVE: ")
            adjective7 = input("Enter another ADJECTIVE: ")
            adjective8 = input("Enter another ADJECTIVE: ")
            verb6 = input("Enter a present tense VERB: ")
            noun9 = input("Enter another plural NOUN: ")
            noun10 = input("Enter another plural NOUN: ")
            adjective9 = input("Enter another ADJECTIVE: ")
            verb7 = input("Enter a present tense VERB: ")
            adjective10 = input("Enter another ADJECTIVE: ")
            noun11 = input("Enter a singular NOUN: ")
            verb8 = input("Enter a present tense VERB: ")
            adjective11 = input("Enter another ADJECTIVE: ")
            print(episode2_title + noun8)
            print("There is unrest in the Galactic")
            print("Senate.", num_adj2, "solar")
            print("systems have", verb4, "their")
            print("intentions to", verb5, "the Republic.")
            print("\nThis", adjective6, "movement,")
            print("under the leadership of the")
            print(adjective7, "Count Dooku, has")
            print("made it difficult for the", adjective8)
            print("number of Jedi Knights to", verb6)
            print(noun9, "and", noun10, "in the galaxy.")
            print("\nSenator Amidala, the", adjective9)
            print("Queen of Naboo, is returning")
            print("to the Galactic Senate to", verb7)
            print("on the", adjective10, "issue of creating")
            print("a(n)", noun11, "OF THE REPUBLIC")
            print("to", verb8, "the", adjective11)
            print("Jedi....")
        elif num_choice == 3:
            episode3_title = "\nEpisode III \nREVENGE OF THE "
            noun12 = input("\nEnter a plural NOUN: ")
            noun13 = input("Enter another plural NOUN: ")
            adjective12 = input("Enter an ADJECTIVE: ")
            noun14 = input("Enter another plural NOUN: ")
            verb9 = input("Enter a present tense VERB ending in 's': ")
            adjective13 = input("Enter another ADJECTIVE: ")
            adjective14 = input("Enter another ADJECTIVE: ")
            verb10 = input("Enter a past tense VERB: ")
            verb11 = input("Enter another past tense VERB: ")
            noun15 = input("Enter a singular NOUN: ")
            noun16 = input("Enter another singular NOUN: ")
            adjective15 = input("Enter another ADJECTIVE: ")
            adjective16 = input("Enter another ADJECTIVE: ")
            noun17 = input("Enter another singular NOUN: ")
            num_adj3 = input("Enter any whole number greater than 1: ")
            noun18 = input("Enter another singular NOUN: ")
            adjective17 = input("Enter another ADJECTIVE: ")
            print(episode3_title + noun12)
            print("War! The Republic is crumbling")
            print("under", noun13, "by the", adjective12)
            print("Sith Lord, Count Dooku.")
            print("There are", noun14, "on both sides.")
            print("Evil", verb9, "everywhere.")
            print("\nIn a", adjective13, "move, the")
            print(adjective14, "droid leader, General")
            print("Grievous, has", verb10, "into the")
            print("Republic capital and", verb11)
            print("Chancellor Palpatine,", noun15, "of")
            print("the Galactic Senate.")
            print("\nAs the Separatist", noun16, "Army")
            print("attempts to flee the", adjective15)
            print("capital with their", adjective16)
            print(noun17 + ", " + num_adj3, "Jedi Knights lead a")
            print("desperate", noun18, "to rescue the")
            print(adjective17, "Chancellor....")        
        elif num_choice == 4:
            episode4_title = "\nEpisode IV"
            print("Work in progress")
            #Episode IV
            #A NEW HOPE
            #It is a period of civil war.
            #Rebel spaceships, striking
            #from a hidden base, have won
            #their first victory against
            #the evil Galactic Empire.

            #During the battle, Rebel
            #spies managed to steal secret
            #plans to the Empire's
            #ultimate weapon, the DEATH
            #STAR, an armored space
            #station with enough power to
            #destroy an entire planet.

            #Pursued by the Empire's
            #sinister agents, Princess
            #Leia races home aboard her
            #starship, custodian of the
            #stolen plans that can save
            #her people and restore
            #freedom to the galaxy.....
        elif num_choice == 5:
            episode5_title = "\nEpisode V"
            print("Work in progress")
            #Episode V
            #THE EMPIRE STRIKES BACK
            #It is a dark time for the
            #Rebellion. Although the Death
            #Star has been destroyed,
            #Imperial troops have driven the
            #Rebel forces from their hidden
            #base and pursued them across
            #the galaxy.

            #Evading the dreaded Imperial
            #Starfleet, a group of freedom
            #fighters led by Luke Skywalker
            #has established a new secret
            #base on the remote ice world
            #of Hoth.

            #The evil lord Darth Vader,
            #obsessed with finding young
            #Skywalker, has dispatched
            #thousands of remote probes into
            #the far reaches of space....
        elif num_choice == 6:
            episode6_title = "\nEpisode VI \nRETURN OF THE "
            print("Work in progress")
            #Episode VI
            #RETURN OF THE JEDI
            #Luke Skywalker has returned to
            #his home planet of Tatooine in
            #an attempt to rescue his
            #friend Han Solo from the
            #clutches of the vile gangster
            #Jabba the Hutt.

            #Little does Luke know that the
            #GALACTIC EMPIRE has secretly
            #begun construction on a new
            #armored space station even
            #more powerful than the first
            #dreaded Death Star.

            #When completed, this ultimate
            #weapon will spell certain doom
            #for the small band of rebels
            #struggling to restore freedom
            #to the galaxy....
        elif num_choice == 7:
            episode7_title = "\nEpisode VII"
            print("Work in progress")
            #Episode VII
            #THE FORCE AWAKENS
            #Luke Skywalker has vanished.
            #In his absence, the sinister
            #FIRST ORDER has risen from
            #the ashes of the Empire
            #and will not rest until
            #Skywalker, the last Jedi,
            #has been destroyed.

            #With the support of the
            #REPUBLIC, General Leia Organa
            #leads a brave RESISTANCE.
            #She is desperate to find her
            #brother Luke and gain his
            #help in restoring peace
            #and justice to the galaxy.

            #Leia has sent her most daring
            #pilot on a secret mission
            #to Jakku, where an old ally
            #has discovered a clue to
            #Luke's whereabouts....
        elif num_choice == 8:
            episode8_title = "\nEpisode VIII \nTHE LAST "
            print("Work in progress")
            #Episode VIII
            #THE LAST JEDI
            #The FIRST ORDER reigns.
            #Having decimated the peaceful
            #Republic, Supreme Leader Snoke
            #now deploys the merciless
            #legions to seize military
            #control of the galaxy.

            #Only General Leia Organa's
            #band of RESISTANCE fighters
            #stand against the rising
            #tyranny, certain that Jedi
            #Master Luke Skywalker will
            #return and restore a spark of
            #hope to the fight.

            #But the Resistance has been
            #exposed. As the First Order
            #speeds toward the rebel base,
            #the brave heroes mount a
            #desperate escape....
        elif num_choice == 9:
            episode9_title = "\nEpisdoe IX \nTHE RISE OF "
            print("Work in progress")
            #Episode IX
            #THE RISE OF SKYWALKER
            #The dead speak! The galaxy has
            #heard a mysterious broadcast,
            #a threat of REVENGE in the
            #sinister voice of the late
            #EMPEROR PALPATINE.

            #GENERAL LEIA ORGANA
            #dispatches secret agents to
            #gather intelligence, while REY,
            #the last hope of the Jedi, trains
            #for battle against the diabolical
            #FIRST ORDER.

            #Meanwhile, Supreme Leader
            #KYLO REN rages in search
            #of the phantom Emperor,
            #determined to destroy any
            #threat to his power....
        else:
            print("You have chosen the DARK SIDE OF THE FORCE!!!")
    retryStory = input("\nEnter 's' to try another story: ")
print("\nMay the FORCE be with you!!!")
