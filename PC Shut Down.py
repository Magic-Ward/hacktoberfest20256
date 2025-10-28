import os
import platform
import time

def auto_shutdown(delay_minutes=1):
    system = platform.system()
    seconds = delay_minutes * 60

    print(f"⚠️ Your computer will shut down in {delay_minutes} minute(s).")
    print("Press Ctrl + C to cancel.")
    time.sleep(seconds)

    try:
        if system == "Windows":
            os.system("shutdown /s /t 1")
        elif system == "Linux" or system == "Darwin":  # Darwin = macOS
            os.system("sudo shutdown -h now")
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
auto_shutdown(delay_minutes=0.1)  # shuts down in 6 seconds (for demo)
