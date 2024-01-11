
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(URL)
    print(response.content)
  
programs = GetPrograms().get_programs()
print(programs)