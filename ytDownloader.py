import pytube
link = input('Enter youtube video URL')
yt = pytube.YouTube(link)
yt.streams.first().download() #File will get downloaded in that folder where you have saved this program
print('downloaded', link) 
