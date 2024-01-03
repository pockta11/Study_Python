#pip install pandas
#pip install openpyxl
import pandas as pd  

user_list=pd.read_excel('sample.xlsx', sheet_name='Sheet1', engine='openpyxl')
print(user_list)

