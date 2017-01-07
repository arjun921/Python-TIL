import subprocess
for x in range(10):
	incomm = input('$')
	for word in incomm.split():
		subprocess.run([word])

