{
    "name": "Hospital Service",
    "description": """Applications for hospital services for clients who value comfort and quality""",
    "version": "1.0",
    "author": "Kostiantyn Kononenko",
    "category": "Human Resources",
    "depends": [],
    "data": [
        "security/ir.model.access.csv",
        "views/hospital_contact_person_view.xml",
        "views/hospital_doctor_view.xml",
        "views/hospital_patient_view.xml",
        "views/hospital_directory_diseases_view.xml",
        "views/hospital_research_type_view.xml",
        "views/hospital_sample_type_view.xml",
        "views/hospital_doctor_schedule_view.xml",
        "views/hospital_doctor_visit_view.xml",
        "views/hospital_research_view.xml",
        "views/hospital_diagnosis_view.xml",
        "views/hospital_personal_doctor_history_view.xml",
        "views/hospital_change_doctor_wizard_form_view.xml",
        "views/hospital_report_wizard_enter_date_view.xml",
        "views/hospital_report_wizard_display_information_view.xml",
        "views/menu_items.xml",
        # Data files
        "data/hospital.doctor.csv",
        "data/hospital.contactperson.csv",
        "data/hospital.patient.csv",
        "data/hospital.disease.csv",
        "data/hospital.research_type.csv",
        "data/hospital.sample_type.csv",
        # Report files
        "report/report_template.xml",
        "report/hospital_doctor_visit_report.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
