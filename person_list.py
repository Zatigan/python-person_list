from tabulate import tabulate
from faker import Faker

fake = Faker("fr_FR")

# En générant les données directement lors de la génération du tableau
print(tabulate({"Nom": [fake.name() for i in range(10)],
                "Email": [fake.email() for i in range(10)],
                "Ville": [fake.city() for i in range(10)]}, headers="keys", tablefmt="outline"))


# En créant un tableau et en insérant avec une boucle les données dans ce même tableau
