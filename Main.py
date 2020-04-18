"""
This is the main file for my integration project. My Integration Project is Mad
Lib story utilizing the opening crawls for Star Wars Episodes 1 through 9
preceded with a short quiz on Star Wars facts.

Credit is due to Leonard Stern and Roger Price who invented Mad Libs in 1953.

Opening crawls were taken directly from the Star Wars movies whose rights
belong to Disney.

Coding help has only come from w3schools.com, FGCU COP 1500 class assignments,
and the Mobile App "SoloLearn".
"""
__author__ = "Donald Browney"

import time


def intro():
    """
    Prints multiple lines of asterisks which together form the words 'STAR
    WARS'. It also prints an opening monologue.
    """
    print(
        "******** *********   *****   *********   *** *** ***   *****   "
        "********* ********")
    time.sleep(1)
    print(
        "******** ********* ***   *** ***   ***   *** *** *** ***   *** ***   "
        "*** ********")
    time.sleep(1)
    print(
        "***         ***    ***   *** ***   ***   *** *** *** ***   *** ***   "
        "*** ***     ")
    time.sleep(1)
    print(
        "********    ***    ********* *********   *** *** *** ********* "
        "********* ********")
    time.sleep(1)
    print(
        "********    ***    ********* ********    *** *** *** ********* "
        "********  ********")
    time.sleep(1)
    print(
        "     ***    ***    ***   *** *** ***     *** *** *** ***   *** *** "
        "***        ***")
    time.sleep(1)
    print(
        "********    ***    ***   *** ***  ***    *********** ***   *** ***  "
        "***  ********")
    time.sleep(1)
    print(
        "********    ***    ***   *** ***   ***   *********** ***   *** ***   "
        "*** ********")
    time.sleep(2)
    print("\nHELLO...and welcome to the newest story in the Star Wars saga!")
    time.sleep(2)
    print(
        "\nBefore we start we need to test and see if your midichlorian level "
        "is high enough!!!\n")
    time.sleep(3)


def quiz():
    """
    Prints 10 questions, one at a time, for the user to answer and also
    prints a message based on how they answered the question.
    :return: It returns the number of questions the user answered correctly.
    """
    quiz_questions = ["What is the first name of Boba Fett's father? ",
                      "What color was Jedi Master Mace Windu's lightsaber? ",
                      "What was Princess Leia's adopted last name? ",
                      "What type of crystal powers a lightsaber? ",
                      "Cloud City was a mining colony on what planet? ",
                      "What were the small, teddy bear-like creatures called "
                      "in 'Return of the Jedi'? ",
                      "What is the mysterious energy field created by life "
                      "that binds the galaxy together? The ",
                      "What is the Sith name for Emperor Palpatine? ",
                      "Luke Skywalker grew up on which planet? ",
                      "What is the name of Han Solo's starship? "]
    quiz_answers = ["jango", "purple", "organa", "kyber", "bespin", "ewoks",
                    "force", "darth sidious", "tatooine",
                    "millennium falcon"]

    num_correct = 0
    counter = 0

    for question in quiz_questions:
        user_answer = input(question)
        if user_answer.lower() == quiz_answers[counter]:
            print("Correct")
            num_correct += 1
        else:
            print("Incorrect")
        counter += 1
    return num_correct


def calculate_score(num1):
    """
    Calculates the total score based on correct number of questions.
    :param num1: The total number of correct questions from quiz
    :return: The total number of points.
    """
    points = num1 * 2100
    return points


def score_table():
    """
    Prints lines displaying the scoring structure.
    """
    print("\n20,001 and above = THE CHOSEN ONE!")
    print("15,001 to 20,000 = Jedi Master")
    print("10,001 to 15,000 = Padawan")
    print("5,001 to 10,000  = Youngling")
    print("5,000 and below  = Force-sensitive\n")


def main():
    """
    Runs the intro, quiz, and score table functions and also prints the
    user's final score.
    """
    intro()
    total_correct = quiz()
    score = calculate_score(total_correct)
    score_table()
    print("Your Score =", score)


main()

