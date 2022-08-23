import pandas as pd
from halo import Halo
import gc

text = "Processing breeds.json to parquet format"
spinner = Halo(text=text, spinner='dots2')
spinner.start()
breeds_data = pd.read_csv('data/raw/dogbreeds-master/breeds.csv').set_index('breed')
# del breeds_data['url']
# del breeds_data['breed_group']
# del breeds_data['height']
# del breeds_data['weight']
# del breeds_data['life_span']
breeds_data.to_parquet('data/pre-processed/breeds.parquet', engine='pyarrow')

spinner.stop_and_persist(symbol='✅', text='breeds_data.parquet exported!')

# user data
text = "Processing user_survey_data.csv to parquet format"
spinner = Halo(text=text, spinner='dots2')
spinner.start()
# change csv to json later
user_survey_data = pd.read_csv("data/raw/user_survey_data.csv").set_index('userId')

user_survey_data.to_parquet("data/pre-processed/user_survey_data.parquet", engine='pyarrow')

spinner.stop_and_persist(symbol='✅', text="user_survey_data.parquet exported!")

# change csv to json later
# text="Processing adopted_data.csv to parquet format"
# spinner=Halo(text=text, spinner='dots2')
# spinner.start()
# adopted_data=pd.read_csv("../data/raw/adopted_data.csv", lines=True)
# adopted_data.to_parquet("../data/pre-processed/adopted_data.parquet", engine='pyarrow')
#
# spinner.stop_and_persist(symbol='✅', text="adopted_data.parquet exported!")
#
# # change csv to json later
# text="Processing abandoned_data.csv to parquet format"
# spinner=Halo(text=text, spinner='dots2')
# spinner.start()
# abandoned_data=pd.read_csv("../data/raw/abandoned_data.csv", lines=True)
# abandoned_data.to_parquet("../data/pre-processed/abandoned_data.parquet", engine='pyarrow')
#
# spinner.stop_and_persist(symbol='✅', text="abandoned_data.parquet exported!")

del breeds_data
del user_survey_data
# del adopted_data
# del abandoned_data
gc.collect()

print(" Your data is ready to be used! ")

