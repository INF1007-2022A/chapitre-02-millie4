#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    nouveaumot = ''
    for lettre in mot:
        if ord('a')<=ord(lettre)<=ord('z'): 
            nouveaumot+=(chr(ord(lettre) - 32))
    return nouveaumot

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
