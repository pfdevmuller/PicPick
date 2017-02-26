from flask import Flask

app = Flask(__name__)

@app.route('/TestProject/Pics/<filename>')
def get_picture(filename):
    return "Hello tester!"

@app.route('/TestProject/Pics')
def get_picture_list():
    return "<root><picture_list></picture_list></root>"

#app.run(debug=True)
