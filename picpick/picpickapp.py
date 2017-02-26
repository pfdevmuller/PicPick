from flask import Flask
import json

app = Flask(__name__)
image_collection = None

def set_image_collection(collection):
    global image_collection
    image_collection = collection


@app.route('/TestProject/Pics/<filename>')
def get_picture(filename):
    return "Hello tester!"


@app.route('/TestProject/Pics')
def get_picture_list():
    return json.dumps(image_collection.pictures)

#app.run(debug=True)
