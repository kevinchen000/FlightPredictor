import pandas as pd
import numpy
import pickle

from dask_ml.wrappers import Incremental
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import BernoulliNB

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score

filenames = ['2018aJan.csv']#'2019_Complete.csv', '2019_Complete_Abb4.csv']
itPD = 0
itDA = 0
itCP = 0
RSEED = 42

############# Delay Percent Chance

##This entire block of code creates one Encoder, Scaler, MLP and RF instance each
##This is necessary because we can't refit the learner for every month,
##there will be errors for Enc and Scaler, and we will also
##not build on previous months' learnings for MLP and RF if we refit

#Create one single learner instance to be used throughout this code block instead of refitting everytime
mlpPD = MLPClassifier(hidden_layer_sizes=(5,5),max_iter=300, activation = 'relu',
                      solver = 'adam',learning_rate_init = 0.001, beta_1 =0.5,
                      alpha = 0.01, shuffle = True)
#rfPD = BernoulliNB(alpha=0.5, binarize=0.0, fit_prior=True, class_prior=None)
#rfPD = RandomForestClassifier(n_estimators=100,random_state=RSEED,max_features='sqrt',
 #                             n_jobs=-1, warm_start=True)

##Wrap learner in Incremental. Use this from now on as model. Will help with batching
learnermlpPD = Incremental(mlpPD)
#learnerrfPD = Incremental(rfPD)

#Need to get encoded fit for the first set of data and apply to all other months.
#Refitting each time causes errors
df = pd.read_csv(filenames[0])
#df['FL_DATE'] = df['FL_DATE'].astype(str)
df['OP_UNIQUE_CARRIER'] = df['OP_UNIQUE_CARRIER'].astype(str)
df['ORIGIN'] = df['ORIGIN'].astype(str)
#df['DEP_TIME'] = df['DEP_TIME'].astype(str)
x_PD = df[['FL_DATE', 'DEP_TIME','OP_UNIQUE_CARRIER','ORIGIN']]
#'DATE_INT','DEP_HOUR'
y_PD = df['DEP_DELAY_IND']
x_trainPD, x_testPD, y_trainPD, y_testPD = train_test_split(x_PD,y_PD,test_size=0.10,
                                                            shuffle = True, stratify=y_PD)
print('PD done splitting data')
#Create one instance of OneHotEncoder. Fit that instance and use it throughout code
enc_xtrainPD = OneHotEncoder(handle_unknown='ignore')
encPD = enc_xtrainPD.fit(x_trainPD)

#OneHotEncoder instance encoding X data
x_trainPD = encPD.transform(x_trainPD)
x_testPD =  encPD.transform(x_testPD)

##Create Scaler instance and scale data for MLP.
scalerPD = StandardScaler(with_mean=False)
scalerPD.fit(x_trainPD)

#Scale Data using scaled instance
x_trainPDscaled = scalerPD.transform(x_trainPD)
x_testPDscaled = scalerPD.transform(x_testPD)

##### MLP Model
learnermlpPD.fit(x_trainPDscaled,y_trainPD,classes=numpy.unique(y_trainPD))
print('PD done training model')
#result = mlpPD.predict([[1,1,1,1]])
#prob_results = mlpPD.predict_proba([[1,1,1,1]])

##### Random Forest Model
##learnerrfPD.fit(x_trainPDscaled,y_trainPD, classes=numpy.unique(y_trainPD))
##
##forest_result = model.predict([[1,1,1,1]])
##forest_prob_result = model.predict_proba([[1,1,1,1]])


#####Testing
predictions_mlpPD = learnermlpPD.predict(x_testPDscaled)
##predictions_forestPD = learnerrfPD.predict(x_testPDscaled)
print('PD done predicting')

print('NN PD Confusion Matrix\n' + str(confusion_matrix(y_testPD,predictions_mlpPD)) + '\n')
print('NN PD Classification Report \n' + classification_report(y_testPD,predictions_mlpPD))
##print('RF Confusion Matrix\n' + str(confusion_matrix(y_testPD,predictions_forestPD)) + '\n')
##print('RF Classification Report \n'+ classification_report(y_testPD,predictions_forestPD))
##
############### Delay Amount

#Create one single learner instance to be used throughout this code block
mlpDA = MLPClassifier(hidden_layer_sizes=(4,4),max_iter=300, activation = 'relu',
                      solver = 'adam',alpha = 0.01,learning_rate_init = 0.001,
                      shuffle = True, warm_start=True)
