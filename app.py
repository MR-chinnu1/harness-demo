from flask import Flask
app= Flash(__name__)
@app.route('/')
def hello():
  return "Hello, world from Harness demo!"
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
