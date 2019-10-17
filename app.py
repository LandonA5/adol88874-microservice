from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return 'Service is alive'

@app.route('/1', methods=['GET', 'POST'])
def post1(userNum):
   if request.method == 'POST':
       return userNum
   else:
       return 'You should POST to this URL'

if __name__ == "__main__":
    app.run(host="0.0.0.0")


