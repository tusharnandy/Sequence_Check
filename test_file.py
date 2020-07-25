from seq_check import Sequence

# How to create csv file for input:
# 1. make sure your data (size=20) is in a numpy array (say 'data', with 20 numbers)
# 2. Simply convert it to dataframe without headers:
#     dataframe = pd.DataFrame(data)
#     dataframe.to_csv("test.csv")

s = Sequence("test.csv")
df = s.all_datasets()

print(df)
# df.to_csv("test_output.csv")
# Check the format of output file in "test_output.csv"
