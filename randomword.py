import random

abc = ["aeiou", "bcdfghjklmnpqrstvwxyz"]

model = random.choice(["kvvk","kvkvk","kvkvvk","vkv","kvvkplvkkvk", "kvkk", "kvk", "kvv", "kvkkvk", "vkvk"])

def generate(model, abc):
 final = ""
 for i in model:
  if i == "k":
     final += random.choice(abc[1])
  if i== "v":
    final += random.choice(abc[0])
  if i== " ":
    final += " "
 return final

print(generate(model, abc))