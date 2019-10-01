#################################################################################
#   caesar.py - Caesar Shift Cipher + ROT13 Algorithm                           #
#                                                                               #
#   Author: Spartan Bunny (spartanbunny@pm.me)                                  #
#                                                                               #
#   Contains:                                                                   #
#           - Caesar Object                                                     #
#               - Shiftencrypt(), ShiftDecrypt()                                #
#           - ROT13 Object                                                      #
#               - update(str), encrypt(), decrypt(), reset()                    #
#                                                                               #
#   Usage: Import the file to your python program.                              #
#           - caesar.[Cryptograpy-Object] to initialise a Crypto-Object.        #
#           - use update(str) to insert string, encrypt() to encrypt,           #
#             decrypt() to decrypt, reset() to reset the data                   #
#                                                                               #
#                                                                               #
#   Copyright (c) 2019 Spartan Bunny                                            #
#################################################################################

class Caesar:
    def __init__(self):
        pass
    def Shiftencrypt(self,string, shift):
        finalString = ""
        for element in string:
            if ord(element) >= ord('A') and ord(element) <= ord('Z'):
                finalString += chr(ord('A') + ((shift + ord(element) - ord('A')) % 26))
            elif ord(element) >= ord('a') and ord(element) <= ord('z'):
                finalString += chr(ord('a') + ((shift + ord(element) - ord('a')) % 26))
            else:
                finalString += element
        return finalString
    def Shiftdecrypt(self,string, shift):
        finalString = ""
        for element in string:
            if ord(element) >= ord('A') and ord(element) <= ord('Z'):
                finalString += chr(ord('A') + ((-shift + ord(element) - ord('A')) % 26))
            elif ord(element) >= ord('a') and ord(element) <= ord('z'):
                finalString += chr(ord('a') + ((-shift + ord(element) - ord('a')) % 26))
            else:
                finalString += element
        return finalString

class ROT13:
    def __init__(self, string = None):
        self._CaesarVar = Caesar()
        self._data = None
        if not string is None:
            self._data = string
    
    def update(self, string):
        if not string is None:
            if self._data is None:
                self._data = string
            else:
                self._data += string
        else:
            try:
                self._data += str(string)
            except:
                print("Error occured in string input.")
    
    def reset(self):
        self._data = None
    
    def __repr__(self):
        return self._CaesarVar.Shiftencrypt(self._data, 13)

    def encrypt(self):
        return self._CaesarVar.Shiftencrypt(self._data, 13)
    
    def decrypt(self):
        return self._CaesarVar.Shiftdecrypt(self._data, 13)