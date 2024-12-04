#!/usr/bin/env python
'''Divisió entera. Introduïm dos nombres i ens retorna la divisió, el residu i
el quocient
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Escriure un programa que demani a l'usuari dos nombres enters: dividend i
divisor. La sortida per pantalla ha de mostrar la divisió, el quocient i el
residu.
'''
__author__ = "Muhammad Ayaan Bilal"
__authors__ = ["One developer", "And another one", "etc"]
__email__ = "mbilal@instituticaria.cat"
__date__ = "2024/11/28"

dividend = int(input('Escriu un nombre enter: '))
divisor = int(input('Escriu un nombre enter: '))
print(f'Divisió: {dividend}/{divisor}')
print('Quocient:', dividend // divisor)
print('Residu:', dividend % divisor)
