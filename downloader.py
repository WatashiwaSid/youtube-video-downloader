# importing modules

from tkinter import *
from pytube import YouTube

# initializing tkinter window

main = Tk()
main.geometry("500x450")
main.title("Youtube Video Downloader")
main.iconbitmap('icon.ico') #move all files in same directory

# defining the function to download YouTube videos.
# Use Try and Excpet 
def download():
    try:
        myvar.set("Downloading, please wait ...")
        main.update()
        YouTube(link.get()).streams.first().download()
        link.set("Download Completed Successfully!")

    except Exception as e:
        myvar.set("Something Went Wrong")
        main.update()
        link.set("Please Enter A Valid URL")    
        


Label(main, text="Download YouTube Videos\nThe Easy Way\n", font="Consolas 15 bold").pack()

Label(main, text="Make Sure You Are Connected To Internet", font="Consolas 8 bold").pack()

myvar = StringVar()
Entry(main, textvariable = myvar, width = 40).pack(pady=10)
myvar.set("Paste Your Link Below")

link = StringVar()
Entry(main, textvariable = link, width = 40).pack(pady=10)
link.set("Paste Your YouTube Video URL Here")

Button(main, text="Download", command=download).pack(pady=15)

#running the mainloop
main.mainloop() 

#Make Sure You're Connected To Internet