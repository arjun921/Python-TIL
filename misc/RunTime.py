start_time = time.time()
"""Enter Code here"""
print("--- %s seconds ---" % (time.time() - start_time))
files = open('time.txt','r')
old = files.readline()
new = time.time() - start_time
old = float(old)
diff = new - old
print (diff)
files.close()


files = open('time.txt','w')
files.write(str(new))
files.close()
