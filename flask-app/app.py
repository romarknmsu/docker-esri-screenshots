from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/10JUly17.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/11Feb17.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/12Sept16.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/13Jun16.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/14Nov15.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/15Dec14.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/16July14.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/1June19.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/2Feb19.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/3.GIF",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/4Sept18.GIF",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/5.JPG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/6Sept18.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/7.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/8.PNG",
	"https://imageryapps.s3.us-west-1.amazonaws.com/media/screenshots/imagery/9Nov17.PNG"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")