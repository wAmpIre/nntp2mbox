#!/usr/bin/python

import nntplib
import sys
import email

outfile = file(sys.argv[-1], 'a')

nntpconn = nntplib.NNTP('news.gmane.org')

resp, count, first, last, name = nntpconn.group(sys.argv[-1])
print 'Group', name, 'has', count, 'articles, range', first, 'to', last

last = int(last)
startnr = last - 500

if startnr < 1:
	startnr = 1

try:
	nofile = file(sys.argv[-1] + ".cfg", 'r')
	startnr = int(nofile.readline())
	nofile.close()
except IOError:
	print 'No number file found, starting at ' + str(startnr)

if startnr < 1:
	startnr = 1
if startnr < last:
	last = last +1





for msgno in range( startnr, last ):
	try:
		resp, number, id, list = nntpconn.article(str(msgno))

		text = str()
		for line in list:
			text += line + "\n"

		msg = email.message_from_string(text)
		outfile.write(str(msg))
		outfile.write('\n')

		print '%s(%s): %s' % (number, msgno, id)
	except:
		pass

outfile.close()


nofile = file(sys.argv[-1] + ".cfg", 'w')
nofile.write(str(last))
nofile.close()


