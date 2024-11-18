from ...core.upload.KiprisDataBatchUploader import KiprisDataUploader

class KiprisTB24DesignDataUploader(KiprisDataUploader):
    def __init__(self):
        super().__init__()
        self.table_name = "TB24_company_design"