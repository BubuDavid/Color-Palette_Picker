# Import important imports
from models.color_picker import get_palette
from flask import Flask, render_template, request, session, redirect
from urllib.request import urlretrieve
import os

app = Flask(__name__)
app.secret_key = 'Bubu Bad Secret Key'
app.jinja_env.filters['zip'] = zip

@app.route('/')
def index_method():
    return render_template("index.html")

@app.route('/image-process', methods=['POST'])
def color_picker_method():

    # Grab the params
    image_url = request.form['image_url']
    n_colors  = int(request.form['n_colors'])
    # Downloading the image
    image_path = "static/images/image.jpg"
    # Delete the image if exists
    try:
        os.remove(image_path)
    except:
        pass
    urlretrieve(image_url, image_path)
    # Extract 6 colors from an image
    colors, distribution = get_palette(image_path, n_colors)

    # Store the parameters into session
    session['colors'] = colors
    session['distribution'] = distribution
    session['image_path'] = image_path 
    # Render our template
    return redirect("/image-view")

    return render_template('404.html')

@app.route('/image-view')
def image_method():
    # Grab variables from session
    colors = session.get('colors', [])
    distribution = session.get('distribution', [])
    image_path = session.get('image_path', '../static/images/kirby.png')

    # Store the colors and image_path in context
    context = {
        'colors': colors,
        'image_path': f"../{image_path}",
        'distribution': distribution,
    }

    return render_template("image_view.html", context=context)
        
if __name__ == '__main__':
    app.run(debug=True, port=8888)

    try:
        os.remove("static/images/image.jpg")
    except:
        pass
