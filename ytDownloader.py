import pytube
link = input('Enter youtube video URL')
yt = pytube.YouTube(link)
yt.streams.first().download()
print('downloaded', link)