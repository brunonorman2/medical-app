from fastapi import HTTPException

from schema.doctor import DoctorsCreate, Doctors, doctors
from schema.doctor import Doctors, doctors
from utils.doctor import DoctorHelpers

class DoctorService:

    @staticmethod
    def create_doctor(payload: DoctorsCreate):
        id = len(doctors)
        doctor: Doctors = doctors[payload.doctor]
id=id,
doctor=doctors,
name= str
specialization= str
phone=str
    
@staticmethod
def get_doctor_by_id(doctor_id: int):
        doctor = DoctorHelpers.get_doctor_by_id(doctor_id)
        if not doctor:
            raise HTTPException(detail='Flight not found', status_code=404)
        return doctor
    
@staticmethod
def edit_doctor(doctor_id: int, payload: DoctorsCreate):
        doctor: Doctors  = DoctorHelpers.get_doctor_by_id(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found', status_code=404)
        doctor: Doctors = doctors[payload.doctor]

     
        return doctor
    
@staticmethod
def edit_doctor(doctor_id: int, payload: DoctorsCreate):
 doctor=doctors,
name= str
specialization= str
phone=str
doctor: doctors  = DoctorHelpers.get_doctor_by_id (doctor_id)
if not doctor:
            raise HTTPException(detail='Doctor not found', status_code=404)
del doctors[doctor_id]






