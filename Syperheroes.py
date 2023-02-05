from pprint import pprint

import requests

class SuperHeroes:

    def __init__(self, main_resourse, additional_resourse, superheroes_list):
        self.main_resourse = main_resourse
        self.additional_resourse = additional_resourse
        self.superheroes_list = superheroes_list
        self.full_path = self.main_resourse + self.additional_resourse
    
    def get_info(self):
        # self.data_format = data_format
        response = requests.get(self.full_path)
        return response.json()
    
    def the_cleverest(self):
        
        target_dict = {}
        
        for item in self.get_info():
            
            if item['name'] in self.superheroes_list:
                target_dict[item['name']] = item['powerstats']['intelligence']
            
        for key, value in target_dict.items():
            if value == max(list(target_dict.values())):
                return key

if __name__ == '__main__':

    intell = SuperHeroes('https://akabab.github.io/superhero-api/api', '/all.json', ['Hulk', 'Captain America', 'Thanos'])
    print(intell.the_cleverest())

# WRITING INTO FILE
# with open('all_super_heroes.txt', 'a', encoding='utf-8') as file:
#     for item in request.get_info():
#         file.write(str(item) + '\n')

###############################################################################

# target_dict = {}

# for item in request:
#     if item['name'] in intell.superheroes_list:
#         target_dict[item['name']] = item['powerstats']['intelligence']

# for key, value in target_dict.items():
#     if value == max(list(target_dict.values())):
#         result = key

# print(result)
# print(target_dict)

