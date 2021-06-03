# parquet file is not human readable. one can use python to read parquet file format
# prerequisite
# pip install pandas, pip install pyarrow
import pandas as pd

parquet_file = r'/Users/najmeh.foroozani/PycharmProjects/pythonProject/AWS-demo/S3/userdata1.parquet'
df = pd.read_parquet(parquet_file,engine="auto")
df.sort_values('first_name') 