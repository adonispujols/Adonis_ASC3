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
print("Thank you for your information! You now have the full version of Fortune Teller!")
##Gathering user input
color = input("What's your favorite color?")
food = input("Favorite Food?")
number = input("Favorite Number?")
##Listing possible outcomes. "Bad" and "Good" Outcomes for each category have their own lists.
bad_building = ["Cardboard box", "Apartment in North Korea", "Trump Towers (must sleep with Trump", "Barn House"]
good_building = ["Trump Towers (you can rename it)", "Bill Gate's Mansion", "Summer House out on Hawaii","Floating Fortress"]
bad_job = ["NO JOB FOR YOU! GET INTERESTING!"]
good_job = ["Ruler of the World", "CEO of Windows", "Supreme Ruler of the Universe", "God"]
bad_mate = ["NO ONE WANTS ANYONE BORING, GET INTERESTING!"]
good_mate = ["This Year's Miss America", "Hottest Model in the world", "Anyone", "Your Crush"]
bad_offspring = ["NO OFFSPRING FOR YOU SINCE YOU CAN'T GET MATE!"]
good_offspring = ["some many children that you could literally make your own country", "The Smartest Kid in the World", "Dat Boi", "Karate Kid"]
##Lists of replies that trigger a change to "fate" variable (As of now only changes fate to -1)
trigger_for_color = ["Red","Blue","Yellow","Green","Purple","Orange"]
trigger_for_food = ["Pizza","Chicken","Sushi","Steak","Fish","Apple","Orange","Candy"]
trigger_for_number = ["1","2","3","4","5","6","7","8","9","10","100",]
##Checks input against "trigger" lists. Any matches will turn "fate" to -1.
if color in trigger_for_color:
    fate = -1
if food in trigger_for_food:
    fate = -1
if number in trigger_for_number:
    fate = -1
 ##Uses fate value to determine which set (bad or good) of outcomes to randomly generate.
if fate == -1:
    print ("You will live in"+bad_building[a-1]+bad_job[0]+bad_mate[0]+bad_offspring[0])