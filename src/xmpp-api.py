import sys
import slixmpp
import asyncio

# Solves conflict with socket dependencies
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class XMPPConn(slixmpp.ClientXMPP):
  def __init__(self, username, password):
    super().__init__(username, password)
    self.add_event_handler('session_start', self.start)
    self.add_event_handler('message', self.message)
    # self.roster contains buddy list
  
  async def start(self, event):
    self.send_presence()
    await self.get_roster()

  async def message(self, msg):
    print('Roster: ')
    print(self.roster)
    print('Received')
    print(msg)
    if msg['type'] == 'chat' or msg['type'] == 'normal':
      self.send_message(mto=msg['from'], mbody='Thanks for sending:\n%s' % msg['body'], mtype='chat')

user = 'martspain_test@alumchat.fun'
password = '123456'

conn = XMPPConn(user, password)
conn.connect(use_ssl=False, disable_starttls=True)

print(conn.roster)

while True:
  inp = input("Continue? y/n: ")
  if inp == "y" or inp == 'Y':
    conn.process()
  else:
    conn.disconnect(3, ignore_send_queue=True)
    print("Bye")
