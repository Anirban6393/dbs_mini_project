from sklearn.model_selection import cross_validate
from sklearn.metrics import classification_report, confusion_matrix
import pickle
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def pca_apply(x):
    pipe = Pipeline([('sc',StandardScaler()),
                 ('pca',PCA(n_components=5))])

    x_vectors=pipe.fit_transform(x.loc[:,'vect_1':'vect_148'])
    x_vectors=pd.DataFrame(x_vectors)
    x_vectors.columns = ['pca1','pca2','pca3','pca4','pca5']
    return x_vectors


class Modelevaluator(object):
    def __init__(self, model, x_train, x_test, y_train, y_test,validation_data):
        self.model = model
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test
        self.validation_data = validation_data
    
    
    def make_prediction(self):
        self.model.fit(self.x_train, self.y_train)
        return self.model.predict(self.x_test)

    
    def classification_report(self):
        y_pred = self.make_prediction()
        return print(classification_report(self.y_test, y_pred))
    
    
    def confusion_matrix(self):
        y_pred = self.make_prediction()
        fig, ax = plt.subplots(figsize=(10, 10))
        sns.heatmap(confusion_matrix(self.y_test, y_pred), ax=ax, annot=True, fmt='d')
        ax.set(xlabel='Predicted', ylabel='Truth')
        return plt.show()
    
    
    def cross_evaluation(self, cv_int):
        scores_tfidf = cross_validate(self.model, self.x_train, self.y_train, cv=cv_int,
                              return_train_score=True,
                              return_estimator=False)
        mean_train = round(scores_tfidf['train_score'].mean(),3)
        mean_test = round(scores_tfidf['test_score'].mean(),3)
        if abs(mean_train - mean_test) > 0.05:
            return print('Overfitting',',','mean_train_score:',mean_train,',',
                 'mean_test_score:',mean_test)
        else:
            return print('Not Overfitting',',','mean_train_score:',mean_train,',',
                 'mean_test_score:',mean_test)
    
    
    def plot_feature_importances(self):
        importances = pd.Series(data=self.model.feature_importances_, index= self.x_train.columns)
        # Sort importances
        importances = importances.sort_values(ascending=False)
        # Draw a horizontal barplot of importances_sorted
        return importances
    
    
    def generate_predictions(self):
        vectors = pca_apply(self.validation_data)
        self.validation_data_short = pd.concat([self.validation_data.loc[:,'loudness':'duration'],vectors],axis=1)
        #self.model.fit(self.x_train, self.y_train)
        return self.model.predict(self.validation_data_short)
    
    
    def save_model(self, filename):
        pkl_filename = filename
        with open(pkl_filename, 'wb') as file: 
            return pickle.dump(self.model, file)