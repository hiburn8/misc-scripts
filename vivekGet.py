#!/usr/bin/python

import urllib2, re, os, thread, time

courseNo = raw_input("courseID: ")
cookie = raw_input("ACSID cookie value: ")

opener = urllib2.build_opener()
opener.addheaders.append(("Cookie","ACSID=" + cookie))
f = opener.open("http://www.pentesteracademy.com/course?id=" + courseNo)

content=f.read()
matches = re.findall('video?id=...', content)
print str(len(matches)) + " modules found"

def get_courseware( matches, tname, delay):
	time.sleep(delay)
	c=1
	for s in matches:
		vurl = ('http://www.pentesteracademy.com/accounting?id=' + s[-3:])
		purl = ('http://www.pentesteracademy.com/downloadpdf?id=' + s[-3:] + '&type=pdf')
		furl = ('http://www.pentesteracademy.com/downloadpdf?id=' + s[-3:] + '&type=file')

		page = opener.open("http://www.pentesteracademy.com/video?id=" + s[-3:])
		content=page.read()

		badtitle = re.findall(r'title-divider"><span>([A-Za-z0-9: ]+)', content)
		
		title = badtitle[0].replace(":", "-");
		title = title.replace("&", "and");
		title = str(c) + " - " + title;

		c +=1;
		if os.path.isdir(title) == False:
			os.mkdir(title)	

			v2 = re.findall('Video', content)
			if v2:
					print 'getting ' + title + '.mp4' 
					f = opener.open(vurl)
					with open(title + "/" + s[-3:] + ".mp4", "wb") as buf:
						buf.write(f.read())

			p2 = re.findall("PDF Slides", content)
			if p2:
					print 'getting ' + title + '.pdf' 
			   		f = opener.open(purl)
					with open(title + "/" + s[-3:] + ".pdf", "wb") as buf:
						buf.write(f.read())

			f2 = re.findall("Additional Files", content)
			if f2:
					print 'getting ' + title + '.zip' 
			  		f = opener.open(furl)
					with open(title + "/" + s[-3:] + ".zip", "wb") as buf:
						buf.write(f.read())
			print title + " folder is complete";
	print tname + " crossed the finish line"

thread.start_new_thread( get_courseware, (matches, "Papillon", 1, ) )
thread.start_new_thread( get_courseware, (matches, "Hedgehunter", 4, ) )
thread.start_new_thread( get_courseware, (matches, "Don't Push It", 7, ) )
thread.start_new_thread( get_courseware, (matches, "Monty's Pass", 10, ) )
while 1:
   pass