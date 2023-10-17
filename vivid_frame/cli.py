import argparse
from .image_to_video import create_video_from_image


def main():
    parser = argparse.ArgumentParser(
        description="Convert an image to a video with inverted colors at the end."
    )

    parser.add_argument("image_path", type=str, help="Path to the input image")
    parser.add_argument("video_path", type=str, help="Path to save the output video")
    parser.add_argument(
        "--duration",
        type=float,
        default=5,
        help="Total duration of the video in seconds",
    )
    parser.add_argument(
        "--inverted_duration",
        type=float,
        default=0.5,
        help="Duration of the inverted colors in seconds",
    )

    args = parser.parse_args()

    create_video_from_image(
        args.image_path, args.video_path, args.duration, args.inverted_duration
    )
