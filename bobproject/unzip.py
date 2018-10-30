import os
import time
def vir2apk2unpack(dirname, dst):
	count = 0
	filenames = os.listdir(dirname)
	for filename in filenames:
		count += 1
		print(count)
		full_filename = os.path.join(dirname,filename)
		command = "unzip "+ full_filename + " -d "+ dst+"/"+filename.split(".")[0]
		# print(command)
		os.system(command)
def main():
	start = time.time()
	vir2apk2unpack("C:\\Users\\SonMinWoo\\Desktop\\KU-Android-pre-train\\0-normal", "C:\\Users\\SonMinWoo\\Desktop\\KU-Android-pre-train\\normalunpack") # must have unpack_submit folder
	end = time.time()
	print("=============\nunpack time: {}\n=============\n").format(start-end)

main()
