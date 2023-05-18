"""
Ejercicio de conteo de palabras: Escribe un programa que lea un archivo 
de texto y cuente la cantidad de veces que aparece cada palabra en el 
archivo. 
Luego, almacena los resultados en un diccionario y muestra los pares 
palabra-frecuencia en orden alfabético.
"""
import string


def read_text_file():
    path_file = "exercise-testing/txt_file.txt"
    with open('exercise-testing/txt_file.txt') as file:
        txt_line = file.readlines()
    return txt_line


def count_words_from_file(text_from_file: str) -> dict:
    frequency = {}
    read_file = read_text_file()
    for line in read_file:
        line = line.translate(str.maketrans('', '', string.punctuation))
        words = line.split()
        frequency = {word: frequency.get(word, 0) + 1 for word in words}
    
    return dict(sorted(frequency.items()))
