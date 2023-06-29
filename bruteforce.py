import csv
import copy

actions = []

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        actions.append(row)
actions.pop(0)


class Client:
    def __init__(self, wallet=500):
        self.pesonal_action = []
        self.benefice = 0
        self.wallet = wallet
        self.total_price = 0

    def __str__(self):
        str_actions = ""

        for action in self.pesonal_action:
            str_actions += action[0]
            str_actions += ", "

        return (
            "benefice = "
            + str(round(self.benefice, 2))
            + " €, pour "
            + str(len(self.pesonal_action))
            + " actions achetées ("
            + str_actions
            + ")"
            + str(self.total_price)
        )

    def already_have_action(self, action_name):
        for action in self.pesonal_action:
            if action[0] == action_name:
                return False
        return True

    def add_action_to_personal(self, action):
        self.pesonal_action.append(action)
        self.wallet -= int(action[1])

        pourcentage_str = action[2]

        self.benefice += int(action[1]) * (float(pourcentage_str.rstrip("%")) / 100)
        self.total_price += int(action[1])

# faire une fonction qui en plus de tout ca verifie le coté investissment/rentabilité


def brute_force(clt):
    p_client = copy.deepcopy(clt)
    if solvability(clt):
        for action in actions:
            v_client = copy.deepcopy(p_client)

            if v_client.wallet >= int(action[1]) and v_client.already_have_action(
                action[0]
            ):
                v_client.add_action_to_personal(action)

                if clt.benefice < v_client.benefice:
                    clt = copy.deepcopy(v_client)
    if clt.wallet > 0 and solvability(clt):
        clt = copy.deepcopy(brute_force(clt))

    return clt


def solvability(clt):
    l_of_actions_not_own = []
    for action in actions:
        if clt.already_have_action(action[0]):
            l_of_actions_not_own.append(action)

    for action in l_of_actions_not_own:
        if clt.wallet > int(action[1]):
            return True
    return False


test = Client()
rere = brute_force(test)
print(rere)
