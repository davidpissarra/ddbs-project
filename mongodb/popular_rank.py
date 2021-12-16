from collection import *
import pandas as pd


class PopularRank(Collection):
    @classmethod
    def popular_rank(cls):
        return {'daily': MongoDatabase.database().popular_rank_daily,
                'weekly': MongoDatabase.database().popular_rank_weekly,
                'monthly': MongoDatabase.database().popular_rank_monthly}

    @classmethod
    def write(cls, insert_dict):
        PopularRank.popular_rank()['daily'].bulk_write(list(insert_dict['daily']), ordered=True)
        PopularRank.popular_rank()['weekly'].bulk_write(list(insert_dict['weekly']), ordered=True)
        PopularRank.popular_rank()['monthly'].bulk_write(list(insert_dict['monthly']), ordered=True)


class ReadTime:
    def __init__(self, timestamp):
        t = pd.to_datetime(int(timestamp), unit='ms')
        self.read_timestamp = {
            'daily': f'{t.day}-{t.month}-{t.year}',
            'weekly': f'{t.week}-{t.year}',
            'monthly': f'{t.month}-{t.year}'
        }
