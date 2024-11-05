from ...kipris.upload.uploader.KiprisTB24DesignDataUploader import KiprisTB24DesignDataUploader
from ...kipris.upload.uploader.KiprisTB24PatentDataUploader import KiprisTB24PatentDataUploader
from ...kipris.upload.uploader.KiprisTB24TrademarkDataUploader import KiprisTB24TrademarkDataUploader


## 예시 데이터 

def main():
    KiprisTB24PatentDataUploader().upload(pa)
    KiprisTB24DesignDataUploader().upload(de)
    KiprisTB24TrademarkDataUploader().upload(tr)
    

if __name__ == "__main__":
    main()