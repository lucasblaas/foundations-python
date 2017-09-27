import webbrowser
import time

total_breaks = 3
break_count = 0

print ("This program started on " + time.ctime())

while(break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("http://www.google.com")
	break_count = break_count + 1

# x = 1

# if x == 2:
# 	print "Blaas learning Python"
# else:
# 	print "Blaas not learning"