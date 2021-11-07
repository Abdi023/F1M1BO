import os
import sys 
import time

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./60)
        



# vraag 1 en antwoord 1 en antwoord


def vraag1():
    os.system("cls")
    slowprint("""je bent geboren in een land waar het veilig is een overheid bestuurd.
je leeft met je familie in een vrede, en opeens is het in je land gaals geworden door dat de
overheid de burgers te hard hebben laten underdrukken.
dit verhaal gaat over vluchtelingen en landen die in burger oorlog zitten, en hoe het leven daar is en wat ze meemaken.
""")
    slowprint("Wil jij je land verlaten waar je geboren bent of wil jij blijven in je land?\n")

    slowprint("A. Ja ik blijf in mijn land")
    slowprint("B. Nee Ik wil vluchten")



    answer1 = input("kies volgende antwoorden uit: >>> ")

    if answer1.lower() == "A" or answer1.lower() == "a":
        verhaal2()
    elif answer1.lower() == "B" or answer1.lower() == "b":
        verhaal3()
    else:
        print("het is een fout antwoord")
        vraag1()



def vraag2():
    os.system("cls")
    slowprint("wil jij met het oorlog meedoen of wil jij het niet meedoen?")

    slowprint("A. Ja")
    slowprint("B. Nee")


    answer2 = input()

    if answer2.lower()  == "A" or answer2.lower() == "a":
        verhaal6()
    elif answer2.lower()  == "B" or answer2.lower() == "b":
        verhaal9()



def vraag3():
    os.system("cls")
    slowprint("")



    slowprint("A. Voor de Overheid gaan vechten.")
    slowprint("B. Voor je eigen Stam gaan vechten.")
    slowprint("C. Voor jezelf gaan vechten.")
    slowprint("D. Voor de terrorist groep gaan vechten.")


    answer3 = input()

    if answer3.lower()  == "A" or answer3.lower()  == "a":
        verhaal4()
    elif answer3.lower()  == "B" or answer3.lower()  == "b":   
        verhaal7()
    elif answer3.lower()  == "C" or answer3.lower()  == "c":   
        verhaal10()
    elif answer3.lower()  == "D" or answer3.lower()  == "d":   
        verhaal8()





def  vraag4():
    os.system("cls")
    slowprint("Je koos om niet in de oorlog in tegaan wat wil je doen?\n")

    slowprint("A. Je gaat onderduiken.")
    slowprint("B. je gaat weg vanuit je stad naar een andere stad.")
    slowprint("C. Je wilt je eigen huis niet verlaten")
    slowprint("D.  Je gaat in een soorte vluchtelingenkamp om eten te gaan zoeken")

    answer4 = input()

    if answer4.lower()  == "A" or answer4.lower()  == "a":
        verhaal11()
    elif answer4.lower()  == "B" or answer4.lower() == "b":
        verhaal15()
    elif answer4.lower() == "C" or answer4.lower() == "c":
        verhaal13()
    elif answer4.lower() == "C" or answer4.lower() == "c":
        verhaal16()



def vraag5():
    os.system("cls")
    slowprint("""Via welke land ga je bijvoorbeeld naar europa of een andere gedeelte van de wereld?
Je kiest om bijvoorbeeld via de kust van griekeland naar europa te komen.......""")


    slowprint("A. Je gaat naar turkije om te wonnen en nieuwe toekomst te bouwen")
    slowprint("B. je gaat via via libya naar griekeland.")
    slowprint("C. je gaat via turkije naar griekeland.")

    answer5 = input()

    if answer5.lower() == "A" or answer5.lower() == "a":
        verhaal12()
    elif answer5.lower() == "B" or answer5.lower() == "b":
        verhaal19()
    elif answer5.lower() == "C" or answer5.lower() == "c":
        verhaal22()



def vraag6():
    slowprint("Je wilt via turkije naar europa, Hoe wil jij naar europa?")

    slowprint("A. Via smokkelaars. ")
    slowprint("B. Via vluchtelingen kamp")

    answer6 = input()

    if answer6.lower() == "A" or answer6.lower()  == "a" or answer6.lower()  == "YES" or answer6.lower()  == "yes" or answer6.lower()  == "y":
        verhaal20()
    elif answer6.lower()  == "B" or answer6.lower()  == "b" or answer6.lower()  == "NO" or answer6.lower()  == "no" or answer6.lower()  == "n":
        verhaal23()


