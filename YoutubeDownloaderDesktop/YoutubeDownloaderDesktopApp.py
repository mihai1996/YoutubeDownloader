import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from YoutubeDownloaderManager.YoutubeDownloaderLibrary import YoutubeDownloaderLibrary

class YoutubeDownloaderDesktopApp(tk.Tk):
    def __init__(self):
        super().__init__()


        self.title("Youtube Downloader")
        self.geometry('800x600')
        self.resizable(0, 0)

        # label for link
        self.label_link = ttk.Label(self, text='YoutubeLink', font=("Segoe UI", 14, "bold"))
        self.label_link.grid(column=0, row=0, sticky=tk.W, padx=5, pady=40)


        # entry for youtube link
        self.link_text = tk.StringVar()
        self.entry_link = ttk.Entry(self, textvariable=self.link_text, font=("Segoe UI", 12, "normal"), width=55)
        self.entry_link.grid(column=1, row=0, sticky=tk.W, padx=10, ipady=10)

        # label path
        self.label_path = ttk.Label(self, text='Select PATH', font=("Segoe UI", 14, "bold"))
        self.label_path.grid(column=0, row=1, sticky=tk.W, padx=5, pady=40)

        # entry for browse folder
        self.directory_text = tk.StringVar()
        self.entry_browse_folder = ttk.Entry(self, textvariable=self.directory_text, font=("Segoe UI", 12, "normal"), width=55)
        self.entry_browse_folder.grid(column=1, row=1, sticky=tk.W, padx=10, ipady=10)

        # create select path button
        self.select_path_button = ttk.Button(self, text="Browse Folder", width=16, command=self.browse_folder)
        self.select_path_button.grid(column=2, row=1, sticky=tk.E, padx=5, pady=40, ipadx=10, ipady=12)

        # create button for mp4 format download
        self.download_mp4_button = ttk.Button(self, text="Download mp4", width=36,
                                              command=lambda: YoutubeDownloaderLibrary(
                                                  link=self.entry_link.get()).downloading_a_single_video(
                                                  save_path=self.entry_browse_folder.get()))
        self.download_mp4_button.grid(column=1, row=3, sticky=tk.N, ipady=10)

        # create button for mp3 format download
        self.download_mp3_button = ttk.Button(self, text="Download mp3", width=36,
                                              command=lambda: YoutubeDownloaderLibrary(
                                                  link=self.entry_link.get()).downloading_a_single_audio(
                                                  save_path=self.entry_browse_folder.get()))
        self.download_mp3_button.grid(column=1, row=4, sticky=tk.N, pady=10, ipady=10)


    def browse_folder(self):

        folder_path = filedialog.askdirectory()
        self.entry_browse_folder.insert(0, folder_path)


if __name__ == '__main__':
    app = YoutubeDownloaderDesktopApp()
    app.mainloop(0)