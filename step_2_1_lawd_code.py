from datakart import Datagokr
import sys
from typing import List, Dict

DATAGO_KEY = "wr3cCX6Pccs2ok0G6l1OCgMtFnjyKAxWWDYXtB7PZJkTLQx5YH9fLFcTn1F0JV281Jw/NalBfCbkBhubCBJspw=="  # 공공데이터포털 API 키 입력
datago = Datagokr(DATAGO_KEY)  # Datagokr 객체 생성
resp = datago.lawd_code("서울특별시")  # 법정동 데이터 조회
print(resp)
print(sys.executable)

def get_symbols(excd: T_EXCD_SYMBOL, force_fetch: bool = False) -> List[Dict]:
    pass