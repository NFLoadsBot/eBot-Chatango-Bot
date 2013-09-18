#Imports

import ch
import random
import time

owners = ['']   #Put your chatango name here
error = ("Oops. Something went wrong D:")    #Error message

#setting colors

class TestBot(ch.RoomManager):
  def onInit(self):
    self.setNameColor("0000f7")
    self.setFontColor("7007ad")
    self.setFontFace("1")
    self.setFontSize(13)
    self.enableBg()  
    self.enableRecording()

#connecting and disconnecting crap

  def onConnect(self, room):
    print("[+] Connected to "+room.name)

  def onReconnect(self, room):
    print("[+] Reconnected to "+room.name)
  
  def onDisconnect(self, room):
    print("[+] Disconnected from "+room.name)

#setting up commands

  def onMessage(self, room, user, message):
    print(room.name + " - " + user.name + ": " + message.body)
    if self.user == user: return
    if message.body[0] == "!":
      data = message.body[1:].split(" ", 1)
      if len(data) > 1:
        cmd, args = data[0], data[1]
      else:
        cmd, args = data[0], ""


#commands section

      if cmd == "test":
        room.message("Test Worked")
        
      elif cmd == "slap":
        if not args == "":
          if args in owners:
            room.message("No! I wont slap my owner!")
          else:
            room.message("*slaps "+args+"*")
        else:
          room.message("Who do I slap? O.o")




#extra crap

  def onUserCountChange(self, room):
    print("Users: " + str(room.usercount))

  def onFloodWarning(self, room):
    room.reconnect()
    print("[+] Reconnecting...")

  def onPMMessage(self, pm, user, body):
    print("PM - "+user.name+": "+body)
    pm.message(user, "Please talk to me owner, CHATANGO_NAME, Instead!")

if __name__ == "__main__":
        TestBot.easy_start()
