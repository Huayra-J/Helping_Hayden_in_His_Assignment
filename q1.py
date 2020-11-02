#get file object reference to the file
file = open("HIT137cdu.txt","r")
#read content of file to string
data = file.read()
#get number of occurrences of the substring in the string
count = data.count("You Make CDU")
count2 = data.count("Great. You Make CDU")
print('Number of You make CDU are:', count)
print('Number of Great. You make CDU are:', count2)