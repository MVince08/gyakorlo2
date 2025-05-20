import datetime

VT = "" # vagyottárgy
VT = input("Mire gyűjt Anna?")
HK = "" # hánykutya
HK = int(input("Hány kuytát sétáltatt Anna?"))

print((HK*20)/60 ,"órát sétáltatt")
print(HK * 700, "Ennyi FT-ot kapott.")
if HK * 700 <= 5000:
    print(f"Anna {HK} sétáltatott {(HK*20)/60} óra alatt, ezért {HK*700} forintot kapott. Ez nem elég a {VT}-hez")
else:
    print(f"Anna {HK} sétáltatott {(HK*20)/60} óra alatt, ezért {HK*700} forintot kapott. Ez elég a {VT}-hez")
