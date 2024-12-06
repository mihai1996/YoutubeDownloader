from pytubefix import YouTube


class YoutubeDownloaderLibrary:

    def downloading_a_single_video(self, save_path: str, link: str):

        try:
            # object creation using YouTube
            yt_obj = YouTube(link)

        except:
            print("Connection Error")

        # get the video with the highest resolution
        video_high_resolution = yt_obj.streams.get_highest_resolution()

        try:
            # downloading the video
            video_high_resolution.download(output_path=save_path)
            print("Video downloaded successfully!")
        except:
            print("Error!")


    def downloading_a_single_audio(self, save_path: str, link: str):

        try:
            # object creation using YouTube
            yt_obj = YouTube(link)
        except:
            print("Connection Error")

        # get audio only
        audio_only = yt_obj.streams.get_audio_only()

        try:
            # downloading the video
            audio_only.download(output_path=save_path)
            print("Audio downloaded successfully!")
        except:
            print("Error!")


SAVE_PATH = r"D:/video"
link = r"https://www.youtube.com/watch?v=k85mRPqvMbE&ab"
test = YoutubeDownloaderLibrary()
test.downloading_a_single_video(save_path=SAVE_PATH, link=link)
test.downloading_a_single_audio(save_path=SAVE_PATH, link=link)

