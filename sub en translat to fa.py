import os
from googletrans import Translator

filepath = 'C:\\Users' #آدرس فایل زیرنویس
filename1 = "S01 .srt" #نام زیرنویس مورد نظر
filename2 = "S01.txt"# نام ذخیره شدن زیرنویس ترجمه شده

nums = ["0", "1","2","3","4","5","6","7","8","9"]
translator = Translator()

with open(os.path.join(filepath,filename1)) as f:
    sub_line = f.readlines()

with open(os.path.join(filepath,filename2), "w" , encoding="utf-8") as f:
    for line_en in sub_line:
        if line_en[0] in nums:
            f.write(line_en)
        elif line_en == "\n":
            f.write("\n")

        else:
            line_fa = translator.translate(line_en, src="en", dest="fa")
            f.write(line_fa.text)

