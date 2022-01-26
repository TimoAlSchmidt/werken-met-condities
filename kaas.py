vragen = ["Is de kaas geel?", "Zitten er gaten in?", "Is de kaas belachelijk duur?", "Is de kaas hard als steen?", "Heeft de kaas blauwe schimmels?", "Heeft de kaas een korst?", "Heeft de kaas een korst?"]
antwoorden = ["Emmenthaler", "Leerdammer", "Parmigiano Reggiano", "Goudse Kaas", "Blue de Rochbaron", "Foume d'Ambert", "Camembert", "Mozzarella"]
stap = 0
binary = 0
vraagnummer = 0

while stap < 3:
    print(vragen[vraagnummer] + " (Y/N)")
    antwoord = input()

    if(antwoord != "Y" and antwoord != "N"):
        print("Incorrect antwoord. Vul alstublieft Y of N in.")
        continue
    else:
        stap += 1
        binary = binary << 1
        vraagnummer += 1
        if (antwoord == "N"):
            vraagnummer += 1
            if(stap == 1):
                vraagnummer += 2
            binary += 1    

print("De kaas is " + antwoorden[binary])