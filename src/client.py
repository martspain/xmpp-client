import threading
import slixmpp
import time
from utils import console_colors
from server import XMPPConn
from slixmpp.exceptions import IqError, IqTimeout
from getpass import getpass # This is to ask for password
# import nest_asyncio
# nest_asyncio.apply()
# __import__('IPython').embed()

class Client:
  def __init__(self):
    self.isRunning = True
    self.isLoggingIn = True
    self.isActive = False
    self.username = ""
    self.strSeparator = "----------------------------------------------------"
  
  # def mainThread(self, stopping):
  #   while True:
  #     try:
  #       self.conn.process(forever=True, timeout=3)
  #     except IqError:
  #       print("ERROR IN SERVER")
  #     if stopping():
  #       break

  #     time.sleep(0.2)

  async def loginMenu(self):
    while self.isLoggingIn:
      print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
      print(f"{console_colors.OKGREEN}LOG IN{console_colors.ENDC}")
      print(f"{console_colors.OKGREEN}{self.strSeparator} \n{console_colors.ENDC}")

      userNameInvalid = True

      # Validate user syntax
      while userNameInvalid:
        print(f"{console_colors.OKCYAN}Please, enter your XMPP address (e.g. {console_colors.ENDC}{console_colors.OKGREEN}username@xmpptest.com{console_colors.ENDC}{console_colors.OKCYAN}){console_colors.ENDC}")
        self.username = input("user@domain: ")
        if "@" in self.username:
          userNameInvalid = False
        else:
          print(f"{console_colors.WARNING}{console_colors.BOLD}\n### WARNING ###{console_colors.ENDC}{console_colors.ENDC}")
          print(f"{console_colors.WARNING}Username is incorrect.{console_colors.ENDC}")
          print(f"{console_colors.WARNING}Please use the correct syntax (username@domain) \n{console_colors.ENDC}")

      print(f"{console_colors.OKCYAN}Please, enter your XMPP address{console_colors.ENDC}")
      password = getpass()

      # CALL AUTH METHOD
      try:  # Login Success
        self.conn = XMPPConn(self.username, password)
        self.conn.connect(use_ssl=False, disable_starttls=True)
        await self.conn.start()
        # await self.conn.process(forever=False)

        # self.stopThreading = False
        # self.mainThread = threading.Thread(target = self.mainThread, args=(lambda : self.stopThreading,))
        # self.mainThread.start()

        # time.sleep(3)
        # self.conn.process(forever=False)

        self.isLoggingIn = False
        print(f'{console_colors.OKGREEN}Login Successful!{console_colors.ENDC}')
        return True
      except IqError: # Login Credential Error
        self.isLoggingIn = True
        print(f"{console_colors.FAIL}{console_colors.BOLD}\n### ERROR ###{console_colors.ENDC}{console_colors.ENDC}")
        print(f"{console_colors.FAIL}Credentials are incorrect.{console_colors.ENDC}")
        print(f"{console_colors.FAIL}Please check your credentials and try again. \n{console_colors.ENDC}")
      except: # Any other error, probably from server
        self.isLoggingIn = False
        print(f"{console_colors.FAIL}{console_colors.BOLD}\n### ERROR ###{console_colors.ENDC}{console_colors.ENDC}")
        print(f"{console_colors.FAIL}Error from server.{console_colors.ENDC}")
        print(F"{console_colors.FAIL}Please check your connection, and try again. \n{console_colors.ENDC}")
        return False

  async def exec(self):
    # Main Menu
    while self.isRunning:
      print("Hello! What do you want to do?")
      print(f"1. {console_colors.OKCYAN}Log In{console_colors.ENDC}")
      print(f"2. {console_colors.OKCYAN}Create Account{console_colors.ENDC}")
      print(f"3. {console_colors.OKCYAN}Help{console_colors.ENDC}")
      print(f"4. {console_colors.OKCYAN}Exit Client{console_colors.ENDC}")
      
      mainOpt = input(f"{console_colors.OKBLUE}{console_colors.BOLD}>>> {console_colors.ENDC}{console_colors.ENDC}{console_colors.OKGREEN}{console_colors.BOLD}")

      print(f"{console_colors.ENDC}{console_colors.ENDC}")

      # LOG IN
      if mainOpt == "1":
        self.isLoggingIn = True
        success = await self.loginMenu()

        if success:
          self.isActive = True
          await self.loggedMenu()

      # CREATE ACCOUNT
      elif mainOpt == "2":
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}CREATE ACCOUNT{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")

        userNameInvalid = True
        newUsername = ""

        # Validate user syntax
        while userNameInvalid:
          print(f"{console_colors.OKCYAN}Please, enter your XMPP address (e.g. {console_colors.ENDC}{console_colors.OKGREEN}username@xmpptest.com{console_colors.ENDC}{console_colors.OKCYAN}){console_colors.ENDC}")
          newUsername = input("user@domain: ")
          if "@" in newUsername:
            userNameInvalid = False
          else:
            print(f"{console_colors.WARNING}{console_colors.BOLD}\n### WARNING ###{console_colors.ENDC}{console_colors.ENDC}")
            print(f"{console_colors.WARNING}Username is incorrect.{console_colors.ENDC}")
            print(f"{console_colors.WARNING}Please use the correct syntax (username@domain) \n{console_colors.ENDC}")
          
        password = getpass()

        # try:
        self.conn = XMPPConn(self.username, password)
        self.conn.connect(use_ssl=False, disable_starttls=True)
        await self.conn.start()
        # regSuccess = await self.conn.registerNew()
        
        # if regSuccess:
        #   print(f"{console_colors.OKGREEN}Account succesfully created.{console_colors.ENDC}")
        # else:
        #   print(f"{console_colors.FAIL}Error creating account. Please try again.{console_colors.ENDC}")
        # except:
        #   print(f"{console_colors.FAIL}Error creating account. Please try again.{console_colors.ENDC}")


      # SHOW INSTRUCTIONS
      elif mainOpt == "3":
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}HELP{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")

        print(f"{console_colors.OKCYAN}{self.strSeparator}")
        print("Select the option you want from the console menu. For more details visit: https://github.com/martspain/xmpp-client/blob/main/README.md")
        print(f"{self.strSeparator}{console_colors.ENDC}")

      # EXIT APPLICATION
      elif mainOpt == "4" or mainOpt == "exit" or mainOpt == "esc" or mainOpt == "0" or mainOpt == "/exit":
        self.isRunning = False
        print(f"{console_colors.OKBLUE}{self.strSeparator}")
        print("Thanks for using this XMPP client. Come back soon!")
        print(f"{self.strSeparator}{console_colors.ENDC}")

      # INVALID OPTION
      else:
        print(f"{console_colors.WARNING}{console_colors.BOLD}\n### WARNING ###{console_colors.ENDC}{console_colors.ENDC}")
        print(f"{console_colors.WARNING}- {mainOpt} - is not an option.{console_colors.ENDC}")
        print(f"{console_colors.WARNING}Please enter a valid option... \n{console_colors.ENDC}")
  
  async def loggedMenu(self):
    # Session is active and user is logged in
    while self.isActive:
      print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
      print(f"{console_colors.OKGREEN}Welcome {self.username}{console_colors.ENDC}")
      print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")

      print("What do you feel like doing today?")
      print(f"1. {console_colors.OKCYAN}Show Contacts{console_colors.ENDC}")
      print(f"2. {console_colors.OKCYAN}Add Contact{console_colors.ENDC}")
      print(f"3. {console_colors.OKCYAN}Contact Details{console_colors.ENDC}")
      print(f"4. {console_colors.OKCYAN}Open Chat{console_colors.ENDC}")
      print(f"5. {console_colors.OKCYAN}Send Message{console_colors.ENDC}")
      print(f"6. {console_colors.OKCYAN}Set Status{console_colors.ENDC}")
      print(f"7. {console_colors.OKCYAN}Log Out{console_colors.ENDC}")
      
      opt = input(f"{console_colors.OKBLUE}{console_colors.BOLD}>>> {console_colors.ENDC}{console_colors.ENDC}{console_colors.OKGREEN}{console_colors.BOLD}")

      print(f"{console_colors.ENDC}{console_colors.ENDC}")

      # SHOW CONTACTS
      if opt == "1":
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}SHOW CONTACTS{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator} \n{console_colors.ENDC}")

        contacts = self.conn.getContacts()
        
        print(f"{console_colors.OKGREEN}#\t|\t\t\tContact\t\t\t|\tStatus\t\t|{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
        
        for n in range(len(contacts)):
          current = contacts[n]
          name = current['user']
          stat = current['status']
          print(f"{console_colors.OKGREEN}{n+1}.\t\t{console_colors.ENDC}{console_colors.OKCYAN}{name}\t\t\t\t{stat}{console_colors.ENDC}")

      # ADD CONTACT
      elif opt == "2":
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}ADD CONTACT{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator} \n{console_colors.ENDC}")

        newFriend = input("Enter new contact username: ")
        success = self.conn.addContact(newFriend)

        if success:
          print(f"{console_colors.OKGREEN}Invitation succesfully sent!{console_colors.ENDC}")
        else:
          print(f"{console_colors.FAIL}Invitation could not be sent :({console_colors.ENDC}")

      # CONTACT DETAILS
      elif opt == "3":
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}CONTACT DETAILS{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator} \n{console_colors.ENDC}")

        contacts = self.conn.getContacts()

        friend = input("Enter contact username: ")

        print(f"\n{console_colors.OKGREEN}Contact\t\t\t\t\t|\tStatus\t\t|{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")

        hasFound = False
        for con in contacts:
          name = con["user"]
          stat = con["status"]
          if friend == con["user"]:
            hasFound = True
            print(f"{console_colors.OKCYAN}{name}\t\t{stat}{console_colors.ENDC}")
        
        if not hasFound:
          print(f"{console_colors.WARNING}User was not found in your contact list.{console_colors.ENDC}")

      # OPEN CHAT
      elif opt == "4":
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}OPEN CHAT{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator} \n{console_colors.ENDC}")
        self.conn.process(forever=False)

      # SEND MESSAGE
      elif opt == "5":
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}SEND MESSAGE{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator} \n{console_colors.ENDC}")

        contacts = self.conn.getContacts()
        
        print(f"{console_colors.OKGREEN}#\t|\t\t\tContact\t\t\t|\tStatus\t\t|{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
        
        for n in range(len(contacts)):
          current = contacts[n]
          name = current['user']
          stat = current['status']
          print(f"{console_colors.OKGREEN}{n+1}.\t\t{console_colors.ENDC}{console_colors.OKCYAN}{name}\t\t\t\t{stat}{console_colors.ENDC}")
        
        try:
          friendOpt = int(input("Choose the number of the user you want to send a message to: "))
          destiny = contacts[friendOpt - 1]
          destName = destiny["user"]

          mssg = input("Enter your message: ")

          self.conn.sendPrivateMessage(destName, mssg)
          # self.conn.process(forever=False, timeout=3)

        except:
          print(f"{console_colors.WARNING}Not valid input. Please try again.{console_colors.ENDC}")

      # SET STATUS
      elif opt == "6":
        print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}SET STATUS{console_colors.ENDC}")
        print(f"{console_colors.OKGREEN}{self.strSeparator} \n{console_colors.ENDC}")

      # LOGOUT
      elif opt == "exit" or opt == "esc" or opt == "0" or opt == "/exit" or opt == "7":
        self.isActive = not await self.conn.endSession()
        if self.isActive:
          print(f"{console_colors.FAIL}{console_colors.BOLD}\n### Error ###{console_colors.ENDC}{console_colors.ENDC}")
          print(f"{console_colors.FAIL}Failed to logout.{console_colors.ENDC}")
          print(f"{console_colors.FAIL}Please try again later. \n{console_colors.ENDC}")
        else:
          # self.stopThreading = True
          # self.mainThread.join()
          print(f"{console_colors.OKGREEN}{self.strSeparator}{console_colors.ENDC}")
          print(f"{console_colors.OKGREEN}Logout Successful{console_colors.ENDC}")
          print(f"{console_colors.OKGREEN}{self.strSeparator}\n{console_colors.ENDC}")
      
      # INVALID OPTION
      else:
        print(f"{console_colors.WARNING}{console_colors.BOLD}\n### WARNING ###{console_colors.ENDC}{console_colors.ENDC}")
        print(f"{console_colors.WARNING}- {opt} - is not an option.{console_colors.ENDC}")
        print(f"{console_colors.WARNING}Please enter a valid option... \n{console_colors.ENDC}")
