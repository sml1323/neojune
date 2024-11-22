from lxml import etree

def sum_total_count(xml_file, ):
    # XML 파일을 파싱하여 루트 요소 가져오기
    tree = etree.parse(xml_file)
    root = tree.getroot()

    # totalCount 값을 찾아 합산
    total_sum = sum(int(item.text) for item in root.xpath(".//totalCount") if item.text.isdigit())
    total_sum_search = sum(int(item.text) for item in root.xpath(".//TotalSearchCount") if item.text.isdigit())
    
    return total_sum + total_sum_search

#XML 파일 경로 설정
total_sum = 0 
print("company")
for data in ['design', 'patent', 'trademark']:
    xml_file_path = f"/home/ubuntu/app/res/output/20241121/xml/company/{data}.xml" # 파일 경로를 여기에 입력하세요
    total_count_sum = sum_total_count(xml_file_path)
    total_sum += total_count_sum
    print(f"{data} Total count sum:", total_count_sum)

print(total_sum)
print('--------------')
total_sum = 0 
print("university")
for data in ['design', 'patent', 'trademark']:
    xml_file_path = f"/home/ubuntu/app/res/output/20241121/xml/university/{data}.xml" # 파일 경로를 여기에 입력하세요
    total_count_sum = sum_total_count(xml_file_path)
    total_sum += total_count_sum
    print(f"{data} Total count sum:", total_count_sum)

print(total_sum)