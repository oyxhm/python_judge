def judge(year):
	if int(year) % 4 == 0  and int(year) % 100 != 0 :
		print "yes"
	elif int(year) %400 == 0:
		print "yes"
	else :
		print "no"
def error(year):
	flag =(year.isalpha()) or (not (year.isalpha() or year.isdigit()) and year.isalnum()) 
	if flag == True :
		print "bieluanshu!!!"
	else :
		judge(year)
	
	
year = raw_input("shuruyigeshu:")
error(year)

