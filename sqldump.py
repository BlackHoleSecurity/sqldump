#!/usr/bin/python
"""
sqldump 1.5
Date: Fri May 11 11:08:40 2018
Author: DedSecTL
Team: BlackHole Security
Github: https://github.com/Gameye98
"""
import sys
import time
from googlesearch import search

__banner__ = "sqldump 1.5 by DedSecTL/DTL - BlackHole Security"
__bannerSQL__ = """sqldump 1.5 by DedSecTL/DTL - BlackHole Security
created @date Fri May 11 11:08:40 2018
Usage: sqldump.py [OPTIONS]

Dump sql result sites with easy

OPTIONS:
	-g DORK         process sql dork result with google
	-a KEYWORD      automatic process sql dork with google
	-r SHOW,CLEAR   show dork result, clear dork result
"""

def sqldump(opt, arg):
	if opt == "-g":
		print __banner__
		print "[+] googledork result(s):"
		dump = open("result.txt", 'a')
		for result in search(str(sys.argv).replace(sys.argv[0], '').replace(sys.argv[1], '').replace('[', '').replace(']', '').replace('\'', '').replace(',', ''), tld="com", num=90, stop=100):
			if "php?id=" in result:
				print "\033[92m"+result+"\033[0m"
				dump.write(result+"\n")
			else:
				print "\033[1;93;101m"+result+"\033[0m"
			time.sleep(1)
		dump.close()
	elif opt == "-a":
		print __banner__
		print "[+] automatic googledork result(s):"
		dump = open("result.txt", 'a')
		for result in search("inurl:"+arg+".php?id=", tld="com", num=90, stop=100):
			if "php?id=" in result:
				print "\033[92m"+result+"\033[0m"
				dump.write(result+"\n")
			else:
				print "\033[1;93;101m"+result+"\033[0m"
			time.sleep(1)
		dump.close()
	elif opt == "-r":
		if arg == "CLEAR":
			result = open("result.txt", 'w')
			result.close()
		else:
			result = open("result.txt", 'r').read()
			print result
	else:
		print __bannerSQL__

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print __bannerSQL__
	else:
		try:
			sqldump(sys.argv[1], sys.argv[2])
		except KeyboardInterrupt:
			print
			sys.exit()
		except:
			print "No address associated with hostname"
			sys.exit()