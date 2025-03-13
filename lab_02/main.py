from scipy import stats

print("\n")
print("----------------------------------------------1--------------------------------------------")
print("\n")

#H0: μ=35 (przeciętny czas pracy baterii wynosi 35h)
#H1: μ≠35 (przeciętny czas pracy baterii różni się istotnie od czasu nominalnego)


# czasy netto próbki
baterie = [35.34, 36.26, 30.54, 38.2, 37.59, 39.18, 33.16, 34.23,
27.9, 36.33, 32.39, 34.89, 35.7, 31.99, 34.03]

# Wartość oczekiwana
czas = 35.00

# Przeprowadź test t-studenta
statystyka_T, p_wartosc = stats.ttest_1samp(baterie, czas)

# Wyświetl wyniki
print("Statystyka testowa:", statystyka_T)
print("P-wartość:", p_wartosc)

# Sprawdź istotność statystyczną na poziomie alfa = 0.05
alfa = 0.05
if p_wartosc < alfa:
    print("Odrzucamy hipotezę zerową - sredni czas pracy jest wiekszy niz 35h ")
else:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej - średnia czas nie jest rozny od 35h")

    print("\n")
    print("----------------------------------------------2--------------------------------------------")
    print("\n")

#H0: μ>=127,7 (przeciętne zuzycie paliwa wynosi 127,7 lub wiecej pomimo predkosci ponizej 17 wezlow)
#H1: μ<127,7 (przeciętny zuzycie paliwa przy predkosci ponizej 17 wezlow spada ponizej 127,7 tony dziennie)

# czasy netto próbki
rejsy = [ 101.1, 105.7, 102.6, 113.4, 98.1]

# Wartość oczekiwana
spalanie = 127.7

# Przeprowadź test t-studenta
statystyka_T, p_wartosc = stats.ttest_1samp(rejsy, spalanie, alternative='less')

# Wyświetl wyniki
print("Statystyka testowa:", statystyka_T)
print("P-wartość:", p_wartosc)

# Sprawdź istotność statystyczną na poziomie alfa = 0.05
alfa = 0.01
if p_wartosc < alfa:
    print("Odrzucamy hipotezę zerową - srednie spalanie spada ponizej 127,7 ")
else:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej - srednie spalanie nie spada ponizej 127,7 pomimo zmniejszenia predkosci")

print("\n")
print("----------------------------------------------3--------------------------------------------")
print("\n")

#H0: Średnia wytrzymałość na ciśnienie wewnętrzne butelek wynosi 1.20 N/mm^2 lub więcej.
#H1: Średnia wytrzymałość na ciśnienie wewnętrzne butelek jest mniejsza niż 1.20 N/mm^2.


# czasy netto próbki
wytrzymalosc = [1.36, 1.14, 1.27, 1.15, 1.20, 1.29, 1.27, 1.18, 1.23, 1.36, 1.38, 1.37, 1.30, 1.21, 1.33, 1.28, 1.32,
1.29, 1.33, 1.25]

# Przeprowadź test t-studenta
statystyka_T, p_wartosc = stats.shapiro(baterie)

# Wyświetl wyniki
print("Statystyka testowa:", statystyka_T)
print("P-wartość:", p_wartosc)

# Sprawdź istotność statystyczną na poziomie alfa = 0.05
alfa = 0.05
if p_wartosc > alfa:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej - rozklad jest normalny i przewyzsza 1.20 N/mm^2")
else:
    print("Odrzucamy hipoteze zerową, rozklad nie jest normalny i spada ponizej 1.20 N/mm^2")

print("\n")
print("-----------------------------------4-------------------------------------------------------")
print("\n")

#H0: (μ_1 =μ_2) nie nastapil istotny spadek zanieczyszczen
#H1: (μ_1>μ_2) nastapil istotny spadek zanieczyszczen

# Wyniki przed
wyniki_przed = [220, 185, 270, 285, 200, 295, 255, 190, 225, 230]

# Wyniki po
wyniki_po = [190, 175, 215, 260, 215, 195, 260, 150, 155, 175]

# Poziom istotności
alpha = 0.05

# Przeprowadzenie testu t dla dwóch niepowiązanych próbek
t_statistic, p_value = stats.ttest_rel(wyniki_po, wyniki_przed, alternative='greater')

# Wyświetlenie wyników testu
print("Statystyka t:", t_statistic)
print("Wartość p:", p_value)

# Sprawdzenie warunku na istotność statystyczną
if p_value < alpha:
    print("\nNa podstawie tej próby można stwierdzić, że nastapil istotny spadek zanieczyszczen.")
else:
    print("\nNie ma wystarczających dowodów na to, że nie nastapil istotny spadek zanieczyszczen.")


