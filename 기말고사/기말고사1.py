from pathlib import Path

import streamlit as st

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_3 import OUT_2_3, read_text_and_draw_line, read_text_from_image
from liv_helper import translate_libre

st.title("✌ 인식률 체크 문자 인식 웹 앱")  # 웹 앱 제목

uploaded = st.file_uploader("인식할 이미지를 선택하세요.")  # 파일 업로더 위젯
if uploaded is not None:  # 파일이 업로드되면, 다음 코드를 실행
    tmp_path = OUT_DIR / f"{Path(__file__).stem}.tmp"  # 임시 파일 경로
    tmp_path.write_bytes(uploaded.getvalue())  # 업로드한 이미지 저장

    col_left, col_right = st.columns(2)  # 두 개의 열 생성
    with col_left:  # 첫 번째 열
        st.subheader("원본 이미지")  # 부제목
        st.image(tmp_path.as_posix())  # 원본 이미지 출력
    with col_right:  # 두 번째 열
        st.subheader("문자 인식 결과")  # 부제목
        with st.spinner(text="문자를 인식하는 중입니다..."):  # 진행 상황 표시
            read_text_and_draw_line(tmp_path)  # 문자 인식 및 박스 그리기
        st.image(OUT_2_3.as_posix())  # 결과 이미지 출력

    st.subheader("📝 인식된 텍스트 및 번역 결과")
    with st.spinner("텍스트를 번역하는 중입니다..."):
        texts = read_text_from_image(tmp_path)
        if texts:
            # for text in texts:
            #     translated = translate_libre(text, source="en", target="ko")  # 필요에 따라 source/target 변경
            #     st.markdown(f"**🔹 {text}**<br/>➡️ {translated}", unsafe_allow_html=True)

            full_text = " ".join(texts)  # 모든 인식된 텍스트를 공백으로 합침
            translated = translate_libre(full_text, source="en", target="ko")
            st.markdown(f"**🔹 {full_text}**<br/>➡️ {translated}", unsafe_allow_html=True)
        else:
            st.info("문자를 인식하지 못했습니다.")









# from pathlib import Path

# from PIL import Image, ImageDraw, ImageFont

# from step_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
# from step_3_2 import read_text_translated

# OUT_3_3 = OUT_DIR / f"{Path(file).stem}.jpg"
# PROB = 0.75


# def read_text_and_fill_area(path: Path):
#     parsed = read_text_translated(path)  # 문자 인식 및 번역 결과 저장
#     img = Image.open(path)
#     draw = ImageDraw.Draw(img, "RGBA")  # 알파 채널 사용 가능
#     font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", size=60)
#     for row in parsed:
#         bbox, text, prob = row
#         box = [(x, y) for x, y in bbox]
#         draw.polygon(
#             box,
#             fill=(255, 0, 0, 100) if prob >= PROB else (0, 255, 0, 100),
#         )
#         draw.text(xy=box[0], text=text, fill=(255, 255, 255), font=font)
#     img.save(OUT_3_3)


# if name == "main":
#     path = IN_DIR / "ocr.jpg"
#     read_text_and_fill_area(path)






# from pathlib import Path

# from PIL import Image, ImageDraw, ImageFont

# from step_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
# from step_2_2 import read_text

# OUT_X = OUT_DIR / f"{Path(file).stem}.jpg"
# PROB = 0.75  # 인식률 기준값


# def read_text_and_draw_line(path: Path):
#     parsed = read_text(path)  # 문자 인식 결과 저장
#     img = Image.open(path)  # 이미지 객체 생성
#     draw = ImageDraw.Draw(img, "RGBA")  # 이미지드로 객체 생성
#     font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", size=50)
#     for row in parsed:
#         bbox, text, prob = row  # 문자 인식 결과를 좌표, 문자, 인식률로 각각 분리
#         box = [(x, y) for x, y in bbox]  # 리스트를 튜플로 변환
#         draw.polygon(
#             box,
#             outline=(255, 0, 0) if prob >= PROB else (0, 255, 0),
#             width=10,
#         )

#         start_x, start_y = box[0]  # 문자열을 그릴 시작점
#         left, top, right, bottom = font.getbbox(text)  # text 문자열의 바운딩 박스
#         text_width = right  # 문자열 너비
#         text_height = bottom  # 문자열 높이

#         pad = 10  # 여백
#         bg_width = pad + text_width + pad  # 배경 너비
#         bg_height = pad + text_height + pad  # 배경 높이

#         draw.rectangle(  # 배경 이미지 그리기
#             xy=(
#                 start_x,
#                 start_y,
#                 start_x + bg_width,  # 시작점부터 배경 너비만큼
#                 start_y + bg_height,  # 시작점부터 배경 높이만큼
#             ),
#             fill=(0, 0, 0, 200),  # 검정색 (0, 0, 0)에 불투명도 적용
#         )

#         draw.text(  # 문자열 그리기
#             xy=(
#                 start_x + pad,  # 시작점에서 여백만큼 떨어져서
#                 start_y + pad,
#             ),
#             text=text,
#             fill=(255, 255, 255),
#             font=font,
#         )
#     img.save(OUT_X)


# if name == "main":
#     path = IN_DIR / "ocr.jpg"
#     read_text_and_draw_line(path)