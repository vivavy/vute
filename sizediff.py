with open("utf8.txt", "rb") as f:
    l1 = len(f.read())

with open("utf8.txt", "rb") as f:
    l2 = len(f.read())

diff = max((l1, l2)) - min((l1, l2))

if l1 == l2:
    s = "="
elif l1 < l2:
    s = "<"
else:
    s = ">"

print("Diff:", diff)
print("UTF-8", s, "VUTE")
