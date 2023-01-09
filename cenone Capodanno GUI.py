import tkinter as tk

def calculate_total():
    #dichiarazione variabili
    ageA = int(entryAgeA.get())
    ageB = int(entryAgeB.get())
    ageC = int(entryAgeC.get())
    prezzoChampagne = float(entryPriceChampagne.get())
    piroTF = str(entryPiro.get().lower())
    champagneTF = str(entryChampagne.get().lower())
    veganTF = str(entryVegan.get().lower())
    costoA = 0
    costoB = 0
    costoC = 0
    prezzoDiscoteca = 100
    babysitting = 10
    piro = 10
    vegan = 10

    #calcolo prima persona
    if ageA >= 18:
        costoA += 30 + prezzoDiscoteca
    elif ageA >= 6 and ageA <= 17:
        costoA += 20
    else:
        costoA += 10 + babysitting
        if piroTF == 'Si':
            costoA += piro
            
    #calcolo seconda persona
    if ageB >= 18:
        costoB += 30 + prezzoDiscoteca
    elif ageB >= 6 and ageB <= 17:
        costoB += 20
    else:
        costoB += 10 + babysitting
        if piroTF == 'Si':
            costoB += piro

    #calcolo terza persona
    if ageC >= 18:
        costoC += 30 + prezzoDiscoteca
    elif ageC >= 6 and ageC <= 17:
        costoC += 20
    else:
        costoC += 10 + babysitting
        if piroTF == 'Si':
            costoC += piro

    #calcolo totale
    total = costoA + costoB + costoC

    #calcolo champagne
    if ageA >= 18 or ageB >= 18 or ageC >= 18:
        if champagneTF == 'Si':
          nChampagne = int(entryNumeroBicchieri.get())
          total += nChampagne * prezzoChampagne

    #calcolo vegani
    if veganTF == 'Si':
        nVegan = int(entryNumeroVegani.get())
        total += nVegan * vegan

    labelTotal['text'] = f"Il totale è: {total}"

#finestra
root = tk.Tk()
root.title('Cenone di capodanno')
root.geometry('1000x727+460+140')
root.iconbitmap('./assets/icon.ico')
root.resizable(False, False)

#label e entry
labelAgeA = tk.Label(root, text="Inserisci l\'età della prima persona:")
labelAgeA.pack()
entryAgeA = tk.Entry(root)
entryAgeA.pack()

labelAgeB = tk.Label(root, text="Inserisci l\'età della seconda persona:")
labelAgeB.pack()
entryAgeB = tk.Entry(root)
entryAgeB.pack()

labelAgeC = tk.Label(root, text="Inserisci l\'età della terza persona:")
labelAgeC.pack()
entryAgeC = tk.Entry(root)
entryAgeC.pack()

#verifica champagne, giochi piro e vegani
labelPriceChampagne = tk.Label(root, text="Inserisci il prezzo dello champagne:")
labelPriceChampagne.pack()
entryPriceChampagne = tk.Entry(root)
entryPriceChampagne.pack()

labelNumeroBicchieri = tk.Label(root, text="Inserisci il numero di bicchieri di champagne:")
labelNumeroBicchieri.pack()
entryNumeroBicchieri = tk.Entry(root)
entryNumeroBicchieri.pack()

labelPiro = tk.Label(root, text="Scrivi \"Si\" se la persona vuole usufruire di giochi pirotecnici e \"No\" se non vuole:")
labelPiro.pack()
entryPiro = tk.Entry(root)
entryPiro.pack()

labelChampagne = tk.Label(root, text="C\'è almeno una persona che vuole lo champagne?:")
labelChampagne.pack()
entryChampagne = tk.Entry(root)
entryChampagne.pack()

labelVegan = tk.Label(root, text="C\'è almeno una persona vegana?:")
labelVegan.pack()
entryVegan = tk.Entry(root)
entryVegan.pack()

labelNumeroVegani = tk.Label(root, text="Inserisci il numero di persone vegane:")
labelNumeroVegani.pack()
entryNumeroVegani = tk.Entry(root)
entryNumeroVegani.pack()

#bottone del totale
labelBottone = tk.Label(root, text="Clicca per ottenere il totale!")
labelBottone.pack()
buttonBottone = tk.Button(root, text="Clicca!", command=calculate_total)
buttonBottone.pack()

#stampa del totale
labelTotal = tk.Label(root, text="")
labelTotal.pack()
root.mainloop()