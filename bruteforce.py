import csv
from dataclasses import dataclass
from itertools import combinations
import sys


@dataclass
class Action:
    name: str
    price: float
    profit: float


if __name__ == '__main__':
    actions = []
    if len(sys.argv) > 1:
        try:
            print("le programme se lance sur le fichier :", sys.argv[1])
            with open(f"datas/{sys.argv[1]}.csv", "r") as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    if i == 0:
                        continue
                    actions.append(Action(row[0], float(row[1]), float(row[2].replace("%", ""))/100))
        except FileNotFoundError:
            print("aucun fichier avec ce nom, le programme "
                  "sera lancer avec les données de base.")
    else:
        with open("datas/data.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                actions.append(Action(row[0], float(row[1]), float(row[2].replace("%", ""))/100))


def get_all_combinations(actions: list[Action]) -> list[tuple[Action]]:
    combs = []
    for n in range(len(actions)):
        combs += list(combinations(actions, n))
    return combs


def found_best_combination(combs: list[tuple[Action]]):
    max_gain = 0
    max_comb = None
    for comb in combs:
        if sum([a.price for a in comb]) > 500:
            continue
        gain = sum([a.price * a.profit for a in comb])
        if gain > max_gain:
            max_gain = gain
            max_comb = comb

    return max_gain, max_comb


if __name__ == '__main__':
    combs = get_all_combinations(actions)
    best_gain, best_comb = found_best_combination(combs)
    best_actions_name = [action.name for action in best_comb]
    best_actions_str = ", ".join(best_actions_name)
    print(f"le meilleur gain est de {best_gain} € pour "
          f"l'achat des actions suivante: {best_actions_str}")
