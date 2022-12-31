import tkinter as tk

def calculate_total():
    ageA = int(age_entry_a.get())
    ageB = int(age_entry_b.get())
    ageC = int(age_entry_c.get())
    prezzoChampagne = float(champagne_price_entry.get())

    costoA = 0
    costoB = 0
    costoC = 0

    prezzoDiscoteca = 100
    babysitting = 10
    piro = 10
    vegan = 10

    # prima persona
    if ageA >= 18:
        costoA += 30 + prezzoDiscoteca
    elif ageA >= 6 and ageA <= 17:
        costoA += 20
    else:
        costoA += 10 + babysitting

        # nascondi etichetta e entry per i giochi pirotecnici
        # pyro_label_a.pack_forget()
        # pyro_entry_a.pack_forget()

        if ageA < 6:

            # mostra etichetta e entry per i giochi pirotecnici
            pyro_label_a.pack()
            pyro_entry_a.pack()

            if pyro_entry_a.get().lower() == 'Si':
                costoA += piro

    # seconda persona
    if ageB >= 18:
        costoB += 30 + prezzoDiscoteca
    elif ageB >= 6 and ageB <= 17:
        costoB += 20
    else:
        costoB += 10 + babysitting

        # nascondi etichetta e entry per i giochi pirotecnici
        # pyro_label_b.pack_forget()
        # pyro_entry_b.pack_forget()

        if ageB < 6:
            # mostra etichetta e entry per i giochi pirotecnici
            pyro_label_b.pack()
            pyro_entry_b.pack()

            if pyro_entry_b.get().lower() == 'Si':
                costoB += piro

    # terza persona
    if ageC >= 18:
        costoC += 30 + prezzoDiscoteca
    elif ageC >= 6 and ageC <= 17:
        costoC += 20
    else:
        costoC += 10 + babysitting

        # nascondi etichetta e entry per i giochi pirotecnici
        # pyro_label_c.pack_forget()
        # pyro_entry_c.pack_forget()

        if ageC < 6:
            # mostra etichetta e entry per i giochi pirotecnici
            pyro_label_c.pack()
            pyro_entry_c.pack()

            if pyro_entry_c.get().lower() == 'Si':
                costoC += piro

    total = costoA + costoB + costoC

    if ageA >= 18 or ageB >= 18 or ageC >= 18:
        champagne_var = tk.IntVar()
        if champagne_var.get() == 1:
            nChampagne = int(champagne_qty_entry.get())
            total = total + (nChampagne * prezzoChampagne)

    vegan_var = tk.IntVar()
    if vegan_var.get() == 1:
        nVegan = int(vegan_qty_entry.get())
        total = total + (vegan * nVegan)

    total_label['text'] = 'Il totale è: {}'.format(total)

# creazione finestra
root = tk.Tk()
root.title('Cenone di capodanno')
root.geometry("1000x727+460+140")
root.iconbitmap('./assets/icon.ico')
root.resizable(False, False)

# età prima persona
age_label_a = tk.Label(root, text='Inserisci l\'età della prima persona:')
age_label_a.pack()

age_entry_a = tk.Entry(root)
age_entry_a.pack()

# giochi pirotecnici prima persona
pyro_label_a = tk.Label(root, text='Giochi pirotecnici prima persona (Si/No):')
pyro_label_a.pack()

pyro_entry_a = tk.Entry(root)
pyro_entry_a.pack()

#età seconda persona
age_label_b = tk.Label(root, text='Inserisci l\'età della seconda persona:')
age_label_b.pack()

age_entry_b = tk.Entry(root)
age_entry_b.pack()

#giochi pirotecnici seconda persona
pyro_label_b = tk.Label(root, text='Giochi pirotecnici seconda persona (Si/No):')
pyro_label_b.pack()

pyro_entry_b = tk.Entry(root)
pyro_entry_b.pack()

# età terza persona
age_label_c = tk.Label(root, text='Inserisci l\'età della terza persona:')
age_label_c.pack()

age_entry_c = tk.Entry(root)
age_entry_c.pack()

# giochi pirotecnici terza persona
pyro_label_c = tk.Label(root, text='Giochi pirotecnici terza persona (Si/No):')
pyro_label_c.pack()

pyro_entry_c = tk.Entry(root)
pyro_entry_c.pack()

# prezzo champagne
champagne_price_label = tk.Label(root, text='Inserisci il prezzo dello champagne')
champagne_price_label.pack()

champagne_price_entry = tk.Entry(root)
champagne_price_entry.pack()

# quantità champagne
champagne_qty_label = tk.Label(root, text='Quantità champagne:')
champagne_qty_label.pack()

champagne_qty_entry = tk.Entry(root)
champagne_qty_entry.pack()

# quantità persone vegane
vegan_qty_label = tk.Label(root, text='Quantità persone vegane:')
vegan_qty_label.pack()

vegan_qty_entry = tk.Entry(root)
vegan_qty_entry.pack()

# pulsante per calcolare il totale
calculate_button = tk.Button(root, text='Calcola totale', command=calculate_total)
calculate_button.pack()

# etichetta per mostrare il totale
total_label = tk.Label(root, text='')
total_label.pack()

root.mainloop()