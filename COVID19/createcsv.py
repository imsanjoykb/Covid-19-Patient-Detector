#importing essential libraries
import random
import pandas as pd
import numpy as np

#create data using random module
idx = np.arange(100)
fever_list=[]
for i in range(2500):
	fever_data ='{:04.3f}'.format(random.uniform(93, 104))
	fever_list.append(fever_data)
fever = np.array(fever_list)

#fever = np.random.randint(92.0,104.0,size=2500)
bodyPain  = np.random.randint(2,size=2500)
age  = np.random.randint(20,80,size=2500)
runnyNose  = np.random.randint(2,size=2500)
diffBreath  = np.random.randint(-1,2,size=2500)
infectionProb  = np.random.randint(2,size=2500)

#initialize data
data = {'fever':fever,'bodyPain':bodyPain,'age':age,'runnyNose':runnyNose,'diffBreath':diffBreath,'infectionProb':infectionProb}

#create dataframe
df = pd.DataFrame(data)

#save csv file
df.to_csv('data.csv',index=False)