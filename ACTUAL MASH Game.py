##THE most realistic MASH simulator (aside from graphics) outthere! No shortcuts!!Just follow the prompts and have fun!
from Myro import *
processing_list = ["Mansion","Apartment","Shack","House"]     #used as a seperate list to actually process through all the user'sinput and create outcomes
##Lists used to generate future outcome
mash = ["Mansion","Apartment","Shack","House"]
spouse_list = []
kids_list = []
cars_list = []
##Just a random introduction
name = input("Welcome to the 100% Legit and Scam-Free Gaurenteed Fortune Telling Software (trial version) Please enter your name now")
creditcard = input("Hello "+name+" Unfortuantely there is no trial version and you must pay now. Enter your credit card number")
print("Thank you for your information, "+name+"! You now have the full version of Fortune Teller!")
##Collecting user_input to generate list of possible outcomes
for i in range(4):          #List of spouses
    spouse = input("Give me the names of possible spouses, each less fair than the last")
    spouse_list.append(spouse)
    processing_list.append(spouse)
t = 0
while t<4:            #Number of kids
    kids = input("Give four different number of kids you will have?")
    try:                #Making sure input is a number
        val = int(kids)
    except ValueError:
        print("That's not an integer!")
    else:
        t += 1
        kids_list.append(kids)
        processing_list.append(kids)
for i in range(4):         #List of cars
    cars = input("Give four different cars you might have in the future")
    cars_list.append(cars)
    processing_list.append(cars)
while t==4:                #Random number to generate MASH
    r = input("Give me a random number to help predict your future!")
    try:                 #Making sure input is a number
        val = int(r)
    except ValueError:
        print("That's not an integer!")
    else:
        randnum = int(r)    
        if randnum==0:       #Making sure input is not 0, or it defeats the purpose of the game!
            print("That number is not usable!")
        else:
            t += 1          #will end loop
start_index = 0                 #where the script starts "counting" just like in real life
while len(processing_list)>0:
    ##This removes one item from the list in traditional MASH style, without fear of overflow/code breaking due to high numbers     
    chosen_index = (randnum+(start_index-1))%(len(processing_list))    #this function handles the case where our randnum does beyond the amount indexes available          
    start_index = chosen_index
    if processing_list[chosen_index] in mash and len(mash)>1:          #these if/elifs will keep removing outcomes form their own groups until only one remains
            mash.remove(processing_list[chosen_index])
    elif processing_list[chosen_index] in spouse_list and len(spouse_list)>1:
            spouse_list.remove(processing_list[chosen_index])
    elif processing_list[chosen_index] in kids_list and len(kids_list)>1:
            kids_list.remove(processing_list[chosen_index])
    elif processing_list[chosen_index] in cars_list and len(cars_list)>1:
            cars_list.remove(processing_list[chosen_index])   
    del processing_list[chosen_index]               #shortens processing)list after each iteration to improve speed
##Printing final results!!
print("You will live in a(n) "+mash[0]+"!")
print("Your future spouse will be "+spouse_list[0]+"!")
print("You will have "+kids_list[0]+" kid(s)!")
print("You will drive in a(n) "+cars_list[0]+"!")
print("Thanks for playing, "+name+"!")
