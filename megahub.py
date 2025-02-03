import ctypes
from ctypes import wintypes
import os
import sys

class MegaHub:
    def __init__(self):
        self.user32 = ctypes.WinDLL('user32', use_last_error=True)
        self.kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        
    def change_wallpaper(self, wallpaper_path):
        SPI_SETDESKWALLPAPER = 20
        if not os.path.exists(wallpaper_path):
            print("Wallpaper file does not exist.")
            return
        
        result = self.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 3)
        if not result:
            print("Failed to change wallpaper.")
        else:
            print("Wallpaper changed successfully.")
    
    def adjust_window_transparency(self, hwnd, transparency_level):
        # transparency_level: 0 (fully transparent) to 255 (opaque)
        extended_style = self.user32.GetWindowLongW(hwnd, -20)
        self.user32.SetWindowLongW(hwnd, -20, extended_style | 0x80000)
        self.user32.SetLayeredWindowAttributes(hwnd, 0, transparency_level, 2)
        print(f"Set window transparency to {transparency_level}.")
    
    def list_open_windows(self):
        def foreach_window(hwnd, lParam):
            if self.user32.IsWindowVisible(hwnd):
                length = self.user32.GetWindowTextLengthW(hwnd)
                title = ctypes.create_unicode_buffer(length + 1)
                self.user32.GetWindowTextW(hwnd, title, length + 1)
                print(f"Window handle: {hwnd}, Title: {title.value}")
            return True

        EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
        enum_windows = EnumWindowsProc(foreach_window)
        self.user32.EnumWindows(enum_windows, 0)
    
    def run(self):
        print("Welcome to MegaHub!")
        while True:
            print("\nOptions:")
            print("1. Change Wallpaper")
            print("2. Adjust Window Transparency")
            print("3. List Open Windows")
            print("4. Exit")
            
            choice = input("Select an option: ")
            if choice == '1':
                path = input("Enter the path to the wallpaper image: ")
                self.change_wallpaper(path)
            elif choice == '2':
                hwnd = int(input("Enter window handle (HWND): "), 16)  # handle in hex
                level = int(input("Enter transparency level (0-255): "))
                self.adjust_window_transparency(hwnd, level)
            elif choice == '3':
                self.list_open_windows()
            elif choice == '4':
                print("Exiting MegaHub.")
                sys.exit(0)
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    MegaHub().run()