ageA = int(input("Inserisci l'età della persona: "));
ageB = int(input("Inserisci l'età della persona: "));
ageC = int(input("Inserisci l'età della persona: "));
prezzoChampagne = float(input("Inserisci il prezzo champagne: "));

costoA = 0;
costoB = 0;
costoC = 0;

prezzoDiscoteca = 100;
babysitting = 10;
piro = 10;
vegan = 10;

#prima persona
if ageA >= 18:
    costoA += 30 + prezzoDiscoteca;
elif ageA >= 6 and ageA <= 17:
    costoA += 20;
else:
    costoA += 10 + babysitting;

    piroTF = input("Scrivi \"Si\" se la persona vuole usufruire di giochi pirotecnici o \"No\" se non vuole: ");
    if piroTF == "Si":
        costoA += piro;


#seconda persona
if ageB >= 18:
    costoB += 30 + prezzoDiscoteca;
elif ageB >= 6 and ageB <= 17:
    costoB += 20;
else:
    costoB += 10 + babysitting;

    piroTF = input("Scrivi \"Si\" se la persona vuole usufruire di giochi pirotecnici o \"No\" se non vuole: ");
    if piroTF == "Si":
        costoB += piro;


#terza persona
if ageC >= 18:
    costoC += 30 + prezzoDiscoteca;
elif ageC >= 6 and ageC <= 17:
    costoC += 20;
else:
    costoC += 10 + babysitting;

    piroTF = input("Scrivi \"Si\" se la persona vuole usufruire di giochi pirotecnici o \"No\" se non vuole: ");
    if piroTF == "Si":
        costoC += piro;

total = costoA + costoB + costoC;

if ageA >= 18 or ageB >= 18 or ageC >= 18:
    champagneTF = input("C'è almeno una persona che vuole lo champagne?: ");
    if champagneTF == "Si":
        nChampagne = int(input("Inserisci il numero di bicchieri: "));
        total = total + (nChampagne * prezzoChampagne);

veganTF = input("C'è almeno una persona vegana?: ");
if veganTF == "Si":
    nVegan = int(input("Inserisci il numero di persone vegane: "));
    total = total + (vegan * nVegan);

print(total);