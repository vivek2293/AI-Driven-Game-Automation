# Screen capture
from mss import mss
from PIL import Image

# x=81, y=32
# x=1343, y=744

# System 1 
region = {'left': 80, 'top': 32, 'width': 950, 'height': 531}
# System 2
# region = {'left': 0, 'top': 0, 'width': 950, 'height': 566}

# Get Screenshot
with mss() as sct:
    screenshot = sct.grab(region)
    img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
    img.show()