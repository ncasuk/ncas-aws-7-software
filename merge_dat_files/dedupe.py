#!/nfs/foe-data-32/export/ncas/lecjlg/Documents/anaconda3/bin/python

import pandas as pd
df = pd.read_csv("output/2010.csv",low_memory=False)

#df = pd.DataFrame(['a','b','c','d','a','b'])
df["is_duplicate"]= df.duplicated()
print(df.to_string())
