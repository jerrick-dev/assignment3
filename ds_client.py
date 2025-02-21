# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jerrick Aguilar
# jerricka@uci.edu
# 66335000
import socket
import time
import ds_protocol as dsp
import json

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    port = 3021
    f1 = True
    f2 = True
    if bio.isspace() or len(bio) == 0 or bio is None:
      f1 = False 
    if message.isspace or len(message) == 0 or message is None:
      f2 = False

    if server is None:
      return False
    try:
      client.connect((server,port))
    except socket.error as e:
      print(f"{e}, Invalid inputs!")
      return False
    
    usert = None
    entry = None
    timemark = time.time()
    if username.isspace() or len(username) == 0 or username is None:
      return False
    if password.isspace() or len(password) == 0 or password is None:
      return False

    join = '{"join": {"username":"' + u + '", "password":"' + p + '", "token": ""}}' 
    s = client.makefile("w")
    rec = client.makefile("r")
    s.write(join + "\r\n")
    s.flush()
    res = rec.readline()[:-1]
    dsp_extract = dsp.extract_json(res)
    current = str(time.time())
    u_token = dsp_extract.token
    u_prof = dsp_extract.type
    if u_prof == 'ok':
      res = json.loads(res)
      u_token = res['response']['token']
      if f2 is True:
        post = "{\"token\":\"" + user_token
        post += "\", \"post\": {\"entry\": \""
        post += message + "\", \"timestamp\": \"" + current + "\"}}"
        assert type(post) == str, "Not a string"
        s.write(post + '\r\n')
        s.flush()
        response = rec.readline()
      else: 
        return False
      
      if f1 is True:
        user_bio = "{\"token\":\"" + user_token
        user_bio += "\", \"bio\": {\"entry\": \""
        user_bio += b + "\", \"timestamp\": \"" + current + "\"}}"
        s.write(user_bio + '\r\n')
        s.flush() 
      else:
        return False
      
      return True
  
    elif u_prof == 'error':
      return False  
