import pytube

def tubedata(id):
    yt = pytube.YouTube("https://youtube.com/watch?v="+str(id))
    title = yt.title
    thumb = yt.thumbnail_url
    yt.channel_url
    title = str(title).split(" ")
    if len(title) > 7:
        title = title[:7]
    title = " ".join(title)
    data = {"thumb":thumb,"title":title}
    return data
yt = pytube.YouTube("https://youtube.com/watch?v="+"VISdz__kXt8")
h = yt.channel_url
print(h)
