from flask import Flask, render_template, request
import pandas as pd
from Modelevaluator import *
import pickle
from sqlalchemy import *
from sqlalchemy import create_engine

model = pickle.load(open("xgbclassifier.pkl",'rb'))
app = Flask(__name__)

engine = create_engine('sqlite:///pyakc.db', echo=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        data = pd.read_csv(file)
        #data.to_html(header="true", table_id="table")
        data_vec=pca_apply(data)
        x=pd.concat([data.loc[:,'loudness':'duration'], data_vec],axis=1)
        x['genre'] = model.predict(x)
        result=pd.concat([x['genre'], data['title']],axis=1)
        result.to_sql('genre', con=engine, if_exists='append')
        qry_table=pd.read_sql_query("SELECT * FROM genre", con=engine)
        return qry_table.to_html(header="true", table_id="table",if_exists='fail')
    


        
#https://morioh.com/p/20750b8a8580

if __name__ == '__main__':
    app.run(port = 1000, debug=True)
