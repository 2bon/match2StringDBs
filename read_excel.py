import pandas as pd

data = pd.read_excel (r'test/井门.xls', sheet_name='已配置')
df = pd.DataFrame(data, columns= ['开出端子描述'])
print (df)