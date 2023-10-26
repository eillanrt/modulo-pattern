# Instructions for Image Generation and Grid Formation

Follow these steps to generate a pattern image and, optionally, create a 2x2 grid of the pattern:

## 1. Prepare Image Files

Place five images in the `pics` folder with the following filenames: `1.png`, `2.png`, `3.png`, `4.png`, and `5.png`. Ensure that all images are in the .png format. If you have images in different formats, you can modify the `main.py` file to handle those formats.

## 2. Generate the Pattern Image

In your terminal, run the following command to generate the pattern image:

```bash
$ ./main.py
```

Alternatively, you can use `python` if the previous command doesn't work:

```bash
$ python main.py
```

This will create a file named `pattern.png` in your current working directory.

## 3. Create a 2x2 Grid (Optional)

If desired, you can create a 2x2 grid of the pattern, with the other cells of the grid mirroring the base pattern from left to right and top to bottom. To do this, execute the following command:

```bash
$ ./grid_pattern.py
```

Or, using `python`:

```bash
$ python grid_pattern.py
```

This will generate a grid pattern containing the base image and three mirrored versions of it.

Following these instructions will provide you with a pattern image and, optionally, a 2x2 grid of the pattern. Please note the limitations mentioned below.

## Limitations
The 2x2 grid of images exhibits mirror symmetries in different directions. Starting with Quadrant II as the fundamental pattern, Quadrant I mirrors this pattern horizontally. Quadrant III mirrors Quadrant I vertically, and Quadrant IV mirrors Quadrant III both horizontally and vertically. In this way, they create a symmetrical set of patterns on a Cartesian plane.
