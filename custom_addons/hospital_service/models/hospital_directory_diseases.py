from odoo import models, fields, api


class Disease(models.Model):
    _name = "hospital.disease"
    _description = "Disease Directory"
    _order = "name"

    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "Disease name must be unique."),
        ("unique_code", "UNIQUE(code)", "Disease code must be unique."),
    ]

    name = fields.Char(string="Disease Name", required=True)
    code = fields.Char(string="Disease Code")
    description = fields.Text(string="Description")
    parent_id = fields.Many2one("hospital.disease", string="Parent Disease")
    child_ids = fields.One2many(
        "hospital.disease", "parent_id", string="Child Diseases"
    )
