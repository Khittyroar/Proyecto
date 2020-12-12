from itertools import zip_longest

dict1 = {0: [1, 0, 2, 1, 2, 0, 2, 0, 3]}
dict2 = {0: [0, 0, 1, 0, 1, 0, 2, 0], 1: [0, 0, 1, 0, 0, 0, 0, 0]}

dict_res = {
    key: [v1 + v2 for v1, v2 in zip_longest(
              dict1.get(key, ()), dict2.get(key, ()), fillvalue=0
              )] for key in dict1.keys() | dict2.keys()}

print(dict_res)

#unir diccionarios por clave
https://es.stackoverflow.com/questions/344426/sumar-los-valores-de-2-diccionarios