#rfDA = RandomForestClassifier(n_estimators=100,random_state=RSEED,max_features='sqrt',
#                              n_jobs=-1, warm_start=True)
##Wrap learner in Incremental. Use this from now on as model. Will help with batching
learnermlpDA = Incremental(mlpDA)
#learnerrfDA = Incremental(rfDA)

#Need to get encoded fit for the first set of data and apply to all other months.
#Refitting each time causes errors
df = pd.read_csv(filenames[0])
#df['FL_DATE'] = df['FL_DATE'].astype(str)
df['OP_UNIQUE_CARRIER'] = df['OP_UNIQUE_CARRIER'].astype(str)
df['ORIGIN'] = df['ORIGIN'].astype(str)
#df['DEP_TIME'] = df['DEP_TIME'].astype(str)
x_DA = df[['FL_DATE','DEP_TIME','OP_UNIQUE_CARRIER','ORIGIN']]
#x_DA = df[['DATE_INT','DEP_HOUR','OP_UNIQUE_CARRIER','ORIGIN']]
y_DA = df['DEP_DELAY']
x_trainDA, x_testDA, y_trainDA, y_testDA = train_test_split(x_DA,y_DA,test_size = 0.1,
                                                            shuffle = True,)#stratify=y_DA)
print('DA done splitting data')
#print(x_testDA)
#Create one OneHotEncoder instance. Fit that instance and use it throughout code block
enc_xtrainDA = OneHotEncoder(handle_unknown='ignore')
encDA = enc_xtrainDA.fit(x_trainDA)

#OneHotEncoder module encoding X data

x_trainDA= encDA.transform(x_trainDA)

x_testDA=encDA.transform(x_testDA)


#print(x_testDAmerged)
##Create one Scaler instance and scale data for MLP. 
scalerDA = StandardScaler(with_mean=False)
scalerDA.fit(x_trainDA)

#Scale data using Scaled instance
x_trainDAscaled = scalerDA.transform(x_trainDA)
x_testDAscaled = scalerDA.transform(x_testDA)

##### MLP Model
learnermlpDA.fit(x_trainDAscaled,y_trainDA,classes=numpy.unique(y_trainDA))
print('DA done training model')

##### Random Forest Model
#learnerrfDA.fit(x_trainDAscaled,y_trainDA)
#predictions_forestDA = learnerrfDA.predict(x_testDAscaled)


#######Testing
predictions_mlpDA = learnermlpDA.predict(x_testDAscaled)
print('DA done predicting')

print('NN DA Confusion Matrix\n' + str(confusion_matrix(y_testDA,predictions_mlpDA)) + '\n')
print('NN DA Classification Report \n' + classification_report(y_testDA,predictions_mlpDA))

############# Cancellation Percent
#Create one single learner instance to be used throughout this code block
mlpCP = MLPClassifier(hidden_layer_sizes=(5,5),max_iter=300, activation = 'relu',
                      solver = 'adam',alpha = 0.01,shuffle=True, warm_start=True)
#rfCP = RandomForestClassifier(n_estimators=100,random_state=RSEED,max_features='sqrt',
#                              n_jobs=-1, warm_start=True)
##Wrap learner in Incremental. Use this from now on as model. Will help with batching
learnermlpCP = Incremental(mlpCP)
#learnerrfCP = Incremental(rfCP)

#Need to get encoded fit for the first set of data and apply to all other months.
#Refitting each time causes errors
df = pd.read_csv(filenames[0])
#df['FL_DATE'] = df['FL_DATE'].astype(str)
df['OP_UNIQUE_CARRIER'] = df['OP_UNIQUE_CARRIER'].astype(str)
df['ORIGIN'] = df['ORIGIN'].astype(str)
#df['DEP_TIME'] = df['DEP_TIME'].astype(str)
x_CP = df[['FL_DATE', 'DEP_TIME','OP_UNIQUE_CARRIER','ORIGIN']]
y_CP = df['CANCELLED']
x_trainCP, x_testCP, y_trainCP, y_testCP = train_test_split(x_CP,y_CP,test_size=0.10,
                                                            shuffle = True, stratify=y_CP)
print('CP done splitting data')

#Create one OneHotEncoder instance. Fit that instance and use it throughout code block
enc_xtrainCP = OneHotEncoder(handle_unknown='ignore')
encCP = enc_xtrainCP.fit(x_trainCP)

#OneHotEncoder module encoding X data
x_trainCP = encCP.transform(x_trainCP)
x_testCP =  encCP.transform(x_testCP)

##Create one Scaler instance and scale data for MLP.
scalerCP = StandardScaler(with_mean=False)
scalerCP.fit(x_trainCP)

#Scale data with Scaled instance
x_trainCPscaled = scalerCP.transform(x_trainCP)
x_testCPscaled = scalerCP.transform(x_testCP)

