# Python_P7_Supligeon_Thomas_22062023
# Script de recherche de combinaison d'actions rentables

Ce script en Python permet de rechercher la combinaison d'actions la plus rentable, tout en respectant une limite de dépenses de 500 euros. Le script se base sur un fichier CSV contenant les données des actions disponibles.

## Prérequis

- Python 3.x
- Bibliothèque CSV (incluse dans la distribution standard de Python)

## Instructions

1. Assurez-vous d'avoir un fichier CSV contenant les données des actions dans le même répertoire que le script. Le fichier CSV doit avoir la structure suivante :

```
Action #,Coût par action (en euros),Bénéfice (après 2 ans)
Action-1,20,5%
Action-2,30,10%
Action-3,50,15%
...
```

2. Remplacez le nom du fichier CSV par votre fichier de données dans la ligne suivante du script :

```python
with open("data.csv", "r") as file:
```

3. Exécutez le script à l'aide de la commande `python script.py` dans votre terminal.

4. Le script trouvera la combinaison d'actions la plus rentable en respectant la limite de dépenses de 500 euros. Les résultats seront affichés à la fin de l'exécution.

## Fonctionnement du script

Le script utilise une approche de force brute pour explorer toutes les combinaisons possibles d'actions. Il crée des instances de la classe `Client` pour représenter différentes combinaisons d'actions et calcule le bénéfice total pour chaque combinaison.

La fonction `brute_force` est utilisée pour itérer sur toutes les actions possibles et construire les combinaisons. La fonction `solvability` vérifie si une combinaison d'actions est réalisable en fonction du budget restant.

## Avertissement

Le script effectue une recherche exhaustive, ce qui peut prendre du temps si le nombre d'actions est élevé. Assurez-vous d'avoir suffisamment de ressources et de patience pour exécuter le script en fonction de vos données spécifiques.
