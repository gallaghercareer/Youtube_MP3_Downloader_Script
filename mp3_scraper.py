import yt_dlp
import scrapetube
from tqdm import tqdm

#Define a function to read in a single line file
def read_api_key(input_file):
    # Open the file in read mode
    with open(input_file, 'r') as file:
        # Read the contents of the file as a string
        string_variable = file.read()
        return string_variable

videos = scrapetube.get_channel("UCv83tO5cePwHMt1952IVVHw")
counter = 0
audioUrl_list =[]

# Set options for downloading the audio file
options = {
    'format': 'bestaudio/best',
    'outtmpl': '/Users/yanni/Documents/GitHub/Youtube_MP3_Downloader_Script/Pinecone_videos/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
 # Create a yt-dlp object and pass in the options
ydl = yt_dlp.YoutubeDL(options)

for video in videos:
    #create list of video ids    
    audioUrl_list.append('https://www.youtube.com/watch?v=' + video['videoId']) 
    
#loop through each link in the file
for audio in audioUrl_list:
    
    try:
       

        # Download the audio file
        ydl.download([audio])
        
        pritn("downloaded " + str(audio))
    except:
        print(r"{line} missing, moving to next url")
        pass
    counter = counter + 1
    print(counter)

