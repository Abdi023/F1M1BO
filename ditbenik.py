import time
import os
import sys
import random
from typing import NoReturn

print("Hello You!")
print("Ik ben Abdi Abdikarim")
print("Ik woon in Haarlem")
print("Type je Naam Hier: ")
x = input()
print("Hallo " +  x , " aangenaam")

print("ik ben een Nieuwkomer op het Mediacollege Amsterdam \nDoor aantal vragen over mij te beantwoorden leer je mij beter kennen. \n\n")

eerste = True
while eerste == True:
        print("Kan je raden wat mijn afkomst is? \n")

        print("A. Somaliër.")
        print("B. Nederland")

        answer = input()

        if answer == "A" or  answer ==  "a":
                print("Ja ik ben een Somaliër.\n")
                
        elif answer == "B" or answer == "b":
                print("Nee ik ben opgegroeid in Nederland maar ik ben geen Nederlander.\n")
                eerste = False
                
                
                
tweede = True        
while tweede == True:
        print("Voordat ik naar het MBO op het MediaCollege Amsterdam kwam zat ik op het? \n\n")

        print("A. NOVA college Haarlem entree.")
        print("B. ROC NOVA college Beverwijk.")
        print("C. VMBO De Oosterhout Haarlem.")


        answer1 = input()

        if answer1 == "A" or answer1 == "a":
                        print("Nova college Haarlem was mijn eerste MBO school maar dat niet waar voor het Media college zat ik op het ROC Nova college Beverwijk.\n")
                       
        elif answer1 == "B" or answer1 == "b":
                        print("ik zat op het Media college kwam zat ik op het ROC nova college Beverwijk.\n")
                       
        elif answer1 == "C" or answer1 == "c":
                        print("ik zat op het VMBO school oosterhout.\n")
                        tweede = False
                        

derde = True
while derde == True:
        print("wat is mijn leeftijd volgens jou?.\n")

        print("A. ik ben 20 jaar jong.")
        print("B. ik ben 16 jaar jong.")
        print("C. ik weet het niet joh.")

        answer2 = input()
        if answer2 == "A" or answer2 ==  "a":
                print("Ja ik ben 20 jaar jong.\n")
               
        elif answer2 == "B" or answer2 == "b":
                print("Nee ik ben 20 jaar jong geen 12.\n")
                
        elif answer2 == "C" or answer2 == "c":
                print("oowh wat jammer maar ik ben 20 jaar oud.\n") 
                derde = False
                


vierde = True
while vierde == True:
        print("wat zijn mijn favoriete kleur?\n")

        print("A. groen")
        print("B. blauw")
        print("C. zwart")


        answer3 = input()

        if answer3 == "A" or answer3 == "a":
                print("nee groen is niet mijn favoriete kleur.\n")

        elif answer3 == "B" or answer3 == "b":
                print("ja blauw is mijn favoriete kleur.\n")

        elif answer3 == "C" or answer3 == "c":
                print("Ik vind zwart kleur mooi maar het is niet mijn favoriete kleur.\n")
                vierde = False


vijfde = True        
while vijfde == True:
        print("wat is mijn favoriete voetbal club volgens jou?\n")

        print("A. chelsea")
        print("B. manchester united")
        print("C. Real madrid")

        answer4 = input()

        if answer4 == "A" or answer4 == "a":
                print("nee chelsea is niet mijn favoriete club dat is manchester united.\n")

        elif answer4 == "B" or answer4 == "b":
                print("Ja manchester united is mijn favoriete club.\n")
                
        elif answer4 == "C" or answer4 == "c":
                print("nooit real madrid always mancherster united\n")
                vijfde = False
                

zesde = True
while zesde == True:
        print("wat is jouw leeftijd?\n")

        print("A. ik bent 16 jaar jong.")
        print("B. ik bent 18 jaar jong.")
        print("C. anders.")

        answer5 = input()
       
        if answer5 == "A" or answer5 == "a":
                print(" niet mooi zeg hoi hoi." + x + "\n")
                      
        elif answer5 == "B" or answer5 == "b":
                print("je bent fucking jong man.\n")
                
        elif answer5 == "C" or answer5 == "c":
                anpu = input("Type hier jouw leeftijd?: ")
                print("je hebt mooi leeftijd " + x + " ik wist niet dat jij " + anpu + " jaar jong was.")
                zesde = False
                

zevende = True
while zevende == True:
        print("wat zijn jou favoriete eten?\n")

        y = input("Type hier: ")
        print(y + " is een lekker gerecht hey  lekker " + x + "\n")

        print("wat is jou afkomt?\n")
        u = input("Type hier: ")
        print("waaw ik had het niet van je verwacht " + x + " ik wist niet dat jij " + u + " was\n")

        print("laatste vraag.\n")
        print("waar kom je vadaan?")
        waaw = input("Type hier: ")
        print(waaw + " is een mooi stad " +  x + " prachtig man")
        zevende = False
        quit()



        









