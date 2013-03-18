class Scanner:

	def __init__(self, sketch_path, ext, display_time):
		self.path = sketch_path #Path to the sketch directory
		self.display_time = display_time * 60 # time in minutes multiplied by 60 seconds
		self.file_list = self.buildFileList() # builds a list of sketches to loop through

	def buildFileList(self):
		os.chdir(sketch_path) #Change the current directory to the directory the sketches are stored in
		files = os.listdir(os.curdir) #get a list of the files
		files = [file for file in files if file.endswith(ext)] # filter out files that do not have the right file extension
		print files #Print the files in the folder that will be cycled through
		return files

	def play(self):

		for file in self.file_list:
			filePath = file # combine path to the file and file names
			filePath = filePath.replace(' ', '\ ') # escape the spaces in the file path and file name strings

			cmd = 'open -a ' + filePath # bash command to open file
			print cmd # output test string
			os.system(cmd) #execute open command in the console
			time.sleep(self.display_time) #Scanner waits a specified amount of time to display the sketch
			os.system('killall JavaApplicationStub') #kills the currently running processing sketch

	def scan(self):

		files = os.listdir(self.path) #gather a list of files in the sketch folder

		for file in files:
			if file not in self.file_list and file.endswith(ext): #if a file matches the ext pattern specified and is not already listed in the display's file_list
				self.file_list.append(file) #add to the display's file_list

if __name__ == '__main__':
	import os, sys, time

	sketch_path = '../Storrs_Display' #relative path to the sketch folder
	display_time = 30 #Time that a sketch is displayed in minutes
	ext = '.app' #File extensions to look for while searching the folder containing the sketches

	dirScanner = Scanner(sketch_path, ext, display_time)

	while True:
		dirScanner.play()
		dirScanner.scan()
