#importing essential libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

#create a function
def data_split(data,ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data)*ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]

if __name__ == '__main__':
	#read a csv file
	df = pd.read_csv("corona.csv")
	train,test = data_split(df,0.2)

	#Splitting the dataset into Training set and Test set
	X_train = train[['fever','bodyPain','age','runnyNose','diffBreath']].to_numpy()
	X_test = test[['fever','bodyPain','age','runnyNose','diffBreath']].to_numpy()
	y_train = train[['infectionProb']].to_numpy().reshape(2000 ,)
	y_test = test[['infectionProb']].to_numpy().reshape(500 ,)

	#Creating a Logistic Regression model
	clf = LogisticRegression()
	clf.fit(X_train,y_train)

	#open a file, where you wany to store  the data
	file = open('model.pkl','wb')

	#dump information to that file
	pickle.dump(clf,file)
	file.close()