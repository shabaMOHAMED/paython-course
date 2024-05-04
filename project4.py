# welcome to my app
# How old are you?
# 10
# sorry, you can't use the app
# 12 
# Good. you can use the app
#-----------------------------------------------------------------------------------------------

#print("welcome to my app")
#age=int(input("How old are you? \n"))
#if age> 12 :
   # print ("Good. you can use the app")
#else :
    #print("sorry, you can't use the app")
#----------------------------------------------------------------------------------------------------

#score= float(input("Enter your test score : \n"))
#if score >= 90 :
   # print(" the grade is A")
#elif score >= 75 :
   # print("the grade is B")
#elif score >= 50 :
    #print (" the grade is C")
#else :
    #print("the grade is F")
#-------------------------------------------------------------------------------------------------------

#chair_number=int(input(" Enter the chair number : \n "))
#if chair_number == 21 :
   # print(" You win ")
#else :
    #print(" sorry")
#------------------------------------------------------------------------------------------------------
#number =int(input(" Enter your number : \n "))
#if number!= 13 :
    #print("you win ")
#else :
   # print (" sorry")
#-------------------------------------------------------------------------------------------------------

#pass_word=str(input("Enter your pass word :\n"))
#if pass_word == ("shaban 2018") :
 #print ("Hello !")
#else :
 #print(" wrong pass word")
#----------------------------------------------------------------------------------------------------------


#the_word= input(" Enter yes , no , maybe : \n")
#if the_word == "yes" :
# print (" you write yes")
#elif the_word == "no" :
 #print (" yoy write no")
#elif the_word == "maybe":
# print("you write maybe")
#else :
 #print(" please folow the instructions")
#----------------------------------------------------------------------------------------------------------------------------

#number = int(input(" Guess the number : \n"))
#if number == 7 :
    #print(" right number ")
#else :
   # print(" wrong number ")
#------------------------------------------------------------------------------------------------------------------------------

#cairo , alexandria , tanta

#area= input("Chose an area: (Cairo) , (Alexandria) , or (Tanta) ")

#if area.lower() == "cairo" or  area.lower()== "alexandrai" or area.lower()=="tanta" :
    #print(f"{area} is on our list!")

#else:
   # print(f"Sorry, {area} is not on our list!")
#----------------------------------------------------------------------------------------------------------------------------------

#age =int(input("Enter your age : \n"))
#license =input("Do you have license ? type (Yes) or (No) \n ")

#if age >= 18 and license.lower() == "yes":
    #print("you can drive")

#elif age <18 or license.lower() == "no":
 #print("you can not drive")

#else :
   #print(f"sorry, your entery of [ {license} ] is not understood")
#-------------------------------------------------------------------------------------

#is_egyptian=input("Are you Egyptian ? type (yes) or (no) \n").lower()

#if is_egyptian =="yes":
   # print ("Good, that's the frist step")

    #is_18=input("Are you above 18 ? Type (yes) or (no) \n").lower()
   # if is_18 == "yes":
       # print("you can have an ID")
    #else:
      #  print("Sorry, you have to be 18 or older")
       # print("please try again when you are 18")

#else:
    #print("Sorry, an Egyptian ID is give only to Egyptian")

#--------------------------------------------------------------------------------------------------

#welcome massage

print("""░░░░░░░░░░░║
░░▄█▀▄░░░░░║░░░░░░▄▀▄▄
░░░░░░▀▄░░░║░░░░▄▀
░▄▄▄░░░░█▄▄▄▄▄▄█░░░░▄▄▄
▀░░░▀█░█▀░░▐▌░░▀█░█▀░░░▀
░░░░░░██░░▀▐▌▀░░██
░▄█▀▀▀████████████▀▀▀█
█░░░░░░██████████░░░░░▀▄
█▄░░░█▀░░▀▀▀▀▀▀░░▀█░░░▄█
░▀█░░░█░░░░░░░░░░█░░░█▀
""")
print("welcome to my island")

#chose the door

print("There are Two doors in front of you.🚪 a red door and 🚪 a blue door")
two_doors=input("which door do you want to open? \n").lower()

if two_doors=="red":
    print("Great! now you entered a room.")
    print("you found three boxes : white, 🎁 black, 🎁 green, 🎁")

#chose the box

    boxes= input("which box do you open?").lower()
    if boxes=="white":
       print("Oops! you oopened abox filled with snakes 🐍🐍🐍")
    elif boxes=="black":
        print("Oops! you oopened abox filled with spiders 🕸️🕸️🕸️")
    elif boxes=="green":
        print("Congratulations! You found treasure! 💰💰💰")
    else:
        print(f"{boxes} invalid choice!")

    
elif two_doors=="blue":
    print("Oops! you chose the crocodile door. \nGame over! 🐊🐊🐊")
else:
    print(f"{two_doors} invalid choice!")    



















    

    
