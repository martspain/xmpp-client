import sys
from datetime import datetime
from utils import console_colors
from client import Client
import asyncio
# import nest_asyncio
# nest_asyncio.apply()
# __import__('IPython').embed()

# Solves conflict with socket dependencies
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# String constants
todayDate = datetime.today().strftime("%B / %d / %Y")
strSeparator = "----------------------------------------------------"

# Banner
print(f"{console_colors.HEADER}{strSeparator}{console_colors.ENDC}")
print(f"{console_colors.HEADER}{console_colors.BOLD}Welcome to the Alumn Chat for Networking Class 2022{console_colors.ENDC}{console_colors.ENDC}")
print(f"{console_colors.HEADER}{console_colors.BOLD}Author: Martín España{console_colors.ENDC}{console_colors.ENDC}")
print(f"{console_colors.HEADER}{console_colors.BOLD}{todayDate}{console_colors.ENDC}{console_colors.ENDC}")
print(f"{console_colors.HEADER}{strSeparator}{console_colors.ENDC}")


async def runChat():
  cl = Client()

  await cl.exec()

asyncio.run(runChat())
