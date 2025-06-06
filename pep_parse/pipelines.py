import os

from datetime import datetime


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = {}
        feed_path = list(spider.settings.get('FEEDS').keys())[0]
        self.results_dir = os.path.dirname(feed_path)

    def close_spider(self, spider):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(
            self.results_dir, f'status_summary_{timestamp}.csv')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.status_count.items():
                f.write(f'{status},{count}\n')
            f.write(f'Total,{sum(self.status_count.values())}\n')

    def process_item(self, item, spider):
        status = item['status']
        self.status_count[status] = self.status_count.get(status, 0) + 1
        return item
