from yt_concate.pipeline.steps.step import Step
from yt_concate.setting import VIDEOS_DIR
from pytube import YouTube
class DownloadVideos(Step):
    def process(self,data,inputs,utils):
        yt_set = set([found.yt for found in data])
        print('videos to download=', len(yt_set))
        for yt in yt_set:
            url = yt.url


            if utils.video_file_exists(yt):
                print(f'found existing video file for{url}','skipping')

                continue

            print('downloading',url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id +'.mp4')


        return data