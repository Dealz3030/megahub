# MegaHub

MegaHub is a Python application designed to customize and enhance the Windows graphical user interface for improved usability. With MegaHub, users can change their desktop wallpaper, adjust the transparency of windows, and list all open windows.

## Features

- **Change Wallpaper**: Easily change your desktop wallpaper by providing the path to an image file.
- **Adjust Window Transparency**: Set the transparency level of windows to achieve a personalized desktop experience.
- **List Open Windows**: View all currently open windows on your system with their handles and titles.

## Requirements

- Windows operating system
- Python 3.x
- Administrative privileges may be required for some features

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/megahub.git
    ```

2. Navigate into the project directory:

    ```bash
    cd megahub
    ```

3. Run the application:

    ```bash
    python megahub.py
    ```

## Usage

1. Upon running the application, you will be greeted with a menu of options.
2. Select an option by entering the corresponding number.
3. Follow the prompts to complete your selection.

## Notes

- Ensure that the image path provided for changing the wallpaper is correct and the file exists.
- Window handles (HWND) can be obtained by listing open windows using the provided option.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Acknowledgements

- This project utilizes the Windows API via the `ctypes` module in Python.