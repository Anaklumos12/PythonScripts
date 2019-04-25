import re

f = open("datt0sink.txt","r+")
q = open("datt0source.txt","r+")
sinklines = q.readlines()
i = 0
lineIndex =0

for line in sinklines:
    print lineIndex, line
#    print line.find("CWMP") , " This is line.find"
    x = re.search("CWMP.*?\s",line)
    printStr = ""
    if (x != None):
        tempStr = ""

        print x.start(), x.end()
        i = x.start()
        while (i < x.end()):
            print i, line[i], " What?"
            tempStr = line[i]
            printStr = printStr + tempStr
            i += 1

        print tempStr

    i=0
    lineIndex+=1


    # while (i < len(line)):
    #     print
exit(1)