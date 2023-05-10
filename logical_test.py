def number_to_thai_text(number):
    thai_digits = {
        "0": "ศูนย์",
        "1": "หนึ่ง",
        "2": "สอง",
        "3": "สาม",
        "4": "สี่",
        "5": "ห้า",
        "6": "หก",
        "7": "เจ็ด",
        "8": "แปด",
        "9": "เก้า"
    }

    thai_units = {
        1: "",
        10: "สิบ",
        100: "ร้อย",
        1000: "พัน",
        10000: "หมื่น",
        100000: "แสน",
        1000000: "ล้าน"
    }

    if number == 0:
        return thai_digits[str(number)]

    thai_text = ""
    magnitude = 1000000

    while magnitude > 0:
        digit = number // magnitude
        if digit > 0:
            if digit == 1 and magnitude == 10:
                thai_text += thai_units[magnitude]
            else:
                thai_text += thai_digits[str(digit)] + thai_units[magnitude]
        number %= magnitude
        magnitude //= 10

    return thai_text

# ตัวอย่างการเรียกใช้งาน
number = int(input("ป้อนตัวเลขที่ต้องการแปลงเป็นภาษาไทย: "))
if 0 <= number < 10000000:
    thai_text = number_to_thai_text(number)
    print("ตัวเลข", number, "แปลงเป็นภาษาไทยคือ", thai_text)
else:
    print("ค่าที่รับต้องมีค่าตั้งแต่ 0 ถึง 9,999,999")
