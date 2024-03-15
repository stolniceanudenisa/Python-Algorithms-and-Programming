def CitireNumar():
    n=int(input("Dati un numar: "))
    return n
''' 
    descriere - functie
    input -
    output -
    
    Formula:
    Age in Days = (Age in Years x 365.2425) + Remaining Days
    Where--->
    Age in Years = ((Current Date) - (Date of Birth) / 365.2425)
    Remaining Days = FLOOR(MOD((TODAY() - Birthdate), 365.2425))
    https://www.shorttutorials.com/how-to-calculate-age/age-in-days.html
'''

def date_persoana(an,luna,zi,an_curent,luna_curenta, zi_curenta):
