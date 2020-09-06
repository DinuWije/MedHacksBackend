from app import db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Caregiver(db.Model):
    __tablename__ = 'caregivers'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(120), nullable=False, unique=True)
    password = Column('password', String(60), nullable=False)
    patients = relationship('Patient', backref='owner')


class Patient(db.Model):
    __tablename__ = 'patients'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(120), nullable=False, unique=True)
    password = Column('password', String(60), nullable=False)
    caregiver_id = Column(Integer, ForeignKey('caregivers.id'), nullable=False)
    journals = relationship('Journal', backref='owner')


class Journal(db.Model):
    __tablename__ = 'journals'

    id = Column('id', Integer, primary_key=True)
    date = Column('date', String(10), nullable=True, default="N/A")
    entry = Column('entry', String(1500), nullable=False)
    sentiment_score = Column('sentiment_score', String(20), nullable=False)
    sentiment_mag = Column('sentiment_mag', String(20), nullable=False)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)


db.create_all()
db.session.commit()
