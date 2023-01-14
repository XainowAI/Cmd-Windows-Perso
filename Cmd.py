import os
import subprocess
from colorama import Fore, Style
import ctypes
import requests
import time

def change_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

change_title("XainowAI@DualBoot: ~")


def terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTCYAN_EX + "XainowAI Terminal ", end="")
    print(Fore.LIGHTCYAN_EX + "[version 10.0.22000.1455]\n", end="")
    print(Fore.LIGHTYELLOW_EX + "(c)", end="")
    print(Fore.LIGHTRED_EX + " XainowAI Corporation. Tous droits réservés.")
    current_directory = os.getcwd()
    print(Fore.WHITE + "\n" + current_directory + ">", end="")
    while True:
        command = input()
        print()
        if command == "exit":
            break
        elif command == "help":
            print("Liste des commandes disponibles :")
            print("- exit : pour quitter le terminal")
            print("- help : pour afficher cette liste de commandes")
            print("- clear : pour nettoyer l'écran")
            print("- ip : pour afficher l'adresse IP publique")
            print("- ping : pour envoyer un paquet ping à une adresse IP ou un nom d'hôte")
            print("- pip : pour install les package")
            print("- python : pour éxécuter des fichier python")
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.LIGHTCYAN_EX + "XainowAI Terminal ", end="")
            print(Fore.LIGHTCYAN_EX + "[version 10.0.22000.1455]\n", end="")
            print(Fore.LIGHTYELLOW_EX + "(c)", end="")
            print(Fore.LIGHTRED_EX + " XainowAI Corporation. Tous droits réservés.")
            current_directory = os.getcwd()
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        elif command == "ip":
            try:
                ip = requests.get("http://ip.42.pl/raw").text
                print("Adresse IP publique : " + ip)
            except requests.ConnectionError:
                print("\nImpossible de se connecter pour obtenir l'adresse IP publique.")
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        elif command.startswith("ping "):
            try:
                hostname = command.split(" ")[1]
                subprocess.run(["ping", hostname])
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        else:
            print("Commande non reconnue, tapez 'help' pour afficher la liste des commandes disponibles.")
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        if command.startswith("pip"):
           package = command.split(" ")[2]
           subprocess.run(["pip", "install", package])
           print("Installation du package "+ package + " terminé")
           time.sleep(3.4)
           print(Fore.WHITE + "\n" + current_directory + ">", end="")
        elif command.startswith("python"):
            try:
               filename = command.split(" ")[1]
               subprocess.run(["python", filename])
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        else:
             print("Commande non reconnue, tapez 'help' pour afficher la liste des commandes disponibles.")
             print(Fore.WHITE + "\n" + current_directory + ">", end="")
                



terminal()