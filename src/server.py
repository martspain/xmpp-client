import sys
import slixmpp
import asyncio

from slixmpp.exceptions import IqError, IqTimeout


# Solves conflict with socket dependencies
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class XMPPConn(slixmpp.ClientXMPP):
  def __init__(self, username, password):
    super().__init__(username, password)
    self.localUser = username
    self.contacts = {}
    # self.roster contains buddy list
  
    self.add_event_handler('session_start', self.start)
    self.add_event_handler('message', self.message)
    self.add_event_handler("got_online", self.gotOnline)

  async def start(self):
    self.send_presence()
    await self.get_roster()

  def message(self, msg):
    print('Roster: ')
    print(self.roster)
    print('Received')
    print(msg)
    if msg['type'] == 'chat' or msg['type'] == 'normal':
      self.send_message(mto=msg['from'], mbody='Thanks for sending:\n%s' % msg['body'], mtype='chat')
  
  def gotOnline(self, ev):
    user = str(ev['from'])
    if 'conference' in user:
      return
    user =  user = user[:user.index("@")]
    try:
      showStr = str(ev['show'])
      statusStr = str(ev['status'])
    except:
      showStr = "AVAILABLE"
      statusStr = "AVAILABLE"

    self.contacts[user] = {
      "from": user, 
      "show": showStr, 
      "status": statusStr
    }

  def addContact(self, recipient):
    try:
      self.send_presence_subscription(recipient, self.localUser)
      return True
    except:
      return False

  def getContacts(self):
    iterContacts = self.roster[self.localUser]
    contacts = []

    for con in iterContacts.keys():
      if con != self.localUser:
        if con in self.contacts.keys():
          info = self.contacts[con]['show']
          status = self.contacts[con]['status']
          resp = {
            "user": con,
            "info": info,
            "status": status
          }
          contacts.append(resp)
        else:
          resp = {
            "user": con,
            "info": "UNAVAILABLE",
            "status": "UNAVAILABLE"
          }
          contacts.append(resp)

    return contacts
  
  async def endSession(self):
    try:
      await self.disconnect(3, ignore_send_queue=True)
      return True
    except:
      return False



# user = 'martspain_test@alumchat.fun'
# password = '123456'

# conn = XMPPConn(user, password)
# conn.connect(use_ssl=False, disable_starttls=True)


# while True:
#   inp = input("Continue? y/n: ")
#   if inp == "y" or inp == 'Y':
#     conn.process(forever=False)
#   else:
#     conn.disconnect(3, ignore_send_queue=True)
#     print("Bye")

# conn.disconnect(3, ignore_send_queue=True)