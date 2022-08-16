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
    self.add_event_handler("got_offline", self.gotOffline)
    self.add_event_handler("presence_subscribe", self._handle_new_subscription)

  async def start(self, ev=None):
    self.send_presence()
    await self.get_roster()

  def message(self, msg):
    output = ""
    if msg['type'] == 'chat' or msg['type'] == 'normal':
      output = msg['from'] + " -> " + msg['body']
    
    print(output)
    # if msg['type'] == 'chat' or msg['type'] == 'normal':
    #   self.send_message(mto=msg['from'], mbody='Thanks for sending:\n%s' % msg['body'], mtype='chat')
  
  def sendPrivateMessage(self, dest, body):
    self.send_message(mto=dest, mbody=body, mtype='chat', mfrom=self.localUser)


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
  
  def gotOffline(self, event):
    user = str(event['from'])
    if 'conference' in user:
      return

    user = user[:user.index("@")]
    self.contacts[user]["show"] = 'UNAVAILABLE'
    self.contacts[user]["status"] = 'UNAVAILABLE'

  def addContact(self, newFriend):
    try:
      self.send_presence_subscription(newFriend, self.localUser)
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
  
  def _handle_new_subscription(self, pres):
    roster = self.roster[pres['to']]
    item = self.roster[pres['to']][pres['from']]
    try_auto_sub = False

    if item['whitelisted']:
      item.authorize()
      if roster.auto_subscribe:
          try_auto_sub = True

    # Auto authorize
    elif roster.auto_authorize:
      item.authorize()
      if roster.auto_subscribe:
          try_auto_sub = True

    elif roster.auto_authorize == False:
      item.unauthorize()

    # Subscribe
    if try_auto_sub:
      item.subscribe()



# user = 'martspain_test@alumchat.fun'
# password = '123456'

# conn = XMPPConn(user, password)
# conn.connect(use_ssl=False, disable_starttls=True)

# try:
#   conn.process(forever=True)
# except:
#   conn.disconnect(3, ignore_send_queue=True)
# while True:
#   inp = input("Continue? y/n: ")
#   if inp == "y" or inp == 'Y':
#   else:
#     conn.disconnect(3, ignore_send_queue=True)
#     print("Bye")

# conn.disconnect(3, ignore_send_queue=True)