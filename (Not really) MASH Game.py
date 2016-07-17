##Gives a random set of "future outcomes" that's affected by the user's input
from random import *
a = randint(1, 4)   #helps decide random outcome
user_input = []
##User's input affects the "fate" stat, changing the type of outcome they recieve
# 0= neutral outcome
# 1= good outcome
# -1= bad outcome
fate = 0
## Introduction (not essential)
name = input("Welcome to the 100% Legit and Scam-Free Gaurenteed Fortune Telling Software (trial version) Please enter your name now")
creditcard = input("Hello "+name+" Unfortuantely there is no trial version and you must pay now. Enter your credit card number")
user_input.append(name)
user_input.append(creditcard)
print("Thank you for your information! You now have the full version of Fortune Teller! Now, I am not your usual fortune teller. Say anything that I particularly do not like and your fortune may be adversely affected...")
##Gathering user input
color = input("What's your favorite color?")
food = input("Favorite Food?")
number = input("Favorite Number?")
##Listing possible outcomes. "Bad" and "Good" Outcomes for each category have their own lists.
bad_building = ["a cardboard box", "an apartment in North Korea", "Trump Towers (but must sleep with Trump", "a barn house"]
good_building = ["Trump Towers (you can rename it)", "Bill Gate's Mansion", "a summer house out on Hawaii","a floating fortress"]
bad_job = ["a harbage man!","a truck driver","a Trump employee","Mr. Bean's special helper"]
good_job = ["ruler of the world", "CEO of Windows", "Supreme Ruler of the Universe", "God"]
bad_mate = ["no one","a dog","a kkeleton","a flower"]
good_mate = ["this year's Miss America", "the hottest model in the world", "anyone you like", "your crush"]
bad_offspring = ["a mutant","the Devil","a monster","nothing"]
good_offspring = ["so many children that you could literally make your own country", "the smartest kid in the world", "Dat Boi", "Karate Kid"]
##Lists of replies that trigger a change to "fate" variable (As of now only changes fate to -1)
trigger_for_color = ["Red","Blue","Yellow","Green","Purple","Orange"]
trigger_for_food = ["Pizza","Chicken","Sushi","Steak","Fish","Apple","Orange","Candy"]
trigger_for_number = ["1","2","3","4","5","6","7","8","9","10","100",]
##Checks input against "trigger" lists. Any matches will turn "fate" to -1.
for i in range(len(trigger_for_color)):
    if trigger_for_color[i] == color:
        fate = -1
for i in range(len(trigger_for_food)):
    if trigger_for_food[i] == food:
        fate = -1
for i in range(len(trigger_for_number)):
    if trigger_for_number[i] == number:
        fate = -1
##Chooses random element from lists of possible outcomes
rbb = randrange(len(bad_building))
rgb = randrange(len(good_building))
rbj = randrange(len(bad_job))
rgj = randrange(len(good_job))
rbm = randrange(len(bad_mate))
rgm = randrange(len(good_mate))
rbo = randrange(len(bad_offspring))
rgo = randrange(len(good_offspring))
##Uses fate value to determine which set (bad or good) of outcomes to randomly generate.
if fate == 0 or fate == 1:
    print ("You will live in "+good_building[rgb]+", working as "+good_job[rgj]+". You will marry "+good_mate[rgm]+", and give birth to "+good_offspring[rgo]+".")
if fate == -1:
    print ("You will live in "+bad_building[rbb]+", working as "+bad_job[rbj]+". You will marry "+bad_mate[rbm]+", and give birth to "+bad_offspring[rbo]+".")