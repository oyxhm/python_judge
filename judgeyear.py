#coding=utf-8
def judge(year):
	try:
		year = int(year)
	except ValueError:
		print "please Enter numbers !"
		return
	if int(year) % 4 == 0  and int(year) % 100 != 0 :
		print "yes"
	elif int(year) %400 == 0:
		print "yes"
	else :
		print "no"

year = raw_input("Enter a year to judge:")
judge(year)

