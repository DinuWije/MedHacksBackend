from app import app, db, bcrypt
from app.models import Caregiver, Patient, Journal
from flask import jsonify, request
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, get_jwt_identity, get_raw_jwt,
                                jwt_optional)


@app.route("/")
def home():
    return("hello dinu")


@app.route("/register", methods=['POST'])
def register():
    req_data = request.get_json()
    account_type = req_data.get('account_type')
    username = req_data.get('username')
    password = req_data.get('password')
    hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')

    status = 'registration error'

    if account_type == "caregiver":
        if Caregiver.query.filter_by(username=username).first() == None:
            user = Caregiver(username=username, password=hashed_pass)
        else:
            status = 'username taken'
    elif account_type == "patient":
        caregiver_name = req_data.get('caregiver')
        caregiver = Caregiver.query.filter_by(username=caregiver_name).first()

        if Patient.query.filter_by(username=username).first() == None:
            user = Patient(username=username, password=hashed_pass,
                           caregiver_id=caregiver.id)
        else:
            status = 'username taken'
    else:
        user = None

    if user:
        db.session.add(user)
        db.session.commit()
        access_token = create_access_token(
            identity=username, expires_delta=False)
        status = f'{access_token}'

    return (status)


@app.route("/caregiver_login")
def caregiver_login():
    status = 'error'

    req_data = request.get_json()
    username = req_data.get('username')
    password = req_data.get('password')
    user = Caregiver.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(
            identity=username, expires_delta=False)
        status = f'{access_token}'

    return status


@app.route("/patient_login")
def patient_login():
    status = 'error'

    req_data = request.get_json()
    username = req_data.get('username')
    password = req_data.get('password')
    user = Patient.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(
            identity=username, expires_delta=False)
        status = f'{access_token}'

    return status


@app.route("/add_journal", methods=['POST'])
@jwt_required
def add_journal():
    patient_name = get_jwt_identity()
    patient = Patient.query.filter_by(username=patient_name).first()

    req_data = request.get_json()

    date = req_data.get('date')
    entry = req_data.get('entry')

    temp_journal_entry = Journal(date=date, entry=entry, patient_id=patient.id)
    db.session.add(temp_journal_entry)
    db.session.commit()

    return("success")


@app.route("/get_patients")
@jwt_required
def get_patients():
    caregiver_name = get_jwt_identity()
    caregiver = Caregiver.query.filter_by(username=caregiver_name).first()
    patients = caregiver.patients
    patients_string = " "
    for patient in patients:
        patients_string += patient.username
    return patients_string


@app.route("/get_journals")
@jwt_required
def get_journals():
    patient_name = get_jwt_identity()
    patient = Patient.query.filter_by(username=patient_name).first()
    journals = patient.journals
    journals_string = " "
    for journal in journals:
        journals_string += journal.entry
    return journals_string
