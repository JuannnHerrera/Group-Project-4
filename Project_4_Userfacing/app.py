#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__, template_folder='my_templates')

# Load your dataset
df = pd.read_csv('cyber_crime_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    years = df['Year'].unique().tolist()
    crime_types = df['CrimeType'].unique().tolist()
    return jsonify({'years': years, 'crime_types': crime_types})

@app.route('/stats/<year>/<crime_type>')
def stats(year, crime_type):
    filtered_df = df[(df['Year'] == int(year)) & (df['CrimeType'] == crime_type)]
    data = filtered_df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
