from pytubefix import YouTube


class YoutubeDownloaderLibrary:

    def __init__(self, link: str):
        try:
            # object creation using YouTube
            self.yt_obj = YouTube(link)
        except:
            print("Connection Error")

    def downloading_a_single_video(self, save_path: str):

        # get the video with the highest resolution
        video_high_resolution = self.yt_obj.streams.get_highest_resolution()

        try:
            # downloading the video
            video_high_resolution.download(output_path=save_path)
            print("Video downloaded successfully!")
        except:
            print("Error!")


    def downloading_a_single_audio(self, save_path: str):

        # get audio only
        audio_only = self.yt_obj.streams.get_audio_only()

        try:
            # downloading the video
            audio_only.download(output_path=save_path)
            print("Audio downloaded successfully!")
        except:
            print("Error!")

if __name__ == '__main__':

    SAVE_PATH = r"D:/video"
    link = r"https://www.youtube.com/watch?v=k85mRPqvMbE&ab"
    test = YoutubeDownloaderLibrary(link=link)
    test.downloading_a_single_video(save_path=SAVE_PATH)
    #test.downloading_a_single_audio(save_path=SAVE_PATH)

