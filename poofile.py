#le poo associe a python

class Car:

    def __init__(self,marque,color,price,model):
        self.marque=marque
        self.color=color
        self.price=price
        self.model=model

    def traitercommande(self):
        print("ilfaut d'aord recevoir la commande")
        print(self.marque)
        print(self.color)

    def test(self):
        print("le test ici revies a verifier si tout  est ok pour la commande")

    def achat(self):
        print("il reviet a fialiser l'achat du vehicule")