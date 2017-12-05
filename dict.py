"""
found = {}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0


found['e'] += 1
found['e'] += 1

for key, val in sorted(found.items()):
    print(key, 'was found', val, 'time(s)' )
"""
"""
vocal = ['a', 'e', 'o', 'i', 'u']

word = input("Enter word for a search: ")

found = {}


for letter in word:
    if letter in vocal:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was_found', v, 'time(s)!')
"""
people = {}

people['Andrey'] = {'Name' : 'Andrey', 'Last name' : 'Sindeev', 'position' : 'QA', 'Salary' : 30000}
people['Alex'] = {'Name' : 'Alexandr', 'Last name' : 'Ponomaryov', 'position' : 'lawyer', 'Salary' : 'unknown'}
people['Pavel'] = {'Name' : 'Pavel', 'Last name' : 'Dudkin', 'position' : 'seller', 'Salary' : 'unknown'}
people['Vanya'] = {'Name' : 'Ivan', 'Last name' : 'Aseev', 'position' : 'Network engineer', 'Salary' : 'unknown'}

for k, v in sorted(people.items()):
    print(k, v)
