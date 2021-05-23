from tkinter import *
from pytube import YouTube

window = Tk()
window.title("Youtube Video downloader")

def download():
    try:
        myVar.set("Downloading..")
        window.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video Downloaded Successfully")
    except Exception as e:
        myVar.set("Mistake")
        window.update()
        link.set("Enter correct link")


website_label = Label(text="Welcome to Youtube Downloader Application")
website_label.pack()

myVar = StringVar()

myVar.set("Enter the link below")

webEntry = Entry(textvariable=myVar, width=40)
webEntry.pack(pady=10)

link = StringVar()

uentry = Entry(textvariable=link, width=40)
uentry.pack(pady=10)

button = Button(text="Download video", command=download)
button.pack()


window.mainloop()