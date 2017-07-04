import os
# main directory listing name of dogs
#species/imageName --> test/species/imageName
a = os.listdir()
testPath = 'test/'
trainPath = 'train/'
for species in a:
	if species not in ['.DS_Store', 'Folder Rename.Py', 'Split.Py','split.py','test', 'train']:
		# species = Dog species name
		# listing images in directory
		images = os.listdir(species)
		twenty = int(round(len(images)*0.2))
		eighty = len(images) - twenty
		species = species+'/'
		#if 'test' does not exist, create
		if not os.path.exists(testPath):
			os.makedirs(testPath)
		#if 'test/species' does not exist, create
		if not os.path.exists(testPath+species):
			os.makedirs(testPath+species)
		#if 'train' does not exist, create
		if not os.path.exists(trainPath):
			os.makedirs(trainPath)
		#if 'train/species' does not exist, create
		if not os.path.exists(trainPath+species):
			os.makedirs(trainPath+species)
		################ move to test
		print(species,twenty)
		for i in range(twenty):
			if images[i] not in ['test','train']:
				initpath = species+images[i]
				finalPath = testPath+species+images[i]
				print ('Test! Initial:{} --> Final:{}'.format(initpath,finalPath))
				os.rename(initpath,finalPath)
			# print(images[i])
############# move to train
		images = os.listdir(species)
		for i in range(len(images)):
			if images[i] not in ['test','train']:
				initpath = species+images[i]
				finalPath = trainPath+species+images[i]
				print ('Train! Initial:{} --> Final:{}'.format(initpath,finalPath))
				os.rename(initpath,finalPath)
		os.rmdir(species)
			# images = os.listdir(species)
			# for rest in images:
			# 	initpath = species+'/'+rest
			# 	finalPath = species+'/train/'+rest
			# 	os.rename(initpath,finalPath)