##### MLP Model
learnermlpCP.fit(x_trainCP,y_trainCP,classes=numpy.unique(y_trainCP))
print('CP done training model')

##### Random Forest Model
##learnerrfCP.fit(x_trainCPscaled,y_trainCP)
##predictions_forestCP = learnerrfCP.predict(x_testCPscaled)


#######Testing
predictions_mlpCP = learnermlpCP.predict(x_testCPscaled)
print('CP done predicting')

print('NN CP Confusion Matrix\n' + str(confusion_matrix(y_testCP,predictions_mlpCP)) + '\n')
print('NN CP Classification Report \n' + classification_report(y_testCP,predictions_mlpCP))

##Save Encoded models for all 3 categories by pickling. Run this once to create the files.
##create txt files
outfile_encPD = open('encPD','wb')
outfile_encDA = open('encDA','wb')
outfile_encCP = open('encCP','wb')

##dump models to files and close
pickle.dump(encPD, outfile_encPD)
outfile_encPD.close()
pickle.dump(encDA, outfile_encDA)
outfile_encDA.close()
pickle.dump(encCP, outfile_encCP)
outfile_encCP.close()


##Save ML models for all 3 categories by pickling. Run this once to create the files.
##create txt files
outfile_mlpPD = open('mlpPD','wb')
#outfile_rfPD = open('rfPD','wb')
outfile_mlpDA = open('mlpDA','wb')
##outfile_rfDA = open('rfDA','wb')
outfile_mlpCP = open('mlpCP','wb')
##outfile_rfCP = open('rfCP','wb')

##dump models to files and close
pickle.dump(learnermlpPD, outfile_mlpPD)
outfile_mlpPD.close()
#pickle.dump(learnerrfPD, outfile_rfPD)
#outfile_rfPD.close()
pickle.dump(learnermlpDA, outfile_mlpDA)
outfile_mlpDA.close()
##pickle.dump(learnerrfDA, outfile_rfDA)
##outfile_rfDA.close()
pickle.dump(learnermlpCP, outfile_mlpCP)
outfile_mlpCP.close()
##pickle.dump(learnerrfCP, outfile_rfCP)
##outfile_rfCP.close()


###Calculate Accuracy of ML and RF
acc_mlpPD=int(); acc_mlpDA=int(); acc_mlpCP=int()
#acc_rfPD=int(); acc_rfDA=int(); acc_rfCP=int()

acc_mlpPD = accuracy_score(y_testPD,predictions_mlpPD)
#acc_rfPD = accuracy_score(y_testPD, predictions_forestPD)
acc_mlpDA = accuracy_score(y_testDA,predictions_mlpDA)
#acc_rfDA = accuracy_score(y_testDA, predictions_forestDA)
acc_mlpCP = accuracy_score(y_testCP,predictions_mlpCP)
#acc_rfCP = accuracy_score(y_testCP, predictions_forestCP)

##Save Accuracy calc for ML and RF
##create txt files
outfile_acc_mlpPD = open('accmlpPD','wb')
#outfile_acc_rfPD = open('accrfPD','wb')
outfile_acc_mlpDA = open('accmlpDA','wb')
#outfile_acc_rfDA = open('accrfDA','wb')
outfile_acc_mlpCP = open('accmlpCP','wb')
#outfile_acc_rfCP = open('accrfCP','wb')

##dump models to files and close
pickle.dump(acc_mlpPD, outfile_acc_mlpPD)
outfile_acc_mlpPD.close()
#pickle.dump(acc_rfPD, outfile_acc_rfPD)
#outfile_acc_rfPD.close()
pickle.dump(acc_mlpDA, outfile_acc_mlpDA)
outfile_acc_mlpDA.close()
#pickle.dump(acc_rfDA, outfile_acc_rfDA)
#outfile_acc_rfDA.close()
pickle.dump(acc_mlpCP, outfile_acc_mlpCP)
outfile_acc_mlpCP.close()
#pickle.dump(acc_rfCP, outfile_acc_rfCP)
#outfile_acc_rfCP.close()


###Calculate F1 score of ML and RF
f1_mlpPD=float(); f1_mlpDA=float(); f1_mlpCP=float()
#f1_rfPD=float(); f1_rfDA=float(); f1_rfCP=float()

f1_mlpPD = f1_score(y_testPD, predictions_mlpPD, average = 'weighted')
#f1_rfPD = f1_score(y_testPD, predictions_forestPD, average = 'weighted')
f1_mlpDA = f1_score(y_testDA,predictions_mlpDA, average = 'weighted')
#f1_rfDA = f1_score(y_testDA, predictions_forestDA, average = 'weighted')
f1_mlpCP = f1_score(y_testCP,predictions_mlpCP, average = 'weighted')
#f1_rfCP = f1_score(y_testCP, predictions_forestCP, average = 'weighted')

