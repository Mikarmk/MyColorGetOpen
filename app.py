from flask import Flask, render_template, request, jsonify
from PIL import Image
import colorsys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            image.save('static/img/' + image.filename)
            colors = get_dominant_colors('static/img/' + image.filename)
            return jsonify(colors)
    return render_template('index.html')

def get_dominant_colors(image_path):
    image = Image.open(image_path)
    image = image.resize((100, 100))
    image = image.convert('RGB')
    image_data = list(image.getdata())
    rgb_frequencies = {}
    for pixel in image_data:
        r, g, b = pixel
        rgb_key = (r, g, b)
        if rgb_key not in rgb_frequencies:
            rgb_frequencies[rgb_key] = 0
        rgb_frequencies[rgb_key] += 1
    sorted_rgb_frequencies = sorted(rgb_frequencies.items(), key=lambda x: x[1], reverse=True)
    dominant_colors = [rgb for rgb, freq in sorted_rgb_frequencies[:5]]
    hex_colors = [rgb_to_hex(rgb) for rgb in dominant_colors]
    rgb_colors = [rgb_to_rgb(rgb) for rgb in dominant_colors]
    return {'hex': hex_colors, 'rgb': rgb_colors}

def rgb_to_hex(rgb):
    r, g, b = rgb
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def rgb_to_rgb(rgb):
    r, g, b = rgb
    return [r, g, b]

if __name__ == '__main__':
    app.run(debug=True)