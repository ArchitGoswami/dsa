dictNew = {}
dictNew.update({"1": "SCE"})
dictNew.update({"2": "NYC"})
dictNew.update({"3": "DXB"})
dictNew.update({"4": "DEL"})
dictNew.update({"5": "BAL"})
dictNew.update({"6": "SYD"})
print(dictNew)

dictNew.pop("4")
print(dictNew)

print(len(dictNew))