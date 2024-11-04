from ....db.mysql import Mysql



class KiprisDataUploader:
    def __init__(self):
        self.mysql = Mysql()
        self.table_name = None

    def upload(self, data):
        # 데이터가 리스트라면, 각 항목을 개별적으로 업로드
        self.mysql.upsert_data(self.table_name, data)



