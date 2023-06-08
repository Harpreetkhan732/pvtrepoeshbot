import os

boobs = []

for pussy in os.listdir("prime/assets"):
    if pussy.endswith("png"):
        boobs.append(pussy[:-4])

