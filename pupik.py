fruits = ["jablko", "Hruška", "Banán", "Mrkev", "Jahoda"]
print(len(fruits))
for i in fruits:
    print(i)
fruits.append("Kámen")
fruits.pop(5)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)