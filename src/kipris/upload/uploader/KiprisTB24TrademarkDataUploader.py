from ...core.upload.KiprisDataBatchUploader import KiprisDataUploader

class KiprisTB24TrademarkDataUploader(KiprisDataUploader):
    def __init__(self):
        super().__init__()
        self.table_name = "TB24_company_trademark"