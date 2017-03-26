import feedparser
import json
import re


lol = feedparser.parse('https://www.reddit.com/r/leagueoflegends/.rss')

arts = len(lol.entries)
#print len(lol.entries)


#Print titles of Front page posts
print('\n')
for i in range(arts):
	print lol.entries[i].title


#Get # of entries, go through entries one by one to match author to moobeat, return title for now
for i in range(arts):

	if lol.entries[i].author == '/u/moobeat': #Find Posts by moobeat
		print '\n' '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
		print "Moobeat posts:" + '\n'
		print 'Title: ' + lol.entries[i].title
		print 'Date: ' + lol.entries[i].date
		print 'Link: ' + str(lol.entries[i].links[0].href)
		print i
		print '\n' '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
	if "lcs" in lol.entries[i].title.lower(): #Find Posts with LCS in title
		print '\n' '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
		print "LCS articles:" + '\n'
		print 'Title: ' + lol.entries[i].title
		print 'Date: ' + lol.entries[i].date
		print 'Link: ' + str(lol.entries[i].links[0].href)
		print i
		print '\n' '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
	if "dyrus" in lol.entries[i].content[0].value.lower(): #Find Posts with Dyrus in Content section
		print '\n' '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
		print "Dyrus mentions:" + '\n'
		print 'Title: ' + lol.entries[i].title
		print 'Date: ' + lol.entries[i].date
		print 'Link: ' + str(lol.entries[i].links[0].href)
		print i
		print '\n' '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
	if "faker" in lol.entries[i].title.lower(): #Find Posts with 24 in title
		print '\n' '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
		print "Faker articles:" + '\n'
		print 'Title: ' + lol.entries[i].title
		print 'Date: ' + lol.entries[i].date
		print 'Link: ' + str(lol.entries[i].links[0].href)
		print i
		print '\n' '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'
	print




'''
for key in league.keys():
	if str(key) == "entries":
		print 'IT HAS BEEN FOUND'
		test = feedparser.parse(key)
		print test
'''


'''
for key in lol.keys():
	print 'Current Key is ' + str(key)
	print 'Current Value is ' + str(lol[key])
	print '\n'
'''



'''
for entry in league['entries']:
	print "[+] NEW POST TITLE - " + str(entry['title'])
	print "\n"
'''
'''
for entry in league['entries']:
	print str(entry)
	print '\n'
'''
