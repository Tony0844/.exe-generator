import os
import subprocess
from os import system


if system("cls") != 0: system("clear")

# Borra comillas y normaliza la ruta
def clean_route(route):
    route = route.strip()
    if (route.startswith('"') and route.endswith('"')) or \
       (route.startswith("'") and route.endswith("'")):
        route = route[1:-1]
    return route.replace("\\", "/")


while True:
    script_route = clean_route(input("File route: "))
    if os.path.exists(script_route) and os.path.isfile(script_route):
        break
    else:
        print("Invalid route. Try again\n")


icon_option = input("Do you want a special icon in your script? (Y/N): ").upper()

if icon_option == "Y":
    while True:
        icon_route = clean_route(input("Icon route (.ico con tamaños: x16, x32, x48, x256): "))
        if os.path.exists(icon_route) and os.path.isfile(icon_route):
            break
        else:
            print("Invalid route. Try again\n")
    
    # Ejecutar con icono
    subprocess.run(f'start cmd /k pyinstaller --onefile --icon="{icon_route}" "{script_route}"', shell=True)

elif icon_option == "N":
    # Ejecutar sin icono
    subprocess.run(f'start cmd /k pyinstaller --onefile "{script_route}"', shell=True)
else:
    print("Invalid option. Use Y or N.")
