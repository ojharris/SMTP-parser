#python 2

def collectFile():##the first function
	global content
	fileName = raw_input("File name: ") ##must include the .txt 
	
	with open(fileName) as f: ##opens as READ ONLY. 
		content = f.readlines() #stores the lines in a variable -- global
	




def splitHeaders():
	##the content of the file is already global so it's already here.
	global headers
	headers = []  #The list holds the information we split up so it can be formatted into a html page
	#    Header name : content of the header
	tempHold = ""
	for line in content:
		part = line[0:3]#first 3 characters
		if(len(part) != len(part.strip())): #if this is true, it means this is part of the same header
			tempHold = tempHold + "\n" + line.strip()
		else:
			##new header!
			headers.append(tempHold)
			tempHold = line.strip()



def createPage():
	##headers is already global
	output = "sorted.html"
	with open(output,"ab") as f:#open the file or create it - appending to the end
		#Generate the new page
		f.write("<html><title>Smtp table</title><body><table><tr><td style='border: dotted 1px orange'>Header</td><td style='border: dotted 1px orange'>Content</td></tr>\n")
		##loop in each of the list items
	
		for item in headers:
			
			try:
				header,content = item.split(":",1)
			except:
				print "ignoring value"
				continue
			##change < > & so that they show on html
			content = content.replace("&","&#x26;")
			content = content.replace("<","&#x3c;")
			content = content.replace(">","&#x3e;")
			
			f.write("<tr><td style='border: solid 1px black'>"+header+"<td style='border: solid 1px grey'><p>"+content+"</p></td></tr>\n")
		f.write("</table></body></html>")



##Now all the functions have been defined the actual program can run. 
##Try loops means the program can keep running even after a user error (entering the wrong file name)
while True:
	try:
		collectFile()
		break
	except:
		print "Incorrect filename!"
		collectFile()
	
##So you correctly entered the file name and its read it - Great, lets split it all up
#No try loop as if there is an error here there is no pointing carrying on
splitHeaders()

print "*******"



createPage()
print "Finished"

