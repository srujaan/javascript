import os # to fetch the songs and directories
from tkinter.filedialog import askdirectory
import pygame # for playing music
from mutagen.id3 import ID3  #for tagging the songs
from tkinter import * #for GUI

##########################################################3

root = Tk() # creates an empty list
root.minsize(300,300) #set the size 300 X 300 window

###########################################################

## creating 2 lists

list_of_songs = []
real_names = []

###########################################################

v = StringVar()
song_label = Label(root, textvariable = v, width = 35)

###########################################################

#creating the function that opens up a directory a
#starts to scan

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)
    # loop over all the files in the directory
    for file in os.listdir(directory):
        #add the only files which end .mp3 format
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)
        # load the meta data of the song into an audio variabe i.e. a dictionary
            audio = ID3(realdir)
        #TIT2 refers to the TITLE of the song, So let’s append that to realnames
            real_names.append(audio['TIT2'].text[0])
            list_of_songs.append(file)
    
    # initialize pygame
    pygame.mixer.init()
    # load the first song
    pygame.mixer.music.load(list_of_songs[0])
    ##pygame.mixer.music.play()

def updatelabel():
    global index # If you do not use global, new index variable will be defined
    global songname
    v.set(realnames[index]) # set our StringVar to the real name 
    #return songname

def nextsong(event):
    # get index from globals
    global index 
    # increment index
    index += 1 
    # get the next song from listofsongs
    pygame.mixer.music.load(list_of_songs[index])
    # play it away
    pygame.mixer.music.play()
    # do not forget to update the label !
    updatelabel()
def prevsong(event):
   global index
   index -= 1
   pygame.mixer.music.load(list_of_songs[index])
   pygame.mixer.music.play()
   updatelabel()

def stopsong(event):
    # stop the current song which is playing
    pygame.mixer.music.stop()
    # set our Label to empty
    v.set("")
    #return songname

label = Label(root,text='Music Player') # set the heading
label.pack() # pack it inside root window

real_names.reverse()

for items in real_names:
    listbox.insert(0,items)

real_names.reverse()

nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()

stopbutton = Button(root,text='Stop Music')
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

song_label.pack()

root.mainloop()
hbh
