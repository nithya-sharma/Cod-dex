import os
import imageio

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Use absolute paths for image files
filenames = [
    r'E:\PLACEMENTS\Python\CreateaGIF\sunflower1.jpeg',
    r'E:\PLACEMENTS\Python\CreateaGIF\sunflower2.jpg'
]

# Check if files exist
for filename in filenames:
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")

# Read and append images
images = []
for filename in filenames:
    images.append(imageio.imread(filename))

# Create GIF
output_path = r'E:\PLACEMENTS\Python\CreateaGIF\sunflower.gif'
imageio.mimsave(output_path, images, duration=0.5, loop=0)

print(f"GIF created successfully at {output_path}")
