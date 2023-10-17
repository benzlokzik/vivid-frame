import cv2


def create_video_from_image(image_path, video_path, duration=5, inverted_duration=0.5):
    print(f"Reading image from {image_path}...")
    img = cv2.imread(image_path)
    inverted_img = 255 - img

    height, width, layers = img.shape
    size = (width, height)
    fps = 30

    normal_frames = int(fps * (duration - inverted_duration))
    inverted_frames = int(fps * inverted_duration)

    print("Creating video...")
    out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*"DIVX"), fps, size)

    print(f"Writing {normal_frames} normal frames to video...")
    for i in range(normal_frames):
        out.write(img)

    print(f"Writing {inverted_frames} inverted frames to video...")
    for i in range(inverted_frames):
        out.write(inverted_img)

    out.release()
    print(f"Video saved to {video_path}.")
