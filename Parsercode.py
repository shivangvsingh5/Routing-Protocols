#open csv file
asda = open("Project2Results.csv")

#Initializ sum variable
sum=0
for line in asda:


	words=line.split(",")

	if words[2].isalpha():
		continue
	sum = sum+int(words[2])

#print total no of packets
print sum
