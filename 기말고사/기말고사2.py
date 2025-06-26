import streamlit as st
import qrcode
from PIL import Image
import io

st.title("깃허브 QR코드 생성기")

# 깃허브 저장소 URL 입력
github_url = st.text_input("깃허브 저장소 URL을 입력하세요", "https://github.com/JungYunsu/py/tree/main/기말고사")

if github_url:
    # QR 코드 생성
    qr_img = qrcode.make(github_url)
    buf = io.BytesIO()
    qr_img.save(buf, format="PNG")
    st.image(Image.open(buf), caption="깃허브 QR코드", use_column_width=False)

    # QR코드 다운로드 버튼
    buf.seek(0)
    st.download_button(
        label="QR코드 이미지 다운로드",
        data=buf,
        file_name="github_qr.png",
        mime="image/png"
    )

# st.info("깃허브에 번역 프로그램을 올리고, 그 저장소 주소를 입력하면 QR코드가 생성됩니다.")