# pip install -U "numpy<=1.26.4" "torch<=2.5.1" "torchvision<=0.20.1" "easyocr<=1.7.2"
# "pillow<=10.4.0" deepl streamlit
import easyocr

from step_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.

path = IN_DIR / "ocr.jpg"
reader = easyocr.Reader(["ko", "en"], verbose=False)
parsed = reader.readtext(path.read_bytes())
print(parsed)