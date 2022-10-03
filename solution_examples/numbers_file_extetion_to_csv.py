
import pandas as pd
from numbers_parser import Document

# Конвертация формата файла `.numbers` в `.csv`

doc = Document("data/data_example.numbers")

sheets = doc.sheets
tables = sheets[0].tables
rows = tables[0].rows(values_only=True)

# Количество листов в документе
print(sheets._items)

# Узнать имя листа
print(sheets[0].name)

# Узнать количество таблиц
print(tables._items)

# Конвертация в CSV
df = pd.DataFrame(rows[1:], columns=rows[0])
print(df.head())
df.to_csv('data/data_example.csv')
