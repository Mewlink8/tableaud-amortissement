s = int(input("Entrer le montant du pret ou du credit : "))
t = float(input("Entrer le taux annuel : "))
n = int(input("Entrer le nombre d'annee : "))
tm = (1+t/100)**(1/12)-1
a = (1+tm)**(12*n)
m = s*tm*a/(a-1)

print("La mensualite avec interets est de",round(m,2),"euros")
print("Le montant des interets remboursÃ©s sont de",round(m*12*n-s,2),"euros")
print("Le taux mensuel est de ",tm)
print()
print("Mois - Mensualite - Interets - capital remboure - capital restant - interet rembourse" )

ir=0
for j in range (n*12):
    i=tm*s
    cr=m-i
    crd=s-cr
    ir=i+ir
    print("",j+1,"  - ",round(m,1),"     - ",round(i,1),"   - ",round(cr,1),"            - ",round(crd,1),"        - ",round(ir,2))
    s=crd
