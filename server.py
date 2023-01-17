import flask
import werkzeug
import time
import os


app = flask.Flask(__name__)


UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'],timestr+'_'+filename))
        image_num = image_num + 1
    print("\n")
    return "Image Uploaded Successfully. Waiting for the result...."

app.run(host="0.0.0.0", port=8000, debug=True)
# app.run(host="127.0.0.1",port=3000,debug=True)
# app.run(host="10.0.2.2",port=3000,debug=True)



# if __name__ == "__main__":
#     app.run(host = '0.0.0.0' port=5000, debug=True)