for i in range(1,4):
	for j in range(1,4):
		for k in range(1,4):
			for l in range(1,4):
				y = str(3*(i-1)+j-1)
				x = str(3*(k-1)+l-1)
				print("\t\t<button class=\"button\" id=\""+y+","+x+"\" onclick=\"disp("+y+","+x+")\">&nbsp;</button>")
			print("<p class = \"horiz-space\">&nbsp;&nbsp;</p>")
		print("\t\t<br>")
	print("\t\t<br>")

for i in range(1,10):
	print("<button class=\"popup\" id=\""+str(i)+"\" onclick=\"process("+str(i)+")\">"+str(i)+"</button>")

