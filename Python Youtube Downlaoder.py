from tkinter import *
from pytube import YouTube

root = Tk()
root.geometery('500x300')
root.resize(0,0)
root.title('My YouTube Downloader')

Label(root, text= 'YouTube Video Downloader', font = 'aerial 20 bold').pack()

link = StringVar()
Label(root, text = 'Paste Your Link Hare', font = 'aerial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width =70, textvariables= link).place(x=32, y=90)

def Downlaod():
    url = YouTube(str(link.get()))
    video = url.stream.first()
    video.downlaod()
    Label(root, text = 'DOWNLOADED', font= 'aerial 15').place(x=150, y = 210)

Button(root, text= 'Download', font= 'aerial 15 bold', bg = 'pale violet red', padx = 2, command = Downloader).place(x=150, y =180)
root.mainloo()