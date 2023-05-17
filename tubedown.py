import pytube
import os


def youtubedownload(id):
  yt = pytube.YouTube("https://youtube.com/watch?v=" + str(id))
  video = yt.streams.filter(only_audio=True).first()

  out_file = video.download('static/temp')
  new_file = id + '.mp3'
  os.rename(out_file, 'static/temp/' + new_file)


def tubedata(id):
  vidurl = "https://youtube.com/watch?v=" + str(id)
  yt = pytube.YouTube(vidurl)
  
  title = yt.title
  thumb = yt.thumbnail_url
  title = str(title).split(" ")
  if len(title) > 7:
    title = title[:7]
  title = " ".join(title)
  chrurl = yt.channel_url
  data = {"thumb": thumb, "title": title, "chrurl": chrurl, "vidurl": vidurl}
  return data
