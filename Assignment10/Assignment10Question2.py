a = open("Yah!!!.txt", "wt")
a.write("Feel like Godzilla, better hit the deck like the card dealer!")
a.close()
b = open("Yah!!!.txt", "rt")
c = b.read()
print(c)
