import os;

def rename_files():
	file_list = os.listdir(r"/Users/lucblaas/Desktop/python-course/prank")
	print(file_list)
	saved_path = os.getcwd()
	print("Currently working directory " + saved_path)

	os.chdir("/Users/lucblaas/Desktop/python-course/prank")
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
rename_files()	