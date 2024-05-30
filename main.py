import flet as ft
import requests
from datetime import datetime

API_BASE_URL = "http://127.0.0.1:8000"

def main(page: ft.Page):
    page.title = "Medical Dispatch Management"
    page.theme_mode = 'light'

    def add_diagnosis(e):
        diagnosis = {
            "initial_diagnosis": diagnosis_input.value,
        }
        response = requests.post(f"{API_BASE_URL}/diagnoses/", json=diagnosis)
        if response.status_code == 200:
            page.add(ft.Text("Diagnosis added successfully!", color="green"))
        else:
            page.add(ft.Text("Error adding diagnosis.", color="red"))

    diagnosis_input = ft.TextField(label="Diagnosis", autofocus=True)
    diagnosis_form = ft.Column([diagnosis_input, ft.ElevatedButton("Add Diagnosis", on_click=add_diagnosis)])

    def add_patient(e):
        patient = {
            "first_name": patient_first_name_input.value,
            "last_name": patient_last_name_input.value,
            "approximate_age": int(patient_age_input.value),
            "address": patient_address_input.value,
            "gender_id": int(patient_gender_id_input.value),
            "initial_diagnosis_id": int(patient_diagnosis_id_input.value),
        }
        response = requests.post(f"{API_BASE_URL}/patients/", json=patient)
        if response.status_code == 200:
            page.add(ft.Text("Patient added successfully!", color="green"))
        else:
            page.add(ft.Text("Error adding patient.", color="red"))

    patient_first_name_input = ft.TextField(label="First Name")
    patient_last_name_input = ft.TextField(label="Last Name")
    patient_age_input = ft.TextField(label="Age")
    patient_address_input = ft.TextField(label="Address")
    patient_gender_id_input = ft.TextField(label="Gender ID")
    patient_diagnosis_id_input = ft.TextField(label="Diagnosis ID")
    patient_form = ft.Column([
        patient_first_name_input, patient_last_name_input, patient_age_input,
        patient_address_input, patient_gender_id_input, patient_diagnosis_id_input,
        ft.ElevatedButton("Add Patient", on_click=add_patient)
    ])

    def add_position(e):
        position = {
            "position_name": position_name_input.value,
        }
        response = requests.post(f"{API_BASE_URL}/positions/", json=position)
        if response.status_code == 200:
            page.add(ft.Text("Position added successfully!", color="green"))
        else:
            page.add(ft.Text("Error adding position.", color="red"))

    position_name_input = ft.TextField(label="Position Name")
    position_form = ft.Column([position_name_input, ft.ElevatedButton("Add Position", on_click=add_position)])

    def add_employee(e):
        employee = {
            "employee_number": int(employee_number_input.value),
            "first_name": employee_first_name_input.value,
            "last_name": employee_last_name_input.value,
            "middle_name": employee_middle_name_input.value,
            "date_of_birth": employee_dob_input.value,
            "position_id": int(employee_position_id_input.value),
            "start_date": employee_start_date_input.value,
            "end_date": employee_end_date_input.value,
            "rate_id": int(employee_rate_id_input.value),
            "brigade_id": int(employee_brigade_id_input.value),
        }
        response = requests.post(f"{API_BASE_URL}/employees/", json=employee)
        if response.status_code == 200:
            page.add(ft.Text("Employee added successfully!", color="green"))
        else:
            page.add(ft.Text("Error adding employee.", color="red"))

    employee_number_input = ft.TextField(label="Employee Number")
    employee_first_name_input = ft.TextField(label="First Name")
    employee_last_name_input = ft.TextField(label="Last Name")
    employee_middle_name_input = ft.TextField(label="Middle Name")
    employee_dob_input = ft.TextField(label="Date of Birth (YYYY-MM-DD)")
    employee_position_id_input = ft.TextField(label="Position ID")
    employee_start_date_input = ft.TextField(label="Start Date (YYYY-MM-DD)")
    employee_end_date_input = ft.TextField(label="End Date (YYYY-MM-DD, Optional)")
    employee_rate_id_input = ft.TextField(label="Rate ID")
    employee_brigade_id_input = ft.TextField(label="Brigade ID")
    employee_form = ft.Column([
        employee_number_input, employee_first_name_input, employee_last_name_input,
        employee_middle_name_input, employee_dob_input, employee_position_id_input,
        employee_start_date_input, employee_end_date_input, employee_rate_id_input,
        employee_brigade_id_input, ft.ElevatedButton("Add Employee", on_click=add_employee)
    ])

    def add_internal_order(e):
        order = {
            "order_number": int(order_number_input.value),
            "order_date": order_date_input.value,
            "shift_start_date": shift_start_date_input.value,
            "shift_end_date": shift_end_date_input.value,
        }
        response = requests.post(f"{API_BASE_URL}/internalorders/", json=order)
        if response.status_code == 200:
            page.add(ft.Text("Internal Order added successfully!", color="green"))
        else:
            page.add(ft.Text("Error adding internal order.", color="red"))

    order_number_input = ft.TextField(label="Order Number")
    order_date_input = ft.TextField(label="Order Date (YYYY-MM-DD)")
    shift_start_date_input = ft.TextField(label="Shift Start Date (YYYY-MM-DD)")
    shift_end_date_input = ft.TextField(label="Shift End Date (YYYY-MM-DD)")
    internal_order_form = ft.Column([
        order_number_input, order_date_input, shift_start_date_input,
        shift_end_date_input, ft.ElevatedButton("Add Internal Order", on_click=add_internal_order)
    ])

    def add_brigade(e):
        brigade = {
            "brigade_number": int(brigade_number_input.value),
            "specialization": specialization_input.value,
            "internal_order_id": int(internal_order_id_input.value),
        }
        response = requests.post(f"{API_BASE_URL}/brigades/", json=brigade)
        if response.status_code == 200:
            page.add(ft.Text("Brigade added successfully!", color="green"))
        else:
            page.add(ft.Text("Error adding brigade.", color="red"))

    brigade_number_input = ft.TextField(label="Brigade Number")
    specialization_input = ft.TextField(label="Specialization")
    internal_order_id_input = ft.TextField(label="Internal Order ID")
    brigade_form = ft.Column([
        brigade_number_input, specialization_input, internal_order_id_input,
        ft.ElevatedButton("Add Brigade", on_click=add_brigade)
    ])

    def add_shift_rate(e):
        shift_rate = {
            "rate": float(shift_rate_input.value),
        }
        response = requests.post(f"{API_BASE_URL}/shiftrates/", json=shift_rate)
        if response.status_code == 200:
            page.add(ft.Text("Shift Rate added successfully!", color="green"))
        else:
            page.add(ft.Text("Error adding shift rate.", color="red"))

    shift_rate_input = ft.TextField(label="Rate")
    shift_rate_form = ft.Column([shift_rate_input, ft.ElevatedButton("Add Shift Rate", on_click=add_shift_rate)])

    def add_call(e):
        call = {
            "call_date_time": call_date_time_input.value,
            "patient_id": int(patient_id_input.value),
            "brigade_id": int(brigade_id_input.value),
            "measures_taken": measures_taken_input.value,
        }
        response = requests.post(f"{API_BASE_URL}/calls/", json=call)
        if response.status_code == 200:
            page.add(ft.Text("Call added successfully!", color="green"))
        else:
            page.add(ft.Text("Error adding call.", color="red"))

    call_date_time_input = ft.TextField(label="Call Date Time (YYYY-MM-DDTHH:MM:SS)")
    patient_id_input = ft.TextField(label="Patient ID")
    brigade_id_input = ft.TextField(label="Brigade ID")
    measures_taken_input = ft.TextField(label="Measures Taken")
    call_form = ft.Column([
        call_date_time_input, patient_id_input, brigade_id_input,
        measures_taken_input, ft.ElevatedButton("Add Call", on_click=add_call)
    ])

    def add_call_result(e):
        call_result = {
            "result_description": result_description_input.value,
        }
        response = requests.post(f"{API_BASE_URL}/callresults/", json=call_result)
        if response.status_code == 200:
            page.add(ft.Text("Call Result added successfully!", color="green"))
        else:
            page.add(ft.Text("Error adding call result.", color="red"))

    result_description_input = ft.TextField(label="Result Description")
    call_result_form = ft.Column([result_description_input, ft.ElevatedButton("Add Call Result", on_click=add_call_result)])

    def add_dispatch(e):
        dispatch = {
            "dispatch_time": dispatch_time_input.value,
            "arrival_time": arrival_time_input.value,
            "call_id": int(call_id_input.value),
            "result_id": int(result_id_input.value),
        }
        response = requests.post(f"{API_BASE_URL}/dispatches/", json=dispatch)
        if response.status_code == 200:
            page.add(ft.Text("Dispatch added successfully!", color="green"))
        else:
            page.add(ft.Text("Error adding dispatch.", color="red"))

    dispatch_time_input = ft.TextField(label="Dispatch Time (YYYY-MM-DDTHH:MM:SS)")
    arrival_time_input = ft.TextField(label="Arrival Time (YYYY-MM-DDTHH:MM:SS)")
    call_id_input = ft.TextField(label="Call ID")
    result_id_input = ft.TextField(label="Result ID")
    dispatch_form = ft.Column([
        dispatch_time_input, arrival_time_input, call_id_input,
        result_id_input, ft.ElevatedButton("Add Dispatch", on_click=add_dispatch)
    ])

    forms_tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Diagnosis", content=diagnosis_form),
            ft.Tab(text="Patient", content=patient_form),
            ft.Tab(text="Position", content=position_form),
            ft.Tab(text="Employee", content=employee_form),
            ft.Tab(text="Internal Order", content=internal_order_form),
            ft.Tab(text="Brigade", content=brigade_form),
            ft.Tab(text="Shift Rate", content=shift_rate_form),
            ft.Tab(text="Call", content=call_form),
            ft.Tab(text="Call Result", content=call_result_form),
            ft.Tab(text="Dispatch", content=dispatch_form),
        ],
    )

    page.add(forms_tabs)

ft.app(target=main)
