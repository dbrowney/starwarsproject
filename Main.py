# Donald Browney
# My Integration Project
# A Mad Lib story utilizing the opening crawls for Star Wars Episodes 1 through 9 preceded with a short quiz on Star Wars facts

# Credit is due to Leonard Stern and Roger Price who invented Mad Libs in 1953
# Opening crawls were taken directly from the Star Wars movies whose rights belong to Disney

# So far, coding help has only come from w3schools.com, class assignments, and the Mobile App "SoloLearn"

import time

def calculateDifficulty(num1, num2, num3):
    total = num1 + num2 + num3
    return total

def main():
    question_easy = (question6 + question7 + question9 + question10) * 5
    #print(question_easy) #used for testing purposes
    question_medium = (question3 + question5 + question8) * 9
    #print(question_medium) #used for testing purposes
    question_hard = (question1 + question2 + question4) * 15
    #print(question_hard) #used for testing purposes
    score = calculateDifficulty(question_easy, question_medium, question_hard)
    score *= 45
    print("Your Score =", score)
    
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

print("\n20,001 and above = THE CHOSEN ONE!")
print("15,001 to 20,000 = Jedi Master")
print("10,001 to 15,000 = Padawan")
print("5,001 to 10,000  = Youngling")
print("5,000 and below  = Force-sensitive\n")

main()

