import requests
from requests.auth import HTTPDigestAuth
import urllib3
import os



def add_user(BASE_URL, USERNAME, PASSWORD, EMPLOYEE_NO, NAME, IMAGE_PATH):

    # Ogohlantirishlarni o‘chirib qo‘yamiz
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # 📌 Qurilma sozlamalari


    # 📌 Foydalanuvchi ma'lumotlari



    url = f"{BASE_URL}/ISAPI/AccessControl/UserInfo/Record?format=json"
    auth = HTTPDigestAuth(USERNAME, PASSWORD)

    payload = {
        "UserInfo": {
            "employeeNo": EMPLOYEE_NO,
            "name": NAME,
            "userType": "normal",
            "Valid": {
                "enable": True,
                "beginTime": "2025-05-01T00:00:00",
                "endTime": "2025-06-20T23:59:59"
            },
            "doorRight": "1",
            "RightPlan": [
                {
                    "doorNo": 1,
                    "planTemplateNo": "1"
                }
            ],
            "userVerifyMode": "face",
            "maxOpenDoorTime": 10,
            "userGroup": 1,
            "localUIRight": True,
            "userPassword": "123456",
            "passwordType": "normal",
            "openDoorType": {
                "doorType": "local"
            }
        }
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, auth=auth, json=payload, headers=headers, verify=False)

    # if response.status_code == 200:
    #     print("✅ Foydalanuvchi muvaffaqiyatli qo‘shildi.")
    #     return True
    # else:
    #     print(f"❌ Foydalanuvchi qo‘shishda xatolik: {response.status_code}")
    #     print("🧾 Javob:", response.text)



    def upload_face():
        url = f"{BASE_URL}/ISAPI/Intelligent/FDLib/FaceDataRecord?format=json"
        auth = HTTPDigestAuth(USERNAME, PASSWORD)

        if not os.path.exists(IMAGE_PATH):
            print(f"❌ Rasm topilmadi: {IMAGE_PATH}")
            return False

        files = {
            "FaceDataRecord": (
                None,
                f'{{"faceLibType":"blackFD","FDID":"1","FPID":"{EMPLOYEE_NO}"}}',
                "application/json"
            ),
            "img": (
                IMAGE_PATH,
                open(IMAGE_PATH, "rb"),
                "image/jpeg"
            )
        }

        response = requests.post(url, auth=auth, files=files, verify=False)

        if response.status_code == 200:
            print("🖼 Rasm muvaffaqiyatli biriktirildi.")
            return True
        else:
            print(f"❌ Surat biriktirishda xatolik: {response.status_code}")
            print("🧾 Javob:", response.text)
            return False

    upload_face()

# if __name__ == "__main__":
#     print("🔄 Yangi foydalanuvchini rasm bilan qo‘shish jarayoni boshlandi...")
#     if add_user():
#         upload_face()