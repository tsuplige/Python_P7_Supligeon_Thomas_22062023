# programmation dynamique / probleme du sac a dos
import csv
import sys
from tqdm import tqdm

l_of_actions = []
if __name__ == '__main__':
    actions = []
    if len(sys.argv) > 1:
        try:
            print("le programme se lance sur le fichier :", sys.argv[1])
            with open(f"datas/{sys.argv[1]}.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    l_of_actions.append(row)
            l_of_actions.pop(0)
        except FileNotFoundError:
            print("aucun fichier avec ce nom, le programme "
                  "sera lancer avec les données de base.")
    else:
        with open("datas/dataset2_Python+P7.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                l_of_actions.append(row)
        l_of_actions.pop(0)


def clean_action_tab(actions: list, ans: bool):
    if ans is True:
        for action in l_of_actions:
            if action[1][0] == '-':
                action[1] = action[1][1:]
            action[1] = int(float(action[1]) * 100)
            action[2] = round(action[1] * (float(action[2][:-1])/100), 2)/100
    else:
        for action in l_of_actions:
            action[1] = action[1]/100
    return actions


def sac_a_dos(budget: int, actions: list):
    budget *= 100
    matrice = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]
    actions = clean_action_tab(actions, True)
    action_acheter = []
    n = len(actions)

    for a in tqdm(range(1, len(matrice))):
        for c in range(1, budget + 1):
            if c >= actions[a - 1][1]:
                matrice[a][c] = max(matrice[a][c-1],
                                    actions[a - 1][2] +
                                    matrice[a - 1][c - actions[a - 1][1]],
                                    matrice[a - 1][c])
            else:
                matrice[a][c] = matrice[a][c-1]

    while budget >= 0 and n >= 0:
        e = actions[n-1]
        if matrice[n][budget] == matrice[n-1][budget-e[1]] + e[2]:
            action_acheter.append(e)
            budget -= e[1]

        n -= 1

    action_acheter = clean_action_tab(action_acheter, False)

    return matrice[-1][-1], action_acheter


if __name__ == '__main__':
    best_gain, best_comb = sac_a_dos(500, l_of_actions)
    best_actions_name = [action[0] for action in best_comb]
    best_actions_str = ", ".join(best_actions_name)
    print(f"le meilleur gain est de {best_gain} € pour "
          f"l'achat des actions suivante: ({best_actions_str})")
