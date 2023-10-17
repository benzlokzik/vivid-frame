import cv2
import numpy as np


def create_video_from_image(image_path, video_path, duration=5, inverted_duration=0.5):
    img = cv2.imread(image_path)
    inverted_img = 255 - img

    height, width, layers = img.shape
    size = (width, height)
    fps = 30

    normal_frames = int(fps * (duration - inverted_duration))
    inverted_frames = int(fps * inverted_duration)

    out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

    for i in range(normal_frames):
        out.write(img)

    for i in range(inverted_frames):
        out.write(inverted_img)

    out.release()
