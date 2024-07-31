from driver import driver
from selenium.webdriver.common.by import By
import json

driver.get('https://www.linkedin.com/help/linkedin/answer/a564109')

table_selector = 'article div.article-content__rich-text-table table tbody'

tables = driver.find_elements(By.CSS_SELECTOR, table_selector)

filesCategoriesList = [ 'Image', 'Document', 'Video', 'Audio' ]

fileTypesDict = {}

for tbody in tables:
    category = filesCategoriesList[tables.index(tbody)]
    extentions = []
    for tr in tbody.find_elements(By.CSS_SELECTOR, 'tr')[1:]:
        extention : list[str] = [ tr.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text ]
        if "," in extention[0]:
            extention = [ ext.strip() for ext in extention[0].split(",") ]
        supported = "✓" in tr.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
        if supported:
            for ext in extention:
                fileTypesDict.update({ ext.lower() : category })

with open('FileTypes.json', 'wt') as file:
    json.dump(fileTypesDict, file)