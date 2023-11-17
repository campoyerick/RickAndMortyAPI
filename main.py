import requests
import json
from tabulate import tabulate
from termcolor import colored
from colorama import Fore, Style, init

init(autoreset=True)

def get_character_data(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def print_colored(message, color=Fore.WHITE):
    print(color + message + Style.RESET_ALL)

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def print_styled(message, color='white', attrs=None):
    print(colored(message, color, attrs=attrs))

def display_character_data(data):
    table_data = [
        ["Nome", data["name"]],
        ["Status", data["status"]],
        ["Espécie", data["species"]],
        ["Tipo", data["type"]],
        ["Gênero", data["gender"]],
        ["Origem", data["origin"]["name"]],
        ["Localização", data["location"]["name"]]
    ]

    table = tabulate(table_data, headers=["Informações", "Valores"], tablefmt="fancy_grid")
    print(table)

def main():
    id = input("Digite o ID do personagem: ")
    data = get_character_data(id)

    if data is not None:
        display_character_data(data)

        filename = f"character_{id}.json"
        save_to_json(data, filename)
        print_colored(f"Dados salvos em {filename}", Fore.GREEN)
    else:
        print_styled("Personagem não encontrado.", color='red', attrs=['bold'])

if __name__ == "__main__":
    main()
