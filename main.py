from tkinter import *
import Download
from tkinter import messagebox

class main():

    def __init__(self, dl):
        self.root = Tk()
        self.root.title('YouTube Video Downloader')
        self.root.geometry("400x250")
        self.clr = '#BA432A'
        self.root.configure(bg=self.clr)
        self.root.resizable(False, False)
        self.root.iconbitmap('icon/yt.ico')
        self.quality = IntVar()
        self.quality.set(0)
        self.url=''
        self.createframes()
        self.createlabels()
        self.createbuttons()
        self.dl=dl
        self.root.protocol('WM_DELETE_WINDOW',self.close)
        self.root.mainloop()

    def createframes(self):
        self.top=Frame(self.root,width=400,height=100,bg=self.clr)
        self.top.pack(side=TOP)
        self.bottom=Frame(self.root,width=400,height=50,bg=self.clr)
        self.bottom.pack(side=BOTTOM)
        self.left=Frame(self.root,width=400,height=100,bg=self.clr)
        self.left.pack(side=LEFT)
        #self.right = Frame(self.root, width=400, height=50, bg=self.clr)
        #self.right.pack(side=RIGHT)

    def createlabels(self):
        self.top_label = Label(self.top, font=('arial', 18, 'bold'), text="YouTube Video Downloader", fg='white', bg=self.clr).grid()
        self.url_label = Label(self.left, font=('arial', 12, 'bold'), text="Url:", anchor='w', fg='white', bg=self.clr).grid(row=1, column=0, padx=20)
        self.url = Entry(self.left, font=('arial', 10), width=30, bd=2, insertwidth=1)
        self.url.grid(row=1, column=2, padx=20, sticky=E)

    def createbuttons(self):
        clrurl_btn = Button(self.left, font=('arial', 12), text="Clear Url", fg='#000000', width=8,command=lambda: self.clr_url()).grid(row=4, column=2, padx=20, pady=10)
        download_btn = Button(self.left, font=('arial', 12), text="Download", fg='#000000', width=8,command=lambda: self.dl.download(url=self.url,quality=self.quality)).grid(row=5, column=2, padx=10,pady=5)
        qunatity_label = Label(self.bottom, font=('arial', 10), text="Quality:", anchor='w', bg=self.clr).grid(row=1,column=0,sticky=N,pady=10)
        but1 = Radiobutton(self.bottom, font=('arial', 10), text="1080p", variable=self.quality, value=0, bg=self.clr).grid(row=1,column=1,sticky=N,pady=10)
        but2 = Radiobutton(self.bottom, font=('arial', 10), text="720p", variable=self.quality, value=1, bg=self.clr).grid(row=1,column=2,sticky=N,pady=10)
        but3 = Radiobutton(self.bottom, font=('arial', 10), text="480p", variable=self.quality, value=2, bg=self.clr).grid(row=1,column=3,sticky=N,pady=10)
        but4 = Radiobutton(self.bottom, font=('arial', 10), text="360p", variable=self.quality, value=3, bg=self.clr).grid(row=1,column=4,sticky=N,pady=10)
        but5 = Radiobutton(self.bottom, font=('arial', 10), text="240p", variable=self.quality, value=4, bg=self.clr).grid(row=1,column=5,sticky=N,pady=10)
        but6 = Radiobutton(self.bottom, font=('arial', 10), text="144p", variable=self.quality, value=5, bg=self.clr).grid(row=1,column=6,sticky=N,pady=10)

    def clr_url(self):
        self.url.delete(0, 'end')

    def close(self):
        if(messagebox.askokcancel('Quit','Do you want to quit?')):
            self.root.destroy()
        else:
            pass

download=Download.Download()
main=main(download)
