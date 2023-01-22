from flask import Flask, jsonify, request
from utils import all, one

app = Flask(__name__)

@app.get('/movie/<title>')
def index(title: str):
   querry =  f"""
   SELECT * FROM netflix
   WHERE title = '{title}'
   ORDER BY date_added desc
   """
   querry_result = one(querry)

   if querry_result is None:
      return jsonify(status = 404)

   film =  {
      'title': querry_result['title'],
      'country': querry_result['country'],
      'release_year': querry_result['release_year'],
      'genre': querry_result['listed_in'],
      'description': querry_result['description']
   }
   return jsonify(film)

@app.get('/movie/<year1>/to/<year2>')
def index_1(year1: str, year2: str):
   querry =  f"""
   SELECT * FROM netflix
   WHERE release_year BETWEEN 
   '{year1}' and '{year2}'
   ORDER BY date_added desc
   LIMIT 100
   """
   result = []
   for i in all(querry):
      result.append(
         {  'title': i['title'],
          'release_year': i['release_year']}
      )

   return jsonify(result)

@app.get('/movie/<year1>/to/<year2>')
def index_1(year1: str, year2: str):
   querry =  f"""
   SELECT * FROM netflix
   WHERE release_year BETWEEN 
   '{year1}' and '{year2}'
   ORDER BY date_added desc
   LIMIT 100
   """



app.run(debug=True)