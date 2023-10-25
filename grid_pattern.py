#!/usr/bin/env python
from PIL import Image

original_image_filename = 'pattern.png'

output_image_filename = 'grid_pattern.jpg'

with Image.open(original_image_filename) as original_image:
    # Create horizontally and vertically flipped images
    horizontal_flipped = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    vertical_flipped = original_image.transpose(Image.FLIP_TOP_BOTTOM)
    both_flipped = original_image.transpose(
        Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)

    grid_image = Image.new(
        'RGB', (2 * original_image.width, 2 * original_image.height))

    # Paste the images into the grid
    grid_image.paste(original_image, (0, 0))
    grid_image.paste(horizontal_flipped, (original_image.width, 0))
    grid_image.paste(vertical_flipped, (0, original_image.height))
    grid_image.paste(
        both_flipped, (original_image.width, original_image.height))

    grid_image.save(output_image_filename)
