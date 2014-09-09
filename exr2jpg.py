import os, sys
#from subprocess import Popen
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call

executable  = "ffmpeg.exe" # -y -i C:/test.exr C:/outs.tiff"
#rawFile = "VFX_Plates_Cam_9624_CineF5.1000.exr"

filename = "VFX_Plates_Cam_9624_CineF42."
InputEnding = "exr"
OutputEnding = "tiff"
commandPool = []
Errorlog = list()
PATH = "V:\\040_Footage\\001_Elements_out\\2K_EXR"
originalWidth = 2048.0
originalHeight = 1152.0
ratio = originalHeight / originalWidth
targetWidth = 200
targetHeight = int(targetWidth * ratio)
print "targetheight: " + str(targetHeight)
def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    print parts
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)


def goBackFolders(path, depth):
	print "original Path: " + path
	numberOfOccurences = path.count("\\")
	relativeGoBack = numberOfOccurences - depth
	position = findnth(path, "\\", relativeGoBack-1)
	newPath = path[0:position]
	print "newPath " + newPath
	return  newPath

def walklevel(some_dir, level=2):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

for path, dirs, files in walklevel(PATH):
	#print path
	if not path.endswith("tiff") and not path.endswith("jpg"):
		if not os.path.exists(path + "\\jpg"):
			os.makedirs(path + "\\jpg")
	if path.endswith("tiff"):
		for filename in files:
			if filename.endswith('.tiff'):
				fullpath = os.path.join(path, filename)
				#newFilePath = path[:-5] + "\\jpg\\" +  filename[:-5] + ".jpg"
				newFilePath = goBackFolders(path, 2) + "\\thumbnails\\" + filename[:-5] + ".jpg"
				scaling = " -vf \"scale="+ str(targetWidth) +  ":" + str(targetHeight) +"\"" 
				command = executable + " -i " + "\"" + fullpath + "\"" + " " + scaling + " " + "\""+newFilePath + "\"" + " -y -loglevel panic"
				commandPool.append(command)
				print command
				break

# pool = Pool(26)
# for i, returncode in enumerate(pool.imap(partial(call, shell=True), commandPool)):
# 	if returncode != 0:
# 		print("%d command failed: %d" % (i, returncode))
# 		Errorlog.append(commandPool[i])

# print Errorlog
# logFile = open('V:\\040_Footage\\logfile.txt', 'w')
# for item in Errorlog:
#   logFile.write("%s\n" % item)