# implement a command shell that provides all of the features
# that the course instructor described at the start of lab and are
# further described inside of the README.md file in this repository.
import os
import sys
import pathlib
import stat
#import all of the modules needed

def cd_command(path):
	""" Move folders """
	try:
		os.chdir(os.path.abspath(path))
	except OSError:
		print("The system cannot find the file specified, is not valid")
	# print(os.getcwd())

def pwd_command():
	""" Current directory """
	print(os.getcwd())
	# return current directory

def ls_command():
	""" List all folders """
	path = os.getcwd()
	for file in os.listdir(os.getcwd()):
		print(os.path.abspath(file))
	# path = os.getcwd()
	# for top, dirs, files in os.walk(os.path.abspath(path)):
	# 	for dir in dirs:
	# 		print(os.path.join(top, dir))
	# 		for file in files:
	# 			print(os.path.join(top, file))

	# return the files in current directory

# main function
def main():

	mode = os.fstat(0).st_mode
	print("pyprompt 0.1.0")
	if stat.S_ISFIFO(mode):
		print("stdin is piped")
	elif stat.S_ISREG(mode):
	# keep running until
		while True:
			#command-line input
			inputline = input("> ")
			print(inputline)
			# if the user choose exit
			if inputline == "exit":
				break
				# exit the terminal
			# if the user choose cd
			elif inputline[:3] == "cd ":
				cd_command(inputline[3:])
				# run this function
			# if the user choose cd ..
			# elif inputline == "cd ..":
				# run this function
			# if the user choose pwd
			elif inputline == "pwd":
				pwd_command()
				# run this function
			# if the user choose ls
			elif inputline == "ls":
				ls_command()
				# run this function
			# if it is not any of those...
			else:
				# execute command
				print("Command not found")
	else:
		while True:
			#command-line input
			inputline = input("> ")
			# if the user choose exit
			if inputline == "exit":
				sys.exit()
				# exit the terminal
			# if the user choose cd
			elif inputline[:3] == "cd ":
				cd_command(inputline[3:])
				# run this function
			# if the user choose cd ..
			# elif inputline == "cd ..":
				# run this function
			# if the user choose pwd
			elif inputline == "pwd":
				pwd_command()
				# run this function
			# if the user choose ls
			elif inputline == "ls":
				ls_command()
				# run this function
			# if it is not any of those...
			else:
				# execute command
				print("Command not found")



if '__main__' == __name__:
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(1)