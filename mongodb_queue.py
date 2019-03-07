from datetime import datetime, timedelta
from pymongo import MongoClient, errors


class MogoQueue():

    OUTSTANDING = 1
    PROCESSING = 2
    COMPLETE = 3

    def __init__(self, db, collection, timeout=300):
        self.client = MongoClient('mongodb://zhi:189154@127.0.0.1:27017/meinv')
        self.Client = self.client[db]
        self.db = self.Client[collection]
        self.timeout = timeout

    def __bool__(self):
        record = self.db.find_one({'status': {'$ne': self.COMPLETE}})
        return True if record else False

    def push(self, url, title, name):
        try:
            self.db.insert({
                '_id': url,
                'status': self.OUTSTANDING,
                '主题': title,
                'name': name
            })
            print(url, '插入队列成功')
        except errors.DuplicateKeyError as e:
            print(url, '已经存在于队列中')
            pass

    def pop(self):
        record = self.db.find_and_modify(
            query={'status': self.OUTSTANDING},
            update={
                '$set': {
                    'status': self.PROCESSING,
                    'timestamp': datetime.now()
                }
            })
        if record:
            return (record['_id'], record['name'])
        else:
            self.repair()
            raise KeyError

    def pop_title(self, url):
        record = self.db.find_one({'_id': url})
        return record['主题']

    def pop_title_(self, url):
        record = self.db.find_one({'_id': url})
        if record:
            return record['主题']
        else:
            return "不知其名"

    def peek(self):
        record = self.db.find_one({'status': self.OUTSTANDING})
        if record:
            return record['_id']

    def complete(self, url):
        self.db.update({'_id': url}, {'$set': {'status': self.COMPLETE}})

    def repair(self):
        record = self.db.find_and_modify(
            query={
                'timestamp': {
                    '$lt': datetime.now() - timedelta(seconds=self.timeout)
                },
                'status': {
                    '$ne': self.COMPLETE
                }
            },
            update={
                '$set': {
                    'status': self.OUTSTANDING
                }
            })
        if record:
            print('重置url状态', record['_id'])

    def clear(self):
        self.db.drop()
