print("Monitoring Validation Started")

import json
with open("../payloads/request.json","r")as file:
  content = json.load(file)
  print("Hostname:", content["hostname"])
  if (content["hostname"] == ""):
      print("validation failed")
  else:
      print("validation successfull")
    
    
  




