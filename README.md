# อธิบายโค้ดเบื้องต้น
  การทำงานเริ่มต้นที่ app.py โดยจะมีการนำเข้าไลบรารี่ flask ,ไฟล๋ models และไฟล์ forms
จากนั้น สร้างหน้าเว็บ flask และต่อ database เข้ากับเว็บโดยจะสร้าง database ไว้ที่โฟลเดอร์ instance ซึ่งเก็บข้อมูล username และ password ไว้
จากนั้น มีการใช้ login_manage ในการจัดการการ login ที่มีการโหลดบัญชีผู้ใช้จากฐานข้อมูล โดยใช้การทำงานของไฟล์ models ที่มี class user ในการเก็บ username และ password ที่มีการ hash ไว้
จากนั้น กำหนด route หน้าต่าง route ที่มีการทำงานพิเศษๆ ได้แก้ register ,login และ logout ส่วนหน้าอื่่นจะเป็นการแสดงหน้าเว็บแบบทั่วไป ที่บางหน้าอาจจำกัดสิทธิในการเข้าในบางหน้า
สำหรับ register จะมีการใช้ from ที่สร้างไว้ในไฟล์ forms (โดยในไฟล์ forms ใน class RegisterForm ก็สร้าง from สำหรับเก็บข้อมูล username และ password)ในการเก็บข้อมูล แล้วเอาข้อมูลไปใส่ใน database
สำหรับ login  ใช้ from ในไฟล์ forms ใน class LoginForm หลังจากรับข้อมูลมาก็ไปหา username ใน database ถ้ามีก็ login สำเร็จ ไม่มีก็ไปยังหน้า register เพื่อให้ผู้ใช้เพิ่มข้อมูลใน database
สำหรับ logout ก็ใช้ logout_user ซึ่งมีอยู่แล้วในโมดูล login_manage
สุดท้ายก็ใช้คำสั่ง run app เพื่่อแสดงเว็บออกมา

# วิธีรัน web
  1. clone code จาก git นี้
  2. ใช้งาน Virtual Machine ด้วยคำสั่ง ven\Scripts\activate
  3. run code ในไฟล์ app.py
