
import requests
import json

class GetPrograms:

  def get_programs(self):

    URL = "https://api.openbrewerydb.org/v1/breweries"

    response = requests.get(URL)
    return response.content
  
  def program_types(self):
    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
      programs_list.append(program["name"])
    return programs_list

# programs = GetPrograms().get_programs()
# print(programs)
programs = GetPrograms()
types = programs.program_types()

for name in set(types):
  print(name)