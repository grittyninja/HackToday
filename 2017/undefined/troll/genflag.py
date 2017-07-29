import random
random.seed(1945)

with open("troll.txt") as f:
	text = f.read()

flag = "HackToday{HTML_Troll}"

res = ""
for c in flag:
	a = ("0000000" + bin(ord(c))[2:])[-7:]
	res += a

print res

tmp = list(text)
res = res.replace("1", "O")

idx = 0
for i,c in enumerate(tmp):
	if (c=="Q"):
		if random.randint(0,3)==2:
			tmp[i] =res[idx]
			idx +=1
			if idx==len(res):
				break

assert(idx==len(res))

with open("tf.txt", "w") as f:
	f.write("".join(tmp))

