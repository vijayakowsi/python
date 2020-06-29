from flask import Flask, send_file, request
from PIL import Image

app=Flask(__name__)

@app.route('/processimage', methods=['POST'])
def processimage():
	f = request.files['file']
	im = Image.open(f)
	im.save("images/output.png")

	return send_file("images/output.png", mimetype='image/png')


	

if __name__ == '__main__':  
    app.run(debug = True)  

