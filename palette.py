from PIL import Image
import numpy as np

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def get_dominant_colors(image, num_colors=5):
    image = image.convert('RGB')
    image_array = np.array(image)
    rgb_values, counts = np.unique(image_array.reshape(-1, 3), axis=0, return_counts=True)
    sorted_indices = np.argsort(counts)[::-1]
    sorted_rgb_values = rgb_values[sorted_indices]
    dominant_colors = sorted_rgb_values[:num_colors]
    hex_colors = [rgb_to_hex(tuple(color)) for color in dominant_colors]
    return hex_colors