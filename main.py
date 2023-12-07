etelnev=["húsleves","paradicsomleves","gyümölcsleves"]
etelar=[1200,1100,2000]

"""
Most annyi lista van, ahány tulajdonsága az adott ételnek.
Úgy lenne a jobb ha csak egy listánk lenne és egy ételnek egyben kezelhetnénk a tulajdonságait.
Létrehozunk egy étel típust - ez az étel általános leírását fogja jelenteni.
A konkrét étel a típus példányosításakor jön létre. 
"""

from Etel import Etel

etelek=[]
etel=Etel("húsleves",1200, "leves") #példányosítás
etelek.append(etel)
etel=Etel("paradicsomleves",1100,"leves")
etelek.append(etel)
etel=Etel("gyümölcsleves",2000,"leves")
etelek.append(etel)

for i in range(0, len(etelek),1):
    print(f"Az {i}.etel: {etelek[i].nev},{etelek[i].ar},{etelek[i].tipus}")


from Szemely import Szemely

szemelyek=[]
szemely=Szemely("Nagy Anna",2000,123123123, "nő")
szemelyek.append(szemely)
szemely=Szemely("Kis Tamás",2002,123123127, "férfi")
szemelyek.append(szemely)
szemely=Szemely("Horváth Előd",2006,123123126, "férfi")
szemelyek.append(szemely)

for i in range(0, len(szemelyek),1):
    print(f"Az {i}.szemely: {szemelyek[i].nev}, {szemelyek[i].szul}, {szemelyek[i].szemsz}, {szemelyek[i].nem}")
    print(f"{szemelyek[i].nev} {szemelyek[i].kor()} éves.")




