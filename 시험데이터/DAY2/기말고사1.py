import streamlit as st
import easyocr
import requests
import tempfile
from PIL import Image

# MyMemory API를 이용한 번역 함수
def translate_mymemory(text, source="en", target="ko"):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source}|{target}"
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data["responseData"]["translatedText"]
        else:
            return "번역 실패"
    except Exception as e:
        return f"번역 오류: {e}"

# easyocr로 이미지에서 텍스트 추출
def read_text_from_image(image_path, lang_list=['en', 'ko']):
    reader = easyocr.Reader(lang_list, gpu=False)
    results = reader.readtext(image_path)
    texts = [result[1] for result in results]
    return "\n".join(texts)

st.title("이미지 텍스트 인식 및 번역 (easyocr + MyMemory API)")

uploaded = st.file_uploader("이미지 파일을 업로드하세요.", type=["png", "jpg", "jpeg"])

if uploaded is not None:
    # 임시 파일로 저장
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        tmp_file.write(uploaded.read())
        tmp_path = tmp_file.name

    # 이미지 표시
    st.image(Image.open(tmp_path), caption="업로드한 이미지", use_column_width=True)

    # 텍스트 추출
    with st.spinner("이미지에서 텍스트 추출 중..."):
        extracted_text = read_text_from_image(tmp_path)
    st.subheader("인식된 텍스트")
    st.write(extracted_text if extracted_text else "텍스트를 인식하지 못했습니다.")

    # 번역
    if extracted_text:
        with st.spinner("번역 중..."):
            translated = translate_mymemory(extracted_text, source="en", target="ko")
        st.subheader("번역 결과")
        st.write(translated)