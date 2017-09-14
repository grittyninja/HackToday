from collections import defaultdict
import random
random.seed(42)

trick_str = "HackToday{xxtHi$_1s_N0t_The_real_Flagxx}"
target_str = "HackToday{str1Ng$_tr1cks_Hack}"

pos_map = defaultdict(list)

for i,c in enumerate(trick_str):
	pos_map[c].append(i)
	
res = []
for c in target_str:
	if c not in pos_map:
		print "Can't find mapping for ", c
		exit(0)
	res.append(str(random.choice(pos_map[c])))
print 'const char *trick_str = "{0}";'.format(trick_str)  
print "int permute[] = {" + ", ".join(res) + ", -1};"
