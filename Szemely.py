import datetime

class Szemely:
    def __init__(self, nev:str, szul:int, szemsz:int, nem:str):
        self.nev=nev
        self.szul=szul
        self.szemsz=szemsz
        self.nem=nem
    
    def kor(self): 
        """kotelezo parameter a self!!!"""
        #tagfüggvény vagy osztály metódus.
        #az osztály adattagjain végeznek műveleteket.
        x= datetime.datetime.now()
        return x.year - self.szul