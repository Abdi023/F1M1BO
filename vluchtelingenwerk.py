import os
import datetime
import random
import sys 


# vraag 1 en antwoord 1 en antwoord


def vraag1():
    os.system("cls")
    print("kies 1 van de volgende 4 keuzen delen?\n")
    print("Wil jij je land verlaten waar je geboren bent of wil jij blijven in je land?\n")

    print("A. Ja ik blijf in mijn land")
    print("B. Nee Ik wil vluchten")



    answer1 = input("kies volgende antwoorden uit: >>> ")

    if answer1 == "A" or answer1 == "a":
        vraag2()
    elif answer1 == "B" or answer1 == "b":
        vraag3()
    else:
        print("het is een fout antwoord")
       
   


def vraag2():
    os.system("cls")
    print("""je hebt gekozen om in je land te blijven en je weet wel dat er burger oorlog is je land.
jij hoopt dat het goed komt met land, maar de burger oorlog verergert zich en er is geen
kans om het land te verlaten./n""")
    print("wil jij met het oorlog meedoen of wil jij het niet meedoen?")

    print("A. Ja")
    print("B. Nee")


    answer2 = input()

    if answer2 == "A" or answer2 == "a":
        vraag6()
    elif answer2 == "B" or answer2 == "b":
        vraag9()



def vraag3():
    os.system("cls")
    print("""je gaat op de vlucht je weet niet waar jij precies waar je heen wilt en je weet niet wat je
nog gaat meemaken het enige wat je in je hoofd hebt is alleen het verlaten van jou eigen
land. je gaat zonder je familie en je vrienden weg. je hebt uiteindelijk je eigenland verlaten.\n""")
    print("")



    print("A.  Voor de Overheid gaan vechten.")
    print("B. Voor je eigen Stam gaan vechten.")
    print("C. Voor jezelf gaan vechten.")
    print("D. Voor de terrorist groep gaan vechten.")


    answer3 = input()

    if answer3 == "A" or answer3 == "a":
        vraag4()
    elif answer3 == "B" or answer3 == "b":   
        vraag3()
    elif answer3 == "C" or answer3 == "c":   
        vraag5()
    elif answer3 == "D" or answer3 == "d":   
        vraag6()





def  vraag4():
    os.system("cls")
    print("je koos te gaan vechten voor de overheid.")
    print("Je koos om niet in de oorlog in tegaan wat wil je doen?")

    print("A. Je gaat onderduiken.")
    print("B. je gaat weg vanuit je stad naar een andere stad.")
    print("C. Je wilt je eigen huis niet verlaten")
    print("D.  Je gaat in een soorte vluchtelingenkamp om eten te gaan zoeken ")

    answer4 = input()

    if answer4 == "A" or answer4 == "a":
        print("")
    elif answer4 == "B" or answer4 == "b":
        print("")
    elif answer4 == "C" or answer4 == "c":
        print("")
    elif answer4 == "C" or answer4 == "c":
        print("")



def vraag5():
    os.system("cls")
    print("")
    print("")


    print("A. ")
    print("B. ")
    print("C. ")

    answer5 = input()

    if answer5 == "A" or answer5 == "a":
        print("")
    elif answer5 == "B" or answer5 == "b":
        print("")
    elif answer5 == "C" or answer5 == "c":
        print("")



def vraag6():
    print("""je hebt gekezon om te gaan vechten en jij weet niet wie eerlijk is welke kant nou de goede kant
is , en je bent in de oorlog en je weet niet welke kant je nou wilt gaan.
""")
    print("")

    print("A. ")
    print("B. ")

    answer6 = input()

    if answer6 == "A" or answer6 == "a":
        print("")
    elif answer6 == "B" or answer6 == "b":
        print("")


def vraag7():
    print("""Je koos tegaan vechten voor jouw stam om het leven te reden van jullie famillies, en het tegen
de overheid en hun systeem te gaan vechten omdat de overheid meer het doel van een leider
volgt die dictatuur is of mischien lafaard is.""")
    print("")

    print("A. ")
    print("B. ")

    answer7 = input()

    if answer7 == "A" or answer7 == "a":
        print("")
    elif answer7 == "B" or answer7 == "b":
        print("")

def vraag8():
    print("""Je koos uiteindelijk tegaan vechten voor de terrorist groep, jullie hebben 1van de 3 van het
land overgenomen, jullie hebben mensen gemarteld na een tijdje aan de macht hebben,
waren de overheid geholpen door andere overheden en is jouw terrorist groep verslagen,
jij hebt nu de kans om jezelf overtegeven aan de overheid.
""")



def vraag9():
    print("Je koos om niet tegaan vechten, maar je kunt niet 100% procenten veilig zijn.")


def vraag10():
    print("""Je vecht nu voor jezelf en je familie je vecht voor zowel de overheid als de terroristen en
andere groep je bent voor niemand anders dan jezelf.
""")

def vraag11():
    print()


def vraag12():
    print("")



def restart():
    now = True
    while now == True:
        print("")


        print("yes")
        print("no")
        restart = input

        if restart == "YES" or restart == "yes" or restart == "y":
            vraag1()
        else:
            stop()
    now = False

def stop():
    print("fijne dag")
    stop = input()

    if stop == "NO" or stop == "no" or stop == "n":
        print("bedankt verhet spelen mijn verhaal")
        stop()
    exit()



vraag1()

