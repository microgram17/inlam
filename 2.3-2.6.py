from fractions import Fraction

#2.3
grader_f = int(input("Skriv temperaturen i F för att convertera: "))
grader_c = ((grader_f-32)*5)/9
print ("Celsius: " + str(grader_c))

#2.4
mile = float(input("Hur många miles/gallon: "))
litermil = ((mile / 6.215)/3.785)
print("Det är: {:.3f}".format(litermil) + " liter/mil")

#2.5





#2.6
amount = float(input("mängd 14C: "))
years = float(input("antal år: "))
halflife = 5730

kvar = amount * (1/2) ** (years / halflife)
prcnt = (kvar / amount) * 100

print(f"Efter {years:.0f} år så är det {prcnt:.1f}% kvar")