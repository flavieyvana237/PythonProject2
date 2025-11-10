#les bases en python

#les variables string
import random
import math
import libb
from poofile import Car
from logging import exception

nom="flavie"
prenom="Meffo"
age=22
ageN=age+7
print("Bonjour" +(" ")+(nom)+(" ")+(prenom)+(" ")+ "vous avez actuellement "+str(age)+"et dans 7ans vous auriez "+str(ageN+4))
print(ageN+1)
#les booleens

debutant = True
maitre=False
expert=False
print("vous etes debutant? "+str(debutant))

#les methodes en python

name="flavie meffo"
print(len(name))#pourcmpterle nombre de caractere
print(name.find("e"))
print(name.lower())
print(name.capitalize())
print(name.upper())
print(name.isalnum())
print(name.isalpha())
print(name.isdigit())

#LES CASTING EN PITYON

y=10
x=12.5
z=9
print(y+x)
print(y-12)
message="felicitation!"
print(message*3)

#fct pour recuperer ue valeur etre par le user

mam= input("etre votre name")
print("hello "+mam+" welcome ")
#les fct e pytho

x1=12
y2=50
z2=-65
print(max(x1,y2,z2))
print(min(x1,y2,z2))
print(math.sqrt(x1**2+y2**2+z2))

#les idexation en python et les slife

my_star="hello geie meffo good"
print(my_star[0:-5])

#les conditions
moy=float(input("entrez votre moy"))

if moy==20:
    print("mension parfait")
elif moy>=18:
    print("mension excelente")
elif moy>=16:
    print("mension tres bien")
elif moy>=14:
    print("mension bien")
elif moy>=12:
    print("mension assez-bien")
elif moy>=10:
    print("mension passable")
else:
    print("faible vous devriez fournir plus d'effort")


    #revision sur les and, or,...
    #programme qui determine la temperature

    temp=int(input("entrez la temperature"))

    if temp>= 0 and temp<= 30:
        print("il faire beau temps")
    elif temp< 0 or temp> 30:
        print("il ne fait pas beau temps")

#LES LISTES EN PYTHON bn

fruits=["orage", "tomate", "pasteck", "pomme"]
fruits.pop()
fruits.reverse()
print(fruits)

#les boucles while et for
for index, fruits in enumerate(fruits):
    print(str(index+1)+"."+ fruits)

    #la  while, breack
while True:
    user=input("wath is your are name?")
    if user=="":
        print("hello "+user)
        break

for i in range(110):
    if i%2==0:

        print(i)
        #print("voici les omres paix")

#LES tuples en python

personne = ("nom", "prenom","age", "moy","meffo")
#for element in personne:
print(personne.count("moy"))

#les set en python

menu={"riz","pomme saute","koki","poisson braise", "poulet","couscous kui"}
dessert={"orange","pasteck","appel","mandarine", "salade","koki"}
menu.add("ndole")
print(menu)
menu.remove("poulet")

dessert.difference(menu)

#les listes a doule dim

etudiant=["meffo","flvie",22,"gl"]

#les fcts

def perimetre(long,larg):
    p=(long+larg)*2
    return p
    s=perimetre(50,27)
    print("le perimetre de rectangle est "+s)


#les dictionnaires en python

capitals={
        "cameroun":"yaounde",
        "france":"paris",
        "usa":"watchitho",
        "philipine":"many",
        "india":"deli",
        "italie":"italia"
    }
#print(capitals)
print(capitals.keys())

#nested fct call
#nombre=input("entrez un nombre")
#nombre=float(nombre)
#nombre=abs(nombre)
#nombre=round(nombre)
#print(nombre)
#ou encore
print(round(abs(float(input("enter a number :")))))

#les str.format

n="Flavie"
w="developpeur"
pi=3.1417432297
m=659043
print("{} a pour profession {}".format(n,w))
print("d'apres les calcul de mr le nre pi donne: {:.2f}".format(pi))
print("pi en biaire donne:{:b}".format(m))
print("pi en hexadecimal donne:{:X}".format(m))
print("pi en exponnenciel donne:{:e}".format(m))


#la methode ramdon en python qui permet de creer des jeux videos

f=random.randint(1,100)
print(f)
lait=['nido','neslest','broli','topmiel','tompi']
u=random.choice(lait)
print(u)

#les exceptions pour gerer les erreurs

try:
    num=int(input("numerateur"))
    den=int(input("denomiateur"))
    result=num/den
    #print(result)
except ZeroDivisionError:
    print("vous ne pas diviser un nombre par zero")

except ValueError:
    print("seul les chiffres sont accepter pour les divisions")

except Exception:
    print("il y'a une erreur de division!")
else:
    print(result)
finally:
    print("voici le resultat")

    #les concept os et file epython qui permet de commuiquer avec le SE
    #creer les fichiers , inserer dans les fichiers, copy, verifier s'il existe,...

    #les modules en programmation
libb.modul()
libb.mathcalcul(14,8)
print(libb.mathcalcul(7,5))


#un code pour les aux harza avec random


#le poo
car1 = Car("flavietessac","violet",5000000,"tessacA")
print(car1.marque)
print(car1.test())
print(car1.traitercommande())
print(car1.achat())

