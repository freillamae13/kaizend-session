# Challenge - Lists Exercise

# Create a variable named shoes that is a
# list of the following items, in order:
# Spizikes
# Air Force 1
# Curry 2
# Melo 5

shoes = ["Spizikes", "Air Force 1", "Curry 2", "Melo 5"]

print(shoes)

shoes.insert(0, "Adidas")
print(shoes)

print(sorted(shoes))

del shoes[2]
print(shoes)

shoes[1] = "Onitsuka Tiger"
print(shoes)
print(len(shoes))