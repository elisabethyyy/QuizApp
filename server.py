from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")
    
@app.route('/about')
def about():
  return render_template ("about.html")

@app.route('/test',methods = ['POST', 'GET'])
def test():
  parametri = ["IQ","Augums","Kājas izmērs"]
  images = ["https://static.wikia.nocookie.net/harrypotter/images/0/04/Niffler_2.png/revision/latest?cb=20161203143220&path-prefix=ru","data:image/jpeg;base64,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","https://i.pinimg.com/736x/16/cb/a0/16cba09b4902d30a0463c36f8f42dd8c.jpg"]
  return render_template("test.html",parametri=parametri,images=images)

#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run(debug="true")

