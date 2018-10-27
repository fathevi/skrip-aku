import sys
import re
import subprocess
import os

def simpan_file(kalimat):
	tokens = [',', '.', '!', '?']

	for token in tokens:
			kalimat = kalimat.replace(token, " "+token+" ")

			kalimat = re.sub (r"\s+", " ", kalimat)
			kalimat = re.sub (r"\s$", "", kalimat)
			simpan_file = open ('IPOSTagger\kalimatinput.tag', 'w')
			simpan_file.write(kalimat)
			simpan_file.close()

def prediksi_pos():
	# print(os.getcwd())
	# subprocess.call('dir', shell=True)
	# os.chdir(os.getcwd()+"/IPOSTagger")
	# subprocess.call('java ipostagger kalimatinput.tag 1 1 0 1', shell=True)
	
	# subprocess.call('dir', shell=True)
	print("prediksi pos")

# def pisah_kata_pos():
# 	print("pisah kata pos")

# def prediksi_jeda():
# 	print("prediksi jeda")

# def pisah_pos_jeda():
# 	print("pisah pos jeda")

# def gabung_kata_jeda():
# 	print("gabung kata jeda")

if __name__=='__main__':
    if len(sys.argv)>1:
        menu = sys.argv[1]
        if(menu == 'simpan_file'):
        	kalimat = sys.argv[2]
        	simpan_file(kalimat)
        elif(menu == 'prediksi_pos'):
        	prediksi_pos()
	     	# elif(menu == 'pisah_kata_pos'):
	     		# pisah_kata_pos()
	     	# elif(menu == 'prediksi_jeda'):
	     		# prediksi_jeda()
	     	# elif(menu == 'pisah_pos_jeda'):
	     		# pisah_pos_jeda()
	     	# elif(menu == 'gabung_kata_jeda'):
	     		# gabung_kata_jeda()
	     		
