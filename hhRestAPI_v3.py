from flask import Flask, request, jsonify
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import base64
from io import BytesIO

app = Flask(__name__)

#def funcPythonString():
#    return "Hello World IronPython"

def funcImageClassify(encoded_data):    
    decoded_data=base64.b64decode((encoded_data))   # decode base64 string data
    image = Image.open(BytesIO(decoded_data))       # Load image from BytesIO
    model = load_model('assets/keras_model_epoch_300.h5')  # Load the model    
    #image.show()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Resize the image to a 224x224 with the same strategy as in TM2:
    # Resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # Turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    print(prediction[0])
    if prediction[0][0] > prediction[0][1]:
        result = 'Non-Fire:' + str(round(prediction[0][0],2))
    else:
        result = 'Fire:' + str(round(prediction[0][1],2))
    
    return result
    

@app.route('/imageClassify', methods = ['POST'])        # POST 방식 (HTTP Body에 데이터를 추가하여 요청하는 방식) (Source: https://rekt77.tistory.com/104?category=825845)
def imageClassify():
     if request.get_json() is not None:
        image = request.get_json().get("ImageUri")
        if not image:
            return jsonify({"image":"None"})
        else:            
            result = funcImageClassify(image).split(':')
            return jsonify({"type":result[0], "conf":result[1]})            
 
if __name__ == "__main__":
    app.run(debug=False, port=8086, host='0.0.0.0')



