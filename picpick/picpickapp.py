from flask import Flask

app = Flask(__name__)

@app.route('/TestProject/Pics/<filename>')
def get_picture(filename):
    return "Hello tester!"

#app.run(debug=True)
