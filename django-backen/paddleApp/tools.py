import os
from paddleocr import PaddleOCR, draw_ocr
import base64

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # need to run only once to download and load model into memory

def ocr_detect(filePath: str):
  '''
   orc识别
  '''
  print("filePath is ", filePath)
  result = ocr.ocr(filePath, cls=True)
  result_list = result
  (path, fileName) = os.path.split(filePath)

  return result_list, os.path.join(path, "draw-" + fileName)


def handle_upload_file(f):
  file_name = f.name
  if (not os.path.exists(os.path.join(BASE_DIR, 'template/media-img'))):
    # 判断文件夹路径是否存在，不存在则创建
    os.makedirs(os.path.join(BASE_DIR, 'template/media-img'))
  with open(os.path.join(BASE_DIR, 'template/media-img', file_name), 'wb') as f_write:
    for chunk in f.chunks():
      f_write.write(chunk)
  f_write.close()
  base64_data = base64.b64encode(f.open(mode='rb').read()).decode('utf-8')
  f.close()
  result_json, deteced_filePath = ocr_detect(os.path.join(BASE_DIR, 'template/media-img', file_name))

  return result_json, deteced_filePath, os.path.join(BASE_DIR, 'template/media-img', file_name), base64_data
