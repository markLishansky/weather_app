# import requests

# url = "https://www.youtube.com/results"

# query = {'search_query': 'edward bil'}
# response = requests.get(url, params=query)

# print(response.status_code)
# print(response.url)


class Person:
    def __init__(self, name):
        self._name = name

    # @property
    def name(self):
        return self._name
    
class Employee(Person):
    def work(self):
        print(self.name, 'works')

tom = Employee('tom')
print(tom.name())