s = 'booboboopusbobomrbooboobobbpbobobbbob'
count = 0
while(len(s) > 0):
    index = s.find('bob')
    print index
    if(index >= 0):
        count = count + 1
        s = s[index+1:]
    else:
        print str(count)
        break
