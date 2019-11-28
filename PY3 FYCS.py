
import time
import sys
lines = "WELCOME TO ANONYMOUS HACKERS\n WE ARE FECHING ALL DATA "
chno=-1
for line in lines:
	for c in line:
		time.sleep(0.1)
		for i in range(len(lines)):    
			chno +=1     
			print(lines[chno],end="")
			sys.stdout.flush()
			break
list_of_names=['Vivek','Roshan','Govind','Nikhil']
name=input("\nEnter Your Name:-")
if name in list_of_names:
	print('Your Data Has Been Found')
else:
	print('Error While Receving Data')
			