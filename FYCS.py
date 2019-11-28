
import time

lines = "WELCOME TO ANONYMOUS HACKERS\n WE ARE FECHING ALL DATA "
chno=-1
for line in lines:
	for c in line:
		time.sleep(1)
		for i in range(len(lines)):    
			chno +=1     
			print(lines[chno])
			break
			
