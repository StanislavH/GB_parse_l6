BOT_NAME = 'leroy_images'

SPIDER_MODULES = ['Leroy.spiders']
NEWSPIDER_MODULE = 'Leroy.spiders'


ROBOTSTXT_OBEY = False


ITEM_PIPELINES = {'Leroy.pipelines.LeroyPipeline': 1,
                  #'leroymerlinparser.pipelines.DataBasePipeline': 300,
                  }

FILES_STORE = r'downloaded'


DOWNLOAD_DELAY = 3

