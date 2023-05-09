from pytube import YouTube 
  
 
SAVE_PATH = "/content/talkinghead/Wav2Lip-GFPGAN/Wav2Lip/data_root/main/"  
 
f = open("/content/talkinghead/Wav2Lip-GFPGAN/Wav2Lip/resources/yt_file_list.txt", "r")
for file_link in f:
   link="https://www.youtube.com/watch?v="+str(file_link)
   
  
   try: 
     
      yt = YouTube(link) 
   except: 
      print("Connection Error")  
  
 
   mp4files = yt.filter('mp4') 
  
 
   yt.set_filename("file"+str(file_link))  
  
 
   d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
   try: 
     d_video.download(SAVE_PATH) 
   except: 
     print("Problem Occured")