retryStory = "s"
while retryStory == "s":
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
        print(episode1_title + noun1.upper())
        print("\nTurmoil has engulfed the")
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
        noun1 = input("\nEnter a plural NOUN: ")
        num_adj1 = input("Enter any whole number greater than 1: ")
        verb1 = input("Enter a past tense VERB: ")
        verb2 = input("Enter a present tense VERB: ")
        adjective1 = input("Enter an ADJECTIVE: ")
        adjective2 = input("Enter another ADJECTIVE: ")
        adjective3 = input("Enter another ADJECTIVE: ")
        verb3 = input("Enter a present tense VERB: ")
        noun2 = input("Enter another plural NOUN: ")
        noun3 = input("Enter another plural NOUN: ")
        adjective4 = input("Enter another ADJECTIVE: ")
        verb4 = input("Enter a present tense VERB: ")
        adjective5 = input("Enter another ADJECTIVE: ")
        noun4 = input("Enter a singular NOUN: ")
        verb5 = input("Enter a present tense VERB: ")
        adjective6 = input("Enter another ADJECTIVE: ")
        print(episode2_title + noun1.upper())
        print("\nThere is unrest in the Galactic")
        print("Senate.", num_adj1, "solar")
        print("systems have", verb1, "their")
        print("intentions to", verb2, "the Republic.")
        print("\nThis", adjective1, "movement,")
        print("under the leadership of the")
        print(adjective2, "Count Dooku, has")
        print("made it difficult for the", adjective3)
        print("number of Jedi Knights to", verb3)
        print(noun2, "and", noun3, "in the galaxy.")
        print("\nSenator Amidala, the", adjective4)
        print("Queen of Naboo, is returning")
        print("to the Galactic Senate to", verb4)
        print("on the", adjective5, "issue of creating")
        print("a(n)", noun4.upper(), "OF THE REPUBLIC")
        print("to", verb5, "the", adjective6)
        print("Jedi....")
    elif num_choice == 3:
        episode3_title = "\nEpisode III \nREVENGE OF THE "
        noun1 = input("\nEnter a plural NOUN: ")
        noun2 = input("Enter another plural NOUN: ")
        adjective1 = input("Enter an ADJECTIVE: ")
        noun3 = input("Enter another plural NOUN: ")
        verb1 = input("Enter a present tense VERB ending in 's': ")
        adjective2 = input("Enter another ADJECTIVE: ")
        adjective3 = input("Enter another ADJECTIVE: ")
        verb2 = input("Enter a past tense VERB: ")
        verb3 = input("Enter another past tense VERB: ")
        noun4 = input("Enter a singular NOUN: ")
        noun5 = input("Enter another singular NOUN: ")
        adjective4 = input("Enter another ADJECTIVE: ")
        adjective5 = input("Enter another ADJECTIVE: ")
        noun6 = input("Enter another singular NOUN: ")
        num_adj1 = input("Enter any whole number greater than 1: ")
        noun7 = input("Enter another singular NOUN: ")
        adjective6 = input("Enter another ADJECTIVE: ")
        print(episode3_title + noun1.upper())
        print("\nWar! The Republic is crumbling")
        print("under", noun2, "by the", adjective1)
        print("Sith Lord, Count Dooku.")
        print("There are", noun3, "on both sides.")
        print("Evil", verb1, "everywhere.")
        print("\nIn a", adjective2, "move, the")
        print(adjective3, "droid leader, General")
        print("Grievous, has", verb2, "into the")
        print("Republic capital and", verb3)
        print("Chancellor Palpatine,", noun4, "of")
        print("the Galactic Senate.")
        print("\nAs the Separatist", noun5, "Army")
        print("attempts to flee the", adjective4)
        print("capital with their", adjective5)
        print(noun6 + ", " + num_adj1, "Jedi Knights lead a")
        print("desperate", noun7, "to rescue the")
        print(adjective6, "Chancellor....")        
    elif num_choice == 4:
        episode4_title = "\nEpisode IV \nA NEW "
        noun1 = input("Enter a singular NOUN: ")
            
        print(episode4_title + noun1.upper())
        print("\nIt is a period of civil war.")
        print("Rebel spaceships, striking")
        print("from a hidden base, have won")
        print("their first victory against")
        print("the evil Galactic Empire.")
        print("\nDuring the battle, Rebel")
        print("spies managed to steal secret")
        print("plans to the Empire's")
        print("ultimate weapon, the DEATH")
        print("STAR, an armored space")
        print("station with enough power to")
        print("destroy an entire planet.")
        print("\nPursued by the Empire's")
        print("sinister agents, Princess")
        print("Leia races home aboard her")
        print("starship, custodian of the")
        print("stolen plans that can save")
        print("her people and restore")
        print("freedom to the galaxy.....")
    elif num_choice == 5:
        episode5_title = "\nEpisode V \nTHE "
        episode5_title2 = "STRIKES BACK"
        noun1 = input("Enter a singular NOUN: ")

        print(episode5_title + noun1.upper() + episode5_title2)
        print("\nIt is a dark time for the")
        print("Rebellion. Although the Death")
        print("Star has been destroyed,")
        print("Imperial troops have driven the")
        print("Rebel forces from their hidden")
        print("base and pursued them across")
        print("the galaxy.")
        print("\nEvading the dreaded Imperial")
        print("Starfleet, a group of freedom")
        print("fighters led by Luke Skywalker")
        print("has established a new secret")
        print("base on the remote ice world")
        print("of Hoth.")
        print("\nThe evil lord Darth Vader,")
        print("obsessed with finding young")
        print("Skywalker, has dispatched")
        print("thousands of remote probes into")
        print("the far reaches of space....")
    elif num_choice == 6:
        episode6_title = "\nEpisode VI \nRETURN OF THE "
        noun1 = input("Enter a singular NOUN: ")
            
        print(episode6_title + noun1.upper())
        print("\nLuke Skywalker has returned to")
        print("his home planet of Tatooine in")
        print("an attempt to rescue his")
        print("friend Han Solo from the")
        print("clutches of the vile gangster")
        print("Jabba the Hutt.")
        print("\nLittle does Luke know that the")
        print("GALACTIC EMPIRE has secretly")
        print("begun construction on a new")
        print("armored space station even")
        print("more powerful than the first")
        print("dreaded Death Star.")
        print("\nWhen completed, this ultimate")
        print("weapon will spell certain doom")
        print("for the small band of rebels")
        print("struggling to restore freedom")
        print("to the galaxy....")
    elif num_choice == 7:
        episode7_title = "\nEpisode VII \nTHE "
        episode7_title2 = " AWAKENS"
        noun1 = input("Enter a singular NOUN: ")
            
        print(episode7_title + noun1.upper() + episode7_title2)
        print("\nLuke Skywalker has vanished.")
        print("In his absence, the sinister")
        print("FIRST ORDER has risen from")
        print("the ashes of the Empire")
        print("and will not rest until")
        print("Skywalker, the last Jedi,")
        print("has been destroyed.")
        print("\nWith the support of the")
        print("REPUBLIC, General Leia Organa")
        print("leads a brave RESISTANCE.")
        print("She is desperate to find her")
        print("brother Luke and gain his")
        print("help in restoring peace")
        print("and justice to the galaxy.")
        print("\nLeia has sent her most daring")
        print("pilot on a secret mission")
        print("to Jakku, where an old ally")
        print("has discovered a clue to")
        print("Luke's whereabouts....")
    elif num_choice == 8:
        episode8_title = "\nEpisode VIII \nTHE LAST "
        noun1 = input("\nEnter a singular NOUN: ")
        noun2 = input("Enter another singular NOUN: ")
        adjective1 = input("Enter an ADJECTIVE: ")
        lastName = input("Enter someone's last name: ")
        noun3 = input("Enter a plural NOUN: ")
        noun4 = input("Enter another singular NOUN: ")
        noun5 = input("Enter another plural NOUN: ")
        verb1 = input("Enter a present tense VERB: ")
        fullName = input("Enter someone's full name: ")
        noun6 = input("Enter a body part: ")
        noun7 = input("Enter another singular NOUN: ")
        verb2 = input("Enter a verb ending in 's': ")
        adjective2 = input("Enter another ADJECTIVE: ")
        adjective3 = input("Enter another ADJECTIVE: ")
        adjective4 = input("Enter another ADJECTIVE: ")  
        print(episode8_title + noun1.upper())
        print("\nThe FIRST", noun2.upper(), "reigns.")
        print("Having decimated the", adjective1)
        print("Republic, Supreme Leader", lastName.upper())
        print("now deploys the merciless")
        print(noun3, "to seize military")
        print("control of the", noun4 + ".")
        print("\nOnly General Leia Organa's")
        print("band of RESISTANCE", noun5)
        print(verb1, "against the rising")
        print("tyranny, certain that Jedi")
        print("Master", fullName.upper(), "will")
        print("return and restore a", noun6, "of")
        print("hope to the fight.")
        print("\nBut the Resistance has been")
        print("exposed. As the FIRST", noun7.upper())
        print(verb2, "toward the", adjective2, "base,")
        print("the", adjective3, "heroes mount a")
        print(adjective4, "escape....")
    elif num_choice == 9:
        episode9_title = "\nEpisdoe IX \nTHE RISE OF "
        lastName1 = input("\nEnter someone's last name: ")
        noun1 = input("Enter a plural NOUN: ")
        noun2 = input("Enter a singular NOUN: ")
        adjective1 = input("Enter an ADJECTIVE: ")
        adjective2 = input("Enter another ADJECTIVE: ")
        adjective3 = input("Enter another ADJECTIVE: ")
        lastName2 = input("Enter someone's last name: ")
        noun3 = input("Enter another plural NOUN: ")
        firstName = input("Enter someone's first name: ")
        noun4 = input("Enter another singular NOUN: ")
        adjective4 = input("Enter another ADJECTIVE: ")
        noun5 = input("Enter another singular NOUN: ")
        fullName = input("Enter someone's full name: ")
        noun6 = input("Enter another singular NOUN: ")
        noun7 = input("Enter another singular NOUN: ")
        print(episode9_title + lastName1.upper())
        print("\nThe", noun1, "speak! The", noun2, "has")
        print("heard a", adjective1, "broadcast,")
        print("a threat of REVENGE in the")
        print(adjective2, "voice of the", adjective3)
        print("EMPEROR", lastName2.upper() + ".")
        print("\nGENERAL LEIA ORGANA")
        print("dispatches secret", noun3, "to")
        print("gather intelligence, while", firstName.upper() + ",")
        print("the last", noun4, "of the Jedi, trains")
        print("for battle against the", adjective4)
        print("FIRST", noun5.upper() + ".")
        print("\nMeanwhile, Supreme Leader")
        print(fullName.upper(), "rages in search")
        print("of the phantom", noun6 + ",")
        print("determined to destroy any")
        print("threat to his/her", noun7 + "....")
    else:
        print("You have chosen the DARK SIDE OF THE FORCE!!!")
    retryStory = input("\nEnter 's' to try another story or any other key to quit: ")
print("\nMay the FORCE be with you!!!")
