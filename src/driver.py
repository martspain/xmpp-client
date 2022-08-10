from datetime import datetime
from utils import console_colors
from client import Client

# String constants
todayDate = datetime.today().strftime("%B / %d / %Y")
strSeparator = "----------------------------------------------------"

# Banner
print(f"{console_colors.HEADER}{strSeparator}{console_colors.ENDC}")
print(f"{console_colors.HEADER}{console_colors.BOLD}Welcome to the Alumn Chat for Networking Class 2022{console_colors.ENDC}{console_colors.ENDC}")
print(f"{console_colors.HEADER}{console_colors.BOLD}Author: Martín España{console_colors.ENDC}{console_colors.ENDC}")
print(f"{console_colors.HEADER}{console_colors.BOLD}{todayDate}{console_colors.ENDC}{console_colors.ENDC}")
print(f"{console_colors.HEADER}{strSeparator}{console_colors.ENDC}")

cl = Client()

cl.exec()

# This will be useful for showing info as table
# print("E\t Hola")
# print("EN\t Hola")
# print("END\t Hola")