def vraag7():
    slowprint("de smokkelaars vragen of je via boot wilt gaan of via auto?")

    slowprint("A. Via boot")
    slowprint("B. Via auto")

    answer7 = input()

    if answer7.lower() == "A" or answer7.lower() == "a":
        verhaal21()
    elif answer7.lower() == "B" or answer7.lower() == "b":
        verhaal5()

def vraag8():
    slowprint("de smokkelaars vragen of je via boot wilt gaan of via auto?")

    slowprint("A. je betaalt het extra geld")
    slowprint("B. je weigert het te betalen.")
    slowprint("c. Je hebt geen geld.")

    answer8 = input()

    if answer8.lower() == "A" or answer8.lower() == "a":
        verhaal24()
    elif answer8.lower() == "B" or answer8.lower() == "b":
        verhaal25()
    elif answer8.lower() == "C" or answer8.lower() == "c":
        verhaal26()




def vraag9():
    slowprint("Je vroeg je familie of zij voor jou konden betalen?")

    slowprint("A. je familie accepteerden om het geld te betalen .")
    slowprint("B. je familie heeft geen geld.")

    answer8 = input()

    if answer8.lower() == "A" or answer8.lower() == "a":
        verhaal27()
    elif answer8.lower() == "B" or answer8.lower() == "b":
        verhaal28()
    elif answer8.lower() == "C" or answer8.lower() == "c":
        print()




def verhaal2():
    print("""je hebt gekozen om in je land te blijven en je weet wel dat er burger oorlog is je land.
jij hoopt dat het goed komt met land, maar de burger oorlog verergert zich en er is geen
kans om het land te verlaten.
""")


def verhaal3():
    print("""je gaat op de vlucht je weet niet waar jij precies waar je heen wilt en je weet niet wat je
nog gaat meemaken het enige wat je in je hoofd hebt is alleen het verlaten van jou eigen
land. je gaat zonder je familie en je vrienden weg. je hebt uiteindelijk je eigenland verlaten""")



def verhaal4():
    print("je koos te gaan vechten voor de overheid.")

# einde verhaal 5
def verhaal5():
    print("""Je bent via auto naar europa gekomen en je bent opgepakt door de politie, je zit in de
gevangenis een na paar maanden ben je weer vrijgelaten en word je gestuurd naar
Azielzoeker. je zit nu in de azielzoeker je wacht voor een onbepaalde indetiteit bewijs om in
het land geaccepteerd teworden. en ondertussen ga je naar school om het taal van het land
te leren. je gaat ook leren samenleven met nieuwe rassen, culturen , religieën talen, etc.""")


def verhaal6():
    print("""je hebt gekezon om te gaan vechten en jij  weet niet wie  eerlijk is welke kant nou de goede kant is , en je bent in de oorlog en  je weet niet welke kant je nou wilt gaan.
je weet niet of  politici speelt met je leven en je hebt geen keuze om te gaan terug te gaan.je doet wat politici zegt ook all martel je de burgers van het land om te het doel te bereiken van een leider. het kan ook goed aflopen en je kan een held worden omdat jij voor jouw land hebt gevochten om een overheid te creeëren.
Maar jij kan ook voor lafaard worden omdat jij je burgers hebt gemartels voor een leider om op zijn Stoel te verdedigen.""")


def verhaal7():
    print("""Je koos tegaan vechten voor jouw stam om het leven te reden van jullie famillies, en het tegen
de overheid en hun systeem te gaan vechten omdat de overheid meer het doel van een leider
volgt die dictatuur is of mischien lafaard is.""")


def verhaal8():
    print("""Je koos uiteindelijk tegaan vechten voor de terrorist groep, jullie hebben 1van de 3 van het
land overgenomen, jullie hebben mensen gemarteld na een tijdje aan de macht hebben,
waren de overheid geholpen door andere overheden en is jouw terrorist groep verslagen,
jij hebt nu de kans om jezelf overtegeven aan de overheid.""")


def verhaal9():
    print("""Je koos om niet tegaan vechten, maar je kunt niet 100% procenten veilig zijn.
""")



