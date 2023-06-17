import customtkinter as ctk
import random
app = ctk.CTk()
app.title('KP app')
app.geometry('1000x500')

lable = ctk.CTkLabel(app, text = "ใส่ชื่อสิเราไม่กัดหรอก", font = ('Aris' , 40))
lable.pack(pady=(30, 0))

answer_text = ctk.StringVar()
answer_label = ctk.CTkLabel(app, textvariable = answer_text, font = ('Aria',40))
answer_label.pack(pady=(20, 0))

entry = ctk.CTkEntry(app, placeholder_text = "ใส่ชื่อสิ")
entry.pack(pady=(20, 0))

daa =["เพราะเชื่อคนง่ายไง ถึงโดนเค้าหลอก", "ไอควาย", "ไอโง่", "หน้าโง่", "กากจัง", "ไอเก", "ไร้ค่า", "เปล่าประโยชน์", "ใช้ชีวิตไปแบบสิ้นหวังเถอะ", "ไปตุยซะ"]
choom = ["ทำดีที่สุดแล้ว", "เก่งมาก", "เก่งจัง", "เท่มาก"]

def button_event():
    user_input = entry.get()
    if user_input == "ข้าวปั้น" :
     answer = str(user_input) + ' ' + random.choice(choom)
    elif user_input == "KP" :
     answer = str(user_input) + ' ' + random.choice(choom)
    elif user_input == "แบงค์" :
     answer = str(user_input) + ' ' + random.choice(choom)
    elif user_input == "เตชินท์" :
     answer = str(user_input) + ' ' + random.choice(choom)
    else :
        answer = str(user_input) + ' ' + random.choice(daa)
    answer_text.set(answer)
    print(user_input, answer)

button = ctk.CTkButton(app, text="กดเราสิ", command = button_event, fg_color="black")
button.pack(pady=(20, 0))

app.mainloop()