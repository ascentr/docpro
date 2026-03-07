import os
import math
from decimal import Decimal
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image, ImageDraw, ImageOps, ImageFont


def dms_to_decimal(dms, ref):
  deg, min_, sec = dms
  decimal = float(deg) + (float(min_) / 60) + (float(sec) / 3600)
  if ref in ('S', 'W'):
      decimal = -decimal
  return decimal


def get_gps_from_image(image_path):
  img = Image.open(image_path)
  exif = img._getexif()

  if not exif:
    return None, None

  # Decode EXIF
  exif_data = {
    TAGS.get(tag, tag): value
    for tag, value in exif.items()
  }

  gps_data = exif_data.get("GPSInfo")

  if not gps_data:
    return None, None

  # Decode GPSTAGS
  gps_info = {
    GPSTAGS.get(k, k): v
      for k, v in gps_data.items()
    }
    
  if "GPSLatitude" not in gps_info or "GPSLongitude" not in gps_info:
      return None, None  
  
  lat = dms_to_decimal(
    gps_info["GPSLatitude"],
    gps_info["GPSLatitudeRef"]
  )

  lon = dms_to_decimal(
    gps_info["GPSLongitude"],
    gps_info["GPSLongitudeRef"]
  )
  
  print("latitude & longitude in utils",lat, lon)
  return lat, lon


# load orignal image, get gps data, resize for A4, and print project data etc

def process_image(image_path, project, room_type, lat, lon):
  A4 = (1240, 1754) #150dpi
  img = Image.open(image_path)
  img = ImageOps.exif_transpose(img)
  img.thumbnail(A4, Image.LANCZOS)


  draw = ImageDraw.Draw(img)
  shape = [(0, 0), (370, 120)]
  draw.rectangle(shape, fill="#fff", outline="#0a2d12")

  draw = ImageDraw.Draw(img)
  
  # myfont = ImageFont.truetype("./static/fonts/calibri.ttf", 20)
  font = ImageFont.load_default()
  text = (
    f'Project : {project} \n'
    f'Room : {room_type} \n'
    f'Lat / Lan : {lat} \ {lon}'
  )
  
  draw.text((30, 30), text, fill="black", font=font)
  img.save(image_path, quality=90)
  


def resize_image(image_path):
  original_image = Image.open(image_path)
  original_image = ImageOps.exif_transpose(original_image)
  img_resized = original_image.copy()
  A4 = (1240, 1754) #150dpi


  # project_name = "Vokera Boiler Pipe"
  # room_type = "Loft Bedroom"

# # A4 = (2480, 3508) #300dpi
# A4 = (1240, 1754) #150dpi

# img_resized.thumbnail(A4, Image.LANCZOS)
# # Rectangle

# draw = ImageDraw.Draw(img_resized)
# shape = [(0, 0), (370, 120)]
# draw.rectangle(shape, fill="#fff", outline="#0a2d12")

# # Font
# myfont = ImageFont.truetype("./static/fonts/calibri.ttf", 25)
# text_string = str(project_name) +'\n'+ str(room_type)+ '\n'+ f'Lat:{lat}, Lon: {lon}'

# # Text
# draw.text((25, 25), text_string, fill="#000", font=myfont)

# # Save
# img_resized.save("loft01_20260128_edited.jpg")