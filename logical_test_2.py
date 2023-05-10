def number_to_roman(number):
    roman_digits = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    if number == 0:
        return "N/A"

    roman_text = ""
    for value, symbol in roman_digits.items():
        while number >= value:
            roman_text += symbol
            number -= value

    return roman_text

# ตัวอย่างการเรียกใช้งาน
number = int(input("ป้อนตัวเลขที่ต้องการแปลงเป็นตัวเลขโรมัน: "))
if 0 < number <= 1000:
    roman_text = number_to_roman(number)
    print("ตัวเลข", number, "แปลงเป็นตัวเลขโรมันคือ", roman_text)
else:
    print("ค่าที่รับต้องมีค่าตั้งแต่ 1 ถึง 1000")