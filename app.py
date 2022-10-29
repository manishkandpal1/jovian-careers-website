from flask import Flask , render_template,jsonify
# created a flask application
app=Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary':'Rs. 12,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]
# route
@app.route("/")
def hello_jovian():
  return render_template('home.html',jobs=JOBS,company_name='Jovian Tutorials & ')
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
 # print("I'm inisde the if now")