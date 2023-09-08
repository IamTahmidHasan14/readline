f = open("file2.txt", "r")
j = 0
sub = ["Math", "English", "Bngla", "History"]
while True:
  j += 1
  line = f.readline()
  if not line:
    break
  print(f"Marks of Student {j}:")
  m = line.split(",")
  for i in range(4):
    print(f"{sub[i]} = {m[i]}")
  # print(m)
  # print(line)
f.close()