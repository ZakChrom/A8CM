from typing import List

stuff = []
ogstuff: List[List[str]] = []
for i in range(1, 5):
    with open(f"bitmap{i}", "r") as f:
        t = f.read()
        stuff.append(t.replace("\n", "").replace(" ", ""))
        ogstuff.append(t.split("\n"))


for i in range(4):
    ogstuff[i] = [x.replace("0", "  ").replace("1", "██") for x in ogstuff[i] if x]

for i in range(len(ogstuff[0])):
    print(f"{ogstuff[0][i]} {ogstuff[1][i]} {ogstuff[2][i]} {ogstuff[3][i]}")
    if i % 6 == 5:
        print("")

for i in range(4): print(f'const var bitmap{i} = "{stuff[i]}";')