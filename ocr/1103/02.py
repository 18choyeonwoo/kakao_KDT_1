import requests
import json


def ocr_space_api(image_path, api_key='K86149005188957', language='kor'):
    url_api = "https://api.ocr.space/parse/image"


    with open(image_path, 'rb') as f:
        response = requests.post(
            url_api,
            files={"filename": f},
            data={"apikey": api_key, "language": language},
            timeout=30
        )


    # HTTP 상태 확인
    try:
        response.raise_for_status()
    except requests.HTTPError:
        print("HTTP error:", response.status_code)
        print(response.text)
        return None


    # JSON으로 파싱
    try:
        result = response.json()
    except ValueError:
        print("응답이 JSON이 아님:", response.text)
        return None


    # 에러 여부 검사
    if result.get("IsErroredOnProcessing"):
        print("OCR 처리 에러:", result.get("ErrorMessage") or result.get("ErrorDetails"))
        return None


    parsed = result.get("ParsedResults")
    if not parsed:
        print("ParsedResults 없음 - 응답:", result)
        return None


    text_detected = parsed[0].get("ParsedText", "")
    return text_detected


text_result = ocr_space_api('01.jpg')
with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(text_result)
print("API로부터 추출된 텍스트:")
print(text_result)