import os
from pprint import pprint
from yt_concate.setting import CAPTIONS_DIR
from yt_concate.pipeline.steps.step import Step

class ReadCaptions(Step):
    def process(self,data,inputs,utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r' , encoding='utf-8') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line == True:
                        caption = line
                        captions[caption] = time
                        time_line = False
            data[caption_file] = captions

        pprint(data)
        return data





