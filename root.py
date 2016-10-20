from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
  pictures = ['samsung','sony','lg','nokia','motorola','bq','iphone','xiaomi']
  return render_template('hello.html', pictures = pictures)

@app.route('/samsung')
def samsung():
  return render_template('samsung.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