##Save F1 calc for ML and RF
##create txt files
outfile_f1_mlpPD = open('f1mlpPD','wb')
#outfile_f1_rfPD = open('f1rfPD','wb')
outfile_f1_mlpDA = open('f1mlpDA','wb')
#outfile_f1_rfDA = open('f1rfDA','wb')
outfile_f1_mlpCP = open('f1mlpCP','wb')
#outfile_f1_rfCP = open('f1rfCP','wb')

##dump models to files and close
pickle.dump(f1_mlpPD, outfile_f1_mlpPD)
outfile_f1_mlpPD.close()
#pickle.dump(f1_rfPD, outfile_f1_rfPD)
#outfile_f1_rfPD.close()
pickle.dump(f1_mlpDA, outfile_f1_mlpDA)
outfile_f1_mlpDA.close()
#pickle.dump(f1_rfDA, outfile_f1_rfDA)
#outfile_f1_rfDA.close()
pickle.dump(f1_mlpCP, outfile_f1_mlpCP)
outfile_f1_mlpCP.close()
#pickle.dump(f1_rfCP, outfile_f1_rfCP)
#outfile_f1_rfCP.close()


###############################Previous Code######################################################

##Results from the PD code block
### Printed Test Results
##print('\nAccuracy of MLPClassifier: ' + str(accuracy_score(y_testPD, predictions_mlpPD)))
##print('Probability of 0 (MLP): ' + str(prob_results[0][0]))
##print('Probability of 1 (MLP): ' + str(prob_results[0][1]) + '\n')

##print('\nAccuracy of RandomForest: ' + str(accuracy_score(y_testPD, predictions_forestPD)))
##print('Probability of 0 (RF): ' + str(forest_prob_result[0][0]))
##print('Probability of 1 (RF): ' + str(forest_prob_result[0][1]) + '\n')


###Dan Test Cases####
# predPD1 = [[1,1,"OH","CLT"]]
# predPD1 = encPD.transform(predPD1)
# print(mlpPD.predict_proba(predPD1))
# print(rfPD.predict_proba(predPD1))
# print(accuracy_score(y_testPD,predictions_mlpPD))
# print(accuracy_score(y_testPD,predictions_forestPD))
#
# predPD2 = [[1,1,"NK","LAX"]]
# predPD2 = encPD.transform(predPD2)
# print(mlpPD.predict_proba(predPD2))
# print(rfPD.predict_proba(predPD2))

####Save y-test data for all 3 categories by pickling. Run this once to create the files.
####create txt files
##outfile_y_testPD = open('y_testPD','wb')
##outfile_y_testDA = open('y_testDA','wb')
##outfile_y_testCP = open('y_testCP','wb')
##
####dump models to files and close
##pickle.dump(y_testPD, outfile_y_testPD)
##outfile_y_testPD.close()
##pickle.dump(y_testDA, outfile_y_testDA)
##outfile_y_testDA.close()
##pickle.dump(y_testCP, outfile_y_testCP)
##outfile_y_testCP.close()

####Save ML predictions for all 3 categories by pickling. Run this once to create the files.
####create txt files
##outfile_predictions_mlpPD = open('predictions_mlpPD','wb')
##outfile_predictions_forestPD = open('predictions_forestPD','wb')
##outfile_predictions_mlpDA = open('predictions_mlpDA','wb')
##outfile_predictions_forestDA = open('predictions_forestDA','wb')
##outfile_predictions_mlpCP = open('predictions_mlpCP','wb')
##outfile_predictions_forestCP = open('predictions_forestCP','wb')

####dump predictions to files and close
##pickle.dump(predictions_mlpPD, outfile_predictions_mlpPD)
##outfile_predictions_mlpPD.close()
##pickle.dump(predictions_forestPD, outfile_predictions_forestPD)
##outfile_predictions_forestPD.close()
##pickle.dump(predictions_mlpDA, outfile_predictions_mlpDA)
##outfile_predictions_mlpDA.close()
##pickle.dump(predictions_forestDA, outfile_predictions_forestDA)
##outfile_predictions_forestDA.close()
##pickle.dump(predictions_mlpCP, outfile_predictions_mlpCP)
##outfile_predictions_mlpCP.close()
##pickle.dump(predictions_forestCP, outfile_predictions_forestCP)
##outfile_predictions_forestCP.close()
