import pandas as pd

df = pd.DataFrame()
for i in range(8):
    filename = 'nuforc'+str(i+1)+'_final.xlsx'
    data = pd.read_excel( filename )
    print(filename, "done.")
    df = df.append(data)

print(df)
#df.to_excel( 'nuforc_final.xlsx' )
