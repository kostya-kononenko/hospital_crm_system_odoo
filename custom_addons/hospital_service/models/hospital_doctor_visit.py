from odoo import api, fields, models
from odoo.exceptions import UserError


class DoctorVisit(models.Model):
    _name = 'hospital.doctor_visit'
    _description = 'Doctor Visit'

    state = fields.Selection(
        [
            ('create', 'Create Visit'),
            ('new', 'Visit Doctor'),
            ('add_research', 'Add research'),
            ('confirm_research', 'Confirm research'),
            ('make_diagnosis', 'Make diagnosis'),
            ('confirm_diagnosis', 'Confirm diagnosis'),
            ('make_recommendations', 'Make recommendations'),
            ('confirm_recommendations', 'Confirm recommendations'),
            ('completed', 'Visit Completed')
        ],
        default='create',
        string='Status')

    doctor = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    patient = fields.Many2one('hospital.patient', string='Patient', required=True)
    appointment_date = fields.Date(string='Appointment Date', required=True)
    time_slot = fields.Many2one(
        'hospital.schedule.line',
        string='Available Time',
        domain="[('schedule_id.appointment_date', '=', appointment_date)]",
        required=True
    )
    recommendations = fields.Text(string='Recommendations')
    is_completed = fields.Boolean(string='Visit Completed', default=False)
    research_ids = fields.One2many('hospital.research', 'doctor_visit', string='Research')
    diagnosis_ids = fields.One2many('hospital.diagnosis', 'doctor_visit', string='Diagnosis')

    def action_finish_research(self):
        if all(research.status_research == 'accepted_research' for research in self.research_ids):
            self.state = 'confirm_research'
        else:
            raise UserError("Not all research are in 'accepted' status.")

    def action_skip_research(self):
        self.state = 'confirm_research'

    def action_finish_diagnosis(self):
        if all(diagnosis.status_diagnosis == 'accepted_diagnosis' for diagnosis in self.diagnosis_ids):
            self.state = 'confirm_diagnosis'
        else:
            raise UserError("Not all diagnosis are in 'accepted' status.")

    def action_skip_diagnosis(self):
        self.state = 'confirm_diagnosis'

    # @api.model
    # def check_access_create(self):
    #     if self.state == 'confirm_research':
    #         raise UserError("Cannot add new research to a completed visit.")

    @api.model
    def create(self, values):
        record = super(DoctorVisit, self).create(values)
        if record:
            record.write({'state': 'new'})
        return record

    def unlink(self):
        for record in self:
            if record.state != 'new':
                raise UserError("Cannot delete a record with status other than 'new'.")
        return super(DoctorVisit, self).unlink()
