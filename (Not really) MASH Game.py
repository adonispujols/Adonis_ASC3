##Gives a random set of "future outcomes" that's affected by the user's input
from random import *
##User's input affects the "fate" stat, changing the type of outcome they recieve
# 0 = neutral outcome
# <0= bad outcome
# >0= good outcome
fate = 0
## Introduction (not essential)
name = input("Welcome to the 100% Legit and Scam-Free Gaurenteed Fortune Telling Software (trial version) Please enter your name now")
creditcard = input("Hello "+name+" Unfortuantely there is no trial version and you must pay now. Enter your credit card number")
print("Thank you for your information, "+name+"! You now have the full version of Fortune Teller! Now, I am not your usual fortune teller. Say anything that I particularly do not like and your fortune may be adversely affected...")
##Gathering user input
color = input("What's your favorite color?")
food = input("Favorite Food?")
number = input("Favorite Number?")
##Listing possible outcomes. "Bad" and "Good" Outcomes for each category have their own lists.
neutral_building = ["a regular house", "a bland apartment","a nice cabin house","whatever seems comfy"]
bad_building = ["a cardboard box", "an apartment in North Korea", "Trump Towers (but must sleep with Trump", "a barn house"]
good_building = ["Trump Towers (you can rename it)", "Bill Gate's Mansion", "a summer house out on Hawaii","a floating fortress"]
neutral_job = ["an office assistant","a clerk","a janitor","a teacher"]
bad_job = ["a harbage man!","a truck driver","a Trump employee","Mr. Bean's special helper"]
good_job = ["ruler of the world", "CEO of Windows", "Supreme Ruler of the Universe", "God"]
neutral_mate = ["a bland wife","your childhood friend","the girl across the street","a funny person"]
bad_mate = ["no one","a dog","a skeleton","a flower"]
good_mate = ["this year's Miss America", "the hottest model in the world", "anyone you like", "your crush"]
neutral_offspring = ["a couple of brats","simple children","smart, but silly kids","one child"]
bad_offspring = ["a mutant","the Devil","a monster","nothing"]
good_offspring = ["so many children that you could literally make your own country", "the smartest kid in the world", "Dat Boi", "Karate Kid"]
##Lists of replies that trigger a change to "fate" variable
bad_trigger_for_color = ["Red","Blue","Yellow"]
good_trigger_for_color = ["Green","Purple","Orange"]
bad_trigger_for_food = ["Pizza","Chicken","Sushi","Steak"]
good_trigger_for_food = ["Fish","Apple","Orange","Candy"]
bad_trigger_for_number = ["1","2","3","4","5"]
good_trigger_for_number = ["6","7","8","9","10","100",]
##Checks input against "trigger" lists. Any matches will cause fate to change
if color in bad_trigger_for_color:
    fate -= 1
elif color in good_trigger_for_color:
    fate += 1
if food in bad_trigger_for_food:
    fate -= 1
elif food in good_trigger_for_food:
    fate += 1    
if number in bad_trigger_for_number:
    fate -= 1
elif number in good_trigger_for_number:
    fate += 1    
##Uses fate value to determine which set (bad or good) of outcomes to randomly generate.
if fate==0:
    print ("Your future seems bland and simple. You will live in "+choice(neutral_building)+", working as "+choice(neutral_job)+". You will marry "+choice(neutral_mate)+", and give birth to "+choice(neutral_offspring)+".")
if fate<0:
    print ("Your future looks terrible. You will live in "+choice(bad_building)+", working as "+choice(bad_job)+". You will marry "+choice(bad_mate)+", and give birth to "+choice(bad_offspring)+".")
if fate>0:
    print ("Your future holds great promise. You will live in "+choice(good_building)+", working as "+choice(good_job)+". You will marry "+choice(good_mate)+", and give birth to "+choice(good_offspring)+".")    
