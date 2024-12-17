import cv2
import os

# Define the directory containing the images
image_folder = "OUTPUT_FINAL/walking_meshes"

# Define the output video file path
output_video = "OUTPUT_FINAL/walking_output.mp4"

# Define the frames per second (FPS) for the video
fps = 12

# Get a list of all image files in the folder, sorted by modification time (descending)
images = sorted(
    [img for img in os.listdir(image_folder) if img.lower().endswith(('.png', '.jpg', '.jpeg'))],
    key=lambda x: os.path.getmtime(os.path.join(image_folder, x)),
    reverse=False
)

# Check if there are images in the folder
if not images:
    print("No images found in the specified folder!")
    exit()

# Read the first image to get the frame size
first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path)
height, width, layers = frame.shape

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for .avi format
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Loop through the images and add them to the video
for image in images:
    image_path = os.path.join(image_folder, image)
    frame = cv2.imread(image_path)
    video.write(frame)
    print(f"Added {image} to video.")

# Release the video writer
video.release()
print(f"Video saved as {output_video}")
