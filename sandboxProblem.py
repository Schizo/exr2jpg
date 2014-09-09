import os, sys
#from subprocess import Popen
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call
from subprocess import Popen

commandPool = ['C:\\dcraw.exe -T \"V:\\010_User\\Julian\\Octo\\Blackmagic Pocket Cinema Camera_1_2014-07-02_1032_C0000\\Blackmagic Pocket Cinema Camera_1_2014-07-02_1032_C0000_008486.dng\"',
'C:\\dcraw.exe -T \"V:\\010_User\\Julian\\Octo\\Blackmagic Pocket Cinema Camera_1_2014-07-02_1032_C0000\\Blackmagic Pocket Cinema Camera_1_2014-07-02_1032_C0000_008489.dng\"']

#print commandPool[0]
#sa_proc = Popen("dcraw.exe")


pool = Pool(26)
for i, returncode in enumerate(pool.imap(partial(call, shell=True), commandPool)):
	if returncode != 0:
		print("%d command failed: %d" % (i, returncode))
		#Errorlog.append(commandPool[i])