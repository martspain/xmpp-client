from utils import console_colors
# from getpass import getpass 
# This is to ask for password

class Client:
  def __init__(self):
    self.isRunning = True
    self.isLoggingIn = True
    self.isActive = False
    self.username = ""
    self.strSeparator = "----------------------------------------------------"
  
  def loginMenu(self):
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
          print(F"{console_colors.WARNING}Please use the correct syntax (username@domain) \n{console_colors.ENDC}")

      print(f"{console_colors.OKCYAN}Please, enter your XMPP address{console_colors.ENDC}")
      password = input("Password: ")

      # TODO
      # CALL AUTH METHOD
      authResponse = True

      # Log In Success
      if authResponse:
        self.isLoggingIn = False
        return True
      
      # Log In Fail
      else:
        print(f"{console_colors.FAIL}{console_colors.BOLD}\n### ERROR ###{console_colors.ENDC}{console_colors.ENDC}")
        print(f"{console_colors.FAIL}Error from server.{console_colors.ENDC}")
        print(F"{console_colors.FAIL}Please check your connection, and try again. \n{console_colors.ENDC}")
        self.isLoggingIn = False
        return False

  def exec(self):
    # Main Menu
    while self.isRunning:
      print("Hello! What do you want to do?")
      print(f"1. {console_colors.OKCYAN}Log In{console_colors.ENDC}")
      print(f"2. {console_colors.OKCYAN}Create Account{console_colors.ENDC}")
      print(f"3. {console_colors.OKCYAN}Help{console_colors.ENDC}")
      print(f"4. {console_colors.OKCYAN}Exit Client{console_colors.ENDC}")
      
      mainOpt = input("Your choice: ")

      # LOG IN
      if mainOpt == "1":
        success = self.loginMenu()

        if success:
          self.isActive = True
          self.loggedMenu()

      # CREATE ACCOUNT
      elif mainOpt == "2":
        pass

      # SHOW INSTRUCTIONS
      elif mainOpt == "3":
        pass

      # EXIT APPLICATION
      elif mainOpt == "4" or mainOpt == "exit" or mainOpt == "esc" or mainOpt == "0" or mainOpt == "/exit":
        self.isRunning = False

      # INVALID OPTION
      else:
        print(f"{console_colors.WARNING}{console_colors.BOLD}\n### WARNING ###{console_colors.ENDC}{console_colors.ENDC}")
        print(f"{console_colors.WARNING}- {mainOpt} - is not an option.{console_colors.ENDC}")
        print(F"{console_colors.WARNING}Please enter a valid option... \n{console_colors.ENDC}")
  
  def loggedMenu(self):
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
      print(f"5. {console_colors.OKCYAN}Set Status{console_colors.ENDC}")
      print(f"6. {console_colors.OKCYAN}Log Out{console_colors.ENDC}")
      
      opt = input("Your choice: ")

      # SHOW CONTACTS
      if opt == "1":
        pass

      # ADD CONTACT
      elif opt == "2":
        pass

      # CONTACT DETAILS
      elif opt == "3":
        pass

      # OPEN CHAT
      elif opt == "4":
        pass

      # SET STATUS
      elif opt == "5":
        pass

      # LOGOUT
      elif opt == "exit" or opt == "esc" or opt == "0" or opt == "/exit" or opt == "6":
        self.isActive = False
      
      # INVALID OPTION
      else:
        print(f"{console_colors.WARNING}{console_colors.BOLD}\n### WARNING ###{console_colors.ENDC}{console_colors.ENDC}")
        print(f"{console_colors.WARNING}- {opt} - is not an option.{console_colors.ENDC}")
        print(F"{console_colors.WARNING}Please enter a valid option... \n{console_colors.ENDC}")
