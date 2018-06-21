from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox
import os


class Download():
    def download(self, url, quality):
        downloaded = False
        try:
            self.status=True
            yturl = str(url.get().strip())
            obj = YouTube(yturl)
            options = obj.streams.all()
            opt = ["1080p", "720p", "480p", "360p", "240p", "144p"]
            for i in options:
                try:
                    if (str(i).find('res=\"' + opt[quality.get()] + '\"') != -1):
                        temp = str(filedialog.askdirectory())
                        path2 = temp.replace('/', '//')
                        messagebox.showinfo("Notification", "Downloading...")
                        i.download(path2)
                        downloaded = True
                        messagebox.showinfo("Notification", "Video Downloaded")
                        clr_url()
                        break
                except:
                    if(downloaded==False):
                        messagebox.showinfo("Error", "This quality option is not available, Please try another option.")
                        downloaded = True
                    break;
            if (downloaded == False):
                raise Exception
        except:
            if (downloaded == False):
                messagebox.showinfo("Error", "Please Enter a Valid Url or check Internet Connection.")
            else:
                pass
        self.status=False


if(__name__=='__main__'):
    print('Download Class')