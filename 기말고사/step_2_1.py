import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import easyocr

from step_1 import IN_DIR

path = IN_DIR / "ocr.jpg"
reader = easyocr.Reader(["ko", "en"], verbose=False)
parsed = reader.readtext(path.read_bytes())
print(parsed)