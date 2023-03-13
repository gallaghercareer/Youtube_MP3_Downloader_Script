import os
import subprocess
import shutil


def transcribe_mp3(directory):
    #current working directory
    cwd = os.getcwd()
    print("outer reached")
	# Iterate through all files and directories in the input directory
    for file in os.listdir("."):   
        print("checking filename of files in directory tree")sudo apt update && sudo apt install ffmpeg

        if file.endswith('.mp3'):
            # Construct the full path to the MP3 file
            mp3 = directory + file
            print(mp3)             
            # Construct the full command to be executed
            full_command = "whisper {mp3} --model medium"          
            # Call the command using subprocess.run()
            print('transcribing video.....')
            subprocess.run(full_command, shell=True)

    for files in os.listdir("."):
        print("creating new directory if output directory doens't exist")
        # Define the path to the new directory
        new_directory = os.path.join(directory, "transcribed_text")

        # Create the new directory if it doesn't already exist

        os.makedirs(new_directory, exist_ok=True)
        
        for filename in files:
              #if filename ends in a .txt move file to new_directory
            if filename.endswith('.txt'):            
                # Move the file to the new directory
                shutil.move(filename, new_directory)
            
    '''input_final = ''
    while True:
        user_input = input("Are you in the directory with the audio files? Enter 'Y' or 'N': ")
        if user_input.lower() == "Y":
            print("You entered 'yes'.")
            input_final=cwd
            transcribe_mp3(input_final)
            break
        elif user_input.lower() == "N":
            print("You entered 'no'.")
            user_input_2 = input("Name the directory with mp3 files: ")
            input_final =user_input_2
            transcribe_mp3(input_final)
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        '''

transcribe_mp3(input("directory of mp3s:"))