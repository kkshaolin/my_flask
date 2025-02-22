from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
import sqlalchemy as sa

bcrypt = Bcrypt()  # เข้ารหัส รหัสผ่าน

class Base(DeclarativeBase):  # คลาสพื้นฐาน SQLAlchemy
    pass

db = SQLAlchemy(model_class=Base)  # สร้างอ็อบเจกต์ SQLAlchemy

def init_app(app):  # ฟังก์ชันสำหรับเริ่มต้น app
    db.init_app(app)  # เริ่มต้น SQLAlchemy ด้วย Flask
    bcrypt.init_app(app)  # เริ่มต้น Bcrypt ด้วย Flask
    with app.app_context():  # ใช้ context(บริบท) ของแอปพลิเคชัน
        db.create_all()  # สร้างตารางข้อมูล

class User(db.Model, UserMixin):  # สำหรับเก็บข้อมูลผู้ใช้
    __tablename__ = "users"  # ชื่อตาราง
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)  # คอลัมน์ `id` เป็น primary key
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)  # เก็บชื่อ username
    _password_hash: Mapped[str] = mapped_column(sa.String, nullable=False)  # เก็บรหัสที่ hash แล้ว
    
    @hybrid_property  # ป้องกันการเข้าถึงรหัสผ่านโดยตรง
    def password_hash(self):
        raise Exception("Password hashes may not be viewed.")
    
    @password_hash.setter  # เข้ารหัสรหัสผ่านก่อนบันทึกลงฐานข้อมูล
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):  # ตรวจสอบรหัสผ่าน
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))
    
    serialize_rules = ("-_password_hash",)  # ซ่อน _password_hash เมื่อ serialize