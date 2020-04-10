import pandas as pd

data = pd.read_excel (r'.\test\井门.xls')
df = pd.DataFrame(data, columns= ['开出端子描述'])
print (df)