retry_story = "s"
while retry_story == "s":
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
        adjective1 = input("Enter an ADJECTIVE: ")
        verb1 = input("Enter a present tense VERB ending in 'ing': ")
        noun2 = input("Enter another singular NOUN: ")
        adjective2 = input("Enter another ADJECTIVE: ")
        noun3 = input("Enter a plural NOUN: ")
        noun4 = input("Enter another plural NOUN: ")
        adjective3 = input("Enter another ADJECTIVE: ")
        noun5 = input("Enter another singular NOUN: ")
        noun6 = input("Enter another singular NOUN: ")
        noun7 = input("Enter another singular NOUN: ")
        noun8 = input("Enter another plural NOUN: ")
        first_name = input("Enter someone's first name: ")
        noun9 = input("Enter another singular NOUN: ")
        noun10 = input("Enter another plural NOUN: ")
        print(episode4_title + noun1.upper())
        print("\nIt is a period of civil war.")
        print(adjective1, "spaceships,", verb1)
        print("from a hidden", noun2 + ", have won")
        print("their first victory against")
        print("the", adjective2, "Galactic Empire.")
        print("\nDuring the battle, Rebel")
        print(noun3, "managed to steal secret")
        print(noun4, "to the Empire's")
        print(adjective3, "weapon, the DEATH")
        print(noun5.upper() + ", an armored space")
        print(noun6, "with enough power to")
        print("destroy an entire", noun7 + ".")
        print("\nPursued by the Empire's")
        print("sinister", noun8 + ", Princess")
        print(first_name, "races home aboard her")
        print(noun9 + ", custodian of the")
        print("stolen", noun4, "that can save")
        print("her", noun10, "and restore")
        print("freedom to the galaxy.....")
    elif num_choice == 5:
        episode5_title = "\nEpisode V \nTHE "
        episode5_title2 = " STRIKES BACK"
        noun1 = input("Enter a singular NOUN: ")
        adjective1 = input("Enter an ADJECTIVE: ")
        adjective2 = input("Enter another ADJECTIVE: ")
        verb1 = input("Enter a past tense VERB ending in 'ed': ")
        noun2 = input("Enter a plural NOUN: ")
        noun3 = input("Enter another plural NOUN: ")
        noun4 = input("Enter another singular NOUN: ")
        verb2 = input("Enter another past tense VERB ending in 'ed': ")
        adjective3 = input("Enter another ADJECTIVE: ")
        adjective4 = input("Enter another ADJECTIVE: ")
        first_name = input("Enter someone's first name: ")
        last_name1 = input("Enter someone's last name: ")
        adjective5 = input("Enter another ADJECTIVE: ")
        adjective6 = input("Enter another ADJECTIVE: ")
        last_name2 = input("Enter someone's last name: ")
        noun5 = input("Enter another plural NOUN: ")
        print(episode5_title + noun1.upper() + episode5_title2)
        print("\nIt is a", adjective1, "time for the")
        print("Rebellion. Although the", adjective2)
        print("Star has been", verb1 + ",")
        print("Imperial", noun2, "have driven the")
        print("Rebel", noun3, "from their hidden")
        print(noun4, "and", verb2, "them across")
        print("the galaxy.")
        print("\nEvading the", adjective3, "Imperial")
        print("Starfleet, a group of", adjective4)
        print("fighters led by", first_name, last_name1)
        print("has established a new", adjective5)
        print("base on the", adjective6, "ice world")
        print("of Hoth.")
        print("\nThe evil lord Darth", last_name2 + ",")
        print("obsessed with finding young")
        print(last_name1 + ", has dispatched")
        print("thousands of remote", noun5, "into")
        print("the far reaches of space....")
    elif num_choice == 6:
        episode6_title = "\nEpisode VI \nRETURN OF THE "
        noun1 = input("Enter a singular NOUN: ")
        first_name1 = input("Enter someone's first name: ")
        last_name = input("Enter someone's last name: ")
        adjective1 = input("Enter an ADJECTIVE: ")
        full_name = input("Enter someone's full name: ")
        first_name2 = input("Enter someone's first name: ")
        noun2 = input("Enter another singular NOUN: ")
        noun3 = input("Enter another singular NOUN: ")
        adjective2 = input("Enter another ADJECTIVE: ")
        noun4 = input("Enter another singular NOUN: ")
        verb1 = input("Enter a past tense VERB ending in 'ed': ")
        adjective3 = input("Enter another ADJECTIVE: ")
        noun5 = input("Enter a plural NOUN: ")
        verb2 = input("Enter a present tense VERB ending in 'ing': ")
        print(episode6_title + noun1.upper())
        print("\n" + first_name1, last_name, "has returned to")
        print("his home planet of Tatooine in")
        print("an attempt to rescue his")
        print("friend", full_name, "from the")
        print("clutches of the", adjective1, "gangster")
        print(first_name2, "the Hutt.")
        print("\nLittle does", first_name1, "know that the")
        print("GALACTIC", noun2.upper(), "has secretly")
        print("begun construction on a new")
        print("armored space", noun3, "even")
        print("more powerful than the first")
        print(adjective2, "Death", noun4 + ".")
        print("\nWhen", verb1 + ", this ultimate")
        print("weapon will spell certain doom")
        print("for the", adjective3, "band of", noun5)
        print(verb2, "to restore freedom")
        print("to the galaxy....")
    elif num_choice == 7:
        episode7_title = "\nEpisode VII \nTHE "
        episode7_title2 = " AWAKENS"
        noun1 = input("Enter a singular NOUN: ")
        first_name1 = input("Enter someone's first name: ")
        last_name1 = input("Enter someone's last name: ")
        noun2 = input("Enter another singular NOUN: ")
        noun3 = input("Enter a plural NOUN: ")
        adjective1 = input("Enter an ADJECTIVE: ")
        verb1 = input("Enter a past tense VERB ending in 'ed': ")
        first_name2 = input("Enter someone's first name: ")
        last_name2 = input("Enter someone's last name: ")
        adjective2 = input("Enter another ADJECTIVE: ")
        noun4 = input("Enter another singular NOUN: ")
        noun5 = input("Enter another plural NOUN: ")
        noun6 = input("Enter another singular NOUN: ")
        adjective3 = input("Enter another ADJECTIVE: ")
        noun7 = input("Enter another singular NOUN: ")
        print(episode7_title + noun1.upper() + episode7_title2)
        print("\n" + first_name1, last_name1, "has vanished.")
        print("In his absence, the sinister")
        print("FIRST", noun2.upper(), "has risen from")
        print("the", noun3, "of the Empire")
        print("and will not rest until")
        print(last_name1 + ", the", adjective1, "Jedi,")
        print("has been", verb1 + ".")
        print("\nWith the support of the")
        print("REPUBLIC, General", first_name2, last_name2)
        print("leads a", adjective2, "RESISTANCE.")
        print("She is desperate to find her")
        print(noun4, first_name1, "and gain his")
        print("help in restoring peace")
        print("and", noun5, "to the galaxy.")
        print("\n" + first_name2, "has sent her most daring")
        print(noun6, "on a", adjective3, "mission")
        print("to Jakku, where an old", noun7)
        print("has discovered a clue to")
        print(first_name1 + "'s whereabouts....")
    elif num_choice == 8:
        episode8_title = "\nEpisode VIII \nTHE LAST "
        noun1 = input("\nEnter a singular NOUN: ")
        noun2 = input("Enter another singular NOUN: ")
        adjective1 = input("Enter an ADJECTIVE: ")
        last_name = input("Enter someone's last name: ")
        noun3 = input("Enter a plural NOUN: ")
        noun4 = input("Enter another singular NOUN: ")
        noun5 = input("Enter another plural NOUN: ")
        verb1 = input("Enter a present tense VERB: ")
        full_name = input("Enter someone's full name: ")
        noun6 = input("Enter a body part: ")
        noun7 = input("Enter another singular NOUN: ")
        verb2 = input("Enter a verb ending in 's': ")
        adjective2 = input("Enter another ADJECTIVE: ")
        adjective3 = input("Enter another ADJECTIVE: ")
        adjective4 = input("Enter another ADJECTIVE: ")
        print(episode8_title + noun1.upper())
        print("\nThe FIRST", noun2.upper(), "reigns.")
        print("Having decimated the", adjective1)
        print("Republic, Supreme Leader", last_name.upper())
        print("now deploys the merciless")
        print(noun3, "to seize military")
        print("control of the", noun4 + ".")
        print("\nOnly General Leia Organa's")
        print("band of RESISTANCE", noun5)
        print(verb1, "against the rising")
        print("tyranny, certain that Jedi")
        print("Master", full_name.upper(), "will")
        print("return and restore a", noun6, "of")
        print("hope to the fight.")
        print("\nBut the Resistance has been")
        print("exposed. As the FIRST", noun7.upper())
        print(verb2, "toward the", adjective2, "base,")
        print("the", adjective3, "heroes mount a")
        print(adjective4, "escape....")
    elif num_choice == 9:
        episode9_title = "\nEpisode IX \nTHE RISE OF "
        last_name1 = input("\nEnter someone's last name: ")
        noun1 = input("Enter a plural NOUN: ")
        noun2 = input("Enter a singular NOUN: ")
        adjective1 = input("Enter an ADJECTIVE: ")
        adjective2 = input("Enter another ADJECTIVE: ")
        adjective3 = input("Enter another ADJECTIVE: ")
        last_name2 = input("Enter someone's last name: ")
        noun3 = input("Enter another plural NOUN: ")
        first_name = input("Enter someone's first name: ")
        noun4 = input("Enter another singular NOUN: ")
        adjective4 = input("Enter another ADJECTIVE: ")
        noun5 = input("Enter another singular NOUN: ")
        full_name = input("Enter someone's full name: ")
        noun6 = input("Enter another singular NOUN: ")
        noun7 = input("Enter another singular NOUN: ")
        print(episode9_title + last_name1.upper())
        print("\nThe", noun1, "speak! The", noun2, "has")
        print("heard a", adjective1, "broadcast,")
        print("a threat of REVENGE in the")
        print(adjective2, "voice of the", adjective3)
        print("EMPEROR", last_name2.upper() + ".")
        print("\nGENERAL LEIA ORGANA")
        print("dispatches secret", noun3, "to")
        print("gather intelligence, while", first_name.upper() + ",")
        print("the last", noun4, "of the Jedi, trains")
        print("for battle against the", adjective4)
        print("FIRST", noun5.upper() + ".")
        print("\nMeanwhile, Supreme Leader")
        print(full_name.upper(), "rages in search")
        print("of the phantom", noun6 + ",")
        print("determined to destroy any")
        print("threat to his/her", noun7 + "....")
    else:
        print("You have chosen the DARK SIDE OF THE FORCE!!!")
    retry_story = input(
        "\nEnter 's' to try another story or any other key to quit: ")
print("\nMay the FORCE be with you!!!")
