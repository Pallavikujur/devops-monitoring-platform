print("Monitoring Validation Started")

import json
with open("../payloads/request.json" as file, "r"):
  content = json.load(file)

print("Hostname:", content["hostname"])

