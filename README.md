# vivid-frame

Convert static images to dynamic videos with a vivid twist at the end – an inverted color frame.

## Installation

### Using Poetry (recommended)

1. Clone the repository:
    ```bash
    git clone https://github.com/benzlokzik/vivid-frame.git
    cd vivid-frame
    ```

2. Install the dependencies using [Poetry](https://python-poetry.org/):
    ```bash
    poetry install
    ```

### Without Poetry

Make sure you have the required dependencies installed:

- [OpenCV for Python](https://pypi.org/project/opencv-python/)

```bash
pip install opencv-python numpy
```

## Usage

From the command line:

```bash
poetry run python -m vivid_frame <path_to_image.jpg> <output_video.avi> --duration 5 --inverted_duration 0.5
```

- `<path_to_image.jpg>`: Replace with the path to your input image.
- `<output_video.avi>`: Replace with the path where you want to save the video.
- `--duration`: Total duration of the video in seconds (optional, default is 5 seconds).
- `--inverted_duration`: Duration of the inverted colors at the end of the video in seconds (optional, default is 0.5
  seconds).

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

