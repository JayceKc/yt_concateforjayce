from yt_concate.pipeline.steps.getvideolist import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.readcaptions import ReadCaptions
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.utils import Utils
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.initializeyt import InitializeYT
from yt_concate.pipeline.steps.search import Search

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word' : 'incredible'
    }
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        Postflight()

    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)

if __name__ == '__main__':
    main()