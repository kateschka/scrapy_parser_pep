from pathlib import Path


BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ALLOWED_DOMAINS = ['peps.python.org']
SPIDER_NAME = 'pep'
START_URLS = ['https://peps.python.org/']

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = 'results'

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}