def verhaal10():
    print("""Je vecht nu voor jezelf en je familie je vecht voor zowel de overheid als de terroristen en
andere groep je bent voor niemand anders dan jezelf.""")


def verhaal11():
    print("""Je besloot om te onderduiken en onderdook tegen de oorloog het duurde lang om te
onderduiken na zoveel hoop je is het je gelukt om jezelf te reden tegen de oorlog.
""")


def verhaal12():
    print("""je bent uiteindelijk naar turkije gekomen om daar wil jij nu toekomst gaan bouwen.
je hebt het de vlucht het overleefd.""")



def verhaal13():
    print("""Je wilt je eigen huis en de stad waar je geboren niet verlaten omdat moeilijk voor jou om je
huis en je stad en je familie en je vrienden in de steek te verlaten.""")


def verhaal14():
    print("")


def verhaal15():
    print("""Je koos voor om je eigen stad te verlaten en naar andere stad, een steeds doe je maar zo als er
oorloog gebeurd in de stad die je woont.
""")



def verhaal16():
    print("""Je bent op een in een soort vluchtelingencamp gekomen je hebt het hongernood overleefd,
maar de oorloog is er nog steeds.""")


def verhaal17():
    print("")


def verhaal18():
    print("")


def verhaal19():
    print("""je gaat via libya met de boot naar griekeland je bent in griekeland gekomen.
je wilt weer van griekeland naar andere europese land.""")


def verhaal20():
    print("Je hebt de smokkelaars betaalt om illegaal naar een europese land te komen om een nieuwe toekomst te beginnen.")

def verhaal21():
    print("""Je koos om via boot naar europa te gaan en je bent met de boot meegegaan na uurtjes het
boot waren hebben de smokkelaars gestopt om weer extra geld te betalen.""")


def verhaal22():
    print("Je bent via turkije naar europa gekomen, je bent naar een europese land gekomen.")


def verhaal23():
    print("""Je bent in de vluchtelingen kamp gekomen , na een tijdje wachten heb je visa gekregen.
en je bent nu in een europese land om opnieuw een toekomst te bouwen.""")


def verhaal24():
    print("""je hebt het geld betaalt en je bent veilig in europa gekomen.""")


def verhaal25():
    print("""Je koos om het extra geld niet te betelen, en de smokkelaars hebben jou in de zee gegooid,
je bent dood.""")


def verhaal26():
    print("""Je hebt verteld dat je geen geld had en ze hebben jou gevraagd om jou familie te bellen of ze
voor jou konden betalen. je hebt geen keuzen dan je familie bellen.""")


def verhaal27():
    print("Je familie hebben het geld betaald, je bent gered door jou familie. je zit nu in eoropa.")


def verhaal28():
    print("""Je familie hebben het geld gezocht ze deden alles om geld te vinden om jou te gaan reden
maar dat was niet gelukt , ze smeekten de smokkelaars om jou te laten gaan , maar de
smokkelaars besloten om jou in het zee te gooien en jou daar te laten. je bent uiteindelijk
dood te gaan.""")








vraag1()
verhaal2()
vraag1()
verhaal3()
vraag2()
verhaal6()
vraag2()
verhaal9()
vraag3()
verhaal14()
vraag3()
verhaal17()
vraag3()
verhaal10()
vraag3()
verhaal8()
vraag4()
verhaal11()
vraag4()
verhaal15()
vraag4()
verhaal13()
vraag4()
verhaal16()
vraag5()
verhaal12()
vraag5()
verhaal19()
vraag5()
verhaal22()
vraag6()
verhaal20()
vraag6()
verhaal23()
vraag7()
verhaal21()
vraag7()
verhaal5()
vraag8()
verhaal24()
vraag8()
verhaal25()
vraag8()
verhaal26()
vraag9()
verhaal27()
vraag9()
verhaal28()






def restart():
    now = True
    while now == True:
        slowprint("")


        slowprint("yes")
        slowprint("no")
        restart = input

        if restart.lower() == "YES" or restart.lower() == "yes" or restart.lower() == "y":
            vraag1()
        else:
            stop()
    now = False

def stop():
    stop = input()

    if stop.lower() == "NO" or stop.lower() == "no" or stop.lower() == "n":
        slowprint("bedankt voor het spelen van mijn verhaal")

