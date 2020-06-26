import sqlite3
import tkinter
# try:
#     import tkinter
# except ImportError:
#     import Tkinter as tkinter


conn = sqlite3.connect("music.sqlite")

class Scrollbox(tkinter.Listbox):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient= tkinter.VERTICAL, command= self.yview)

    def grid(self, row, column, sticky='nse', rowspan=1, columnsapan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky,
        # rowspan=rowspan, **kwargs)
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnsapan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


def get_albums(event):
    lb = event.widget
    #print(lb.curselection()[0])
    index = lb.curselection()[0]
    artist_name = lb.get(index),

    artist_id = conn.execute("SELECT artists._id FROM artists WHERE (artists.name=?)", artist_name).fetchone()
    alist = []
    for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name", artist_id):
        alist.append(row[0])
        albumLV.set(tuple(alist))
        songLV.set(("Choose an Album first",))

def get_songs(event):
        lb = event.widget
        index = int(lb.curselection()[0])
        album_name = lb.get(index),

        album_id = conn.execute("SELECT albums._id FROM albums WHERE (albums.name=?)", album_name).fetchone()
        alist = []
        for x in conn.execute("SELECT songs.title FROM songs WHERE (songs.album = ?) ORDER BY songs.track", album_id):
            alist.append(x[0])
        songLV.set(tuple(alist))


mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry('1024x768')
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)  # space column

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ======= labels ========
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# ======= Artists Listbox =========
#artistList = tkinter.Listbox(mainWindow)
artistList = Scrollbox(mainWindow, background='orange')
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

# artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
# artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
# artistList['yscrollcommand'] = artistScroll.set

for artist in conn.execute("SELECT name from artists ORDER BY name"):
    artistList.insert(tkinter.END, artist[0])

artistList.bind('<<ListboxSelect>>', get_albums)

# ======= Albums Listbox =========
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an Artist",))
albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)
albumList = Scrollbox(mainWindow, listvariable=albumLV, background='white')
albumList.grid(row=1, column=1, sticky='nsew', padx=(30,0))
albumList.config(border=2, relief='sunken')

# albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
# albumScroll.grid(row=1, column=1, sticky='nse', rowspan=1)
# albumList['yscrollcommand'] = albumScroll.set

albumList.bind('<<ListboxSelect>>', get_songs)

# ======== Sogn Listbox ==========
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose a Song",))
# songList = tkinter.Listbox(mainWindow, listvariable=songLV)
songList = Scrollbox(mainWindow, listvariable=songLV,background='green')
songList.grid(row=1,column=2, sticky='nsew', padx=(30,0))
songList.config(border=2, relief='sunken')

# ======== Main Loop ===========
# testList = range(1, 100)
# albumLV.set((1, 2, 3, 4, 5))
# albumLV.set(tuple(testList))
# songLV.set(('Baby', 'Sorry'))


mainWindow.mainloop()
print("Closing database connections")
conn.close()