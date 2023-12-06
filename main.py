
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import pose


app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return 'Hello word'

@app.route('/api', methods=['POST'])
def api_endpoint():
    print('request : ' + str(request))
    data = request.json
    if data is None:
        return 'Invalid JSON data'

    print('api data : ' + str(data))

    #dir_path = data['dir_path']
    dir_path = '../../poketAi_workspace/allaboutu_springboot/src/main/resources/style_upload/'
    image_path = dir_path + data['image_path']
    org_path = data['org_path']
    img_path = data['image_path']
    arr = img_path.split(".")
    renameFileName2 = arr[0] + "_form." + arr[1]
    print("renameFileName2 : " + renameFileName2)


    change_path = dir_path + renameFileName2
    print('dir_path : ' + dir_path)
    print('org_path : ' + org_path)
    print('img_path : ' + img_path)
    print('renameFileName2 : ' + renameFileName2)
    print('image_path : ' + image_path)
    print('change_path : ' + change_path)
    pose.playMoveNet(image_path, change_path)

    params = {
        'org_path': org_path,
        'image_path' : img_path,
        'change_path' : renameFileName2,
        #'type' : type
        #'indexed_keypoints' : indexed_keypoints
    }

    return jsonify(params)

if __name__ == '__main__':
    app.run(host='localhost', port=4444)

    # dir_path = '../../poketAi_workspace/allaboutu_springboot/src/main/resources/style_upload/'  # data['dir_path']
    # image_path = dir_path + '20231206124745.jpg'
    # change_path = dir_path + '20231206124745_form.jpg'
    #
    # playMoveNet(image_path, change_path)



