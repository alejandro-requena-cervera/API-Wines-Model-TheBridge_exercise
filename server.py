import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine, MetaData
import json
import pickle


app = Flask(__name__)

# importo las credenciales de la base de datos
with open('./templates/config.json', 'r') as file:
    config = json.load(file)
    db_config = config['db_conn']
# creo la estructura de la url con las credenciales de la base de datos
url = f"postgresql://{db_config['user']}:{db_config['passw']}@{db_config['host']}:{db_config['port']}"
# llamo a la base de datos ya creada
engine = create_engine(url)
# "leo" la tabla de la base de datos como DataFrame
df_wines = pd.read_sql_table('wines', con=engine)
# Leo las tablas en la bases de datos
def list_databases(delete_table=None):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    if delete_table == None:
        list_databases = list(metadata.tables)
        return list_databases
    else:
        delete_database = metadata.tables[delete_table]
        return delete_database
# cargo el modelo
with open('./models/wines_model.plk', 'rb') as archive:
    model = pickle.load(archive)
# defino el target
target_dict = {
    0: 'Merlot',    # Class_0
    1: 'Chardonnay',    # Class_1
    2: 'Syrah'  # Class_2
}


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/api/v0/get_predict', methods=['GET'])
def get_predict_v0():
    alcohol = request.args.get('alcohol', None)
    malic_acid = request.args.get('malic_acid', None)
    ash = request.args.get('ash', None)
    alcalinity_of_ash = request.args.get('alcalinity_of_ash', None)

    samples = [alcohol, malic_acid, ash, alcalinity_of_ash]

    if None in samples:
        return render_template('error404.html')

    array = np.array(samples).astype(float).reshape(1, -1)
    prediction = model.predict(array)

    df_samples = pd.DataFrame(array, columns=df_wines.columns[:-1])
    df_samples['prediction'] = prediction
    df_samples.to_sql('samples', con=engine, if_exists='append', index=False)

    response = '<div style="color:maroon"><u>Type Of Wine:</u></div><br>'
    result = f'<div style="color:maroon;font-size:27">{target_dict[int(prediction)]}</div>'

    return response + result


@app.route('/api/v1/get_predict', methods=['GET', 'POST'])
def get_predict_v1():
    if request.method == 'POST':
        alcohol = float(request.form['alcohol'])
        malic_acid = float(request.form['malic_acid'])
        ash = float(request.form['ash'])
        alcalinity_of_ash = float(request.form['alcalinity_of_ash'])

        samples = [alcohol, malic_acid, ash, alcalinity_of_ash]

        array = np.array(samples).reshape(1, -1)
        prediction = model.predict(array)

        df_samples = pd.DataFrame(array, columns=df_wines.columns[:-1])
        df_samples['prediction'] = prediction
        df_samples.to_sql('samples', con=engine, if_exists='append', index=False)
        return render_template('predictions.html', 
                               inp=samples,
                               pred=target_dict[int(prediction)])

    return render_template('predictions.html')


@app.route('/api/v0/get_database', methods=['GET', 'POST'])
def get_database_v0():
    if request.method == 'POST':
        name_datab = request.form['datab']

        if name_datab not in list_databases():
            return render_template('error404.html')

        dict_datab = pd.read_sql_table(name_datab, con=engine).to_dict('records')
        return jsonify(dict_datab)
    
    return render_template('database.html', list_databases=list_databases())


@app.route('/api/v1/get_database', methods=['GET', 'POST'])
def get_database_v1():
    if request.method == 'POST':
        name_datab = request.form['datab']

        if name_datab not in list_databases():
            return render_template('error404.html')

        dict_datab = pd.read_sql_table(name_datab, con=engine).to_dict('records')
        return render_template('database_v1.html', 
                               list_databases=list_databases(),
                               dict_datab=dict_datab,
                               name_datab=name_datab)
    
    return render_template('database_v1.html', list_databases=list_databases())


@app.route('/api/v0/delete_database', methods=['GET', 'POST'])
def delete_database():
    if request.method == 'POST':
        name_datab = request.form.get('delete', None)
        confirmation = request.form.get('confirm', None)

        if (name_datab not in list_databases()) or (name_datab == 'wines'):
            return render_template('error404.html')
        
        if confirmation == name_datab:
            delete_datab = list_databases(delete_table=name_datab)
            delete_datab.drop(bind=engine)

        return render_template('delete_database.html', 
                               list_databases=list_databases(),
                               name_datab=name_datab,
                               confirmation=confirmation)
    
    return render_template('delete_database.html', list_databases=list_databases())
    



if __name__ == '__main__':
    app.run(debug=True)
