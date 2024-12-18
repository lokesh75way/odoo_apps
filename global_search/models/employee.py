# models/global_search.py
from odoo import models, fields, api

class EmployeeSearchResult(models.TransientModel):
    _name = 'global.search.result.employee'
    _description = 'Employees'

    name = fields.Char(string='Name')
    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Resource ID')
    search_id = fields.Many2one('global.search', string='Search Reference')

    activity_summary = fields.Char(string='Activity Summary') 
    job_title = fields.Char(string='Job Title') 
    work_phone = fields.Char(string='Work Phone') 
    mobile_phone = fields.Char(string='Mobile Phone') 
    work_email = fields.Char(string='Work Email')
    private_email = fields.Char(string='Private Email') 
    spouse_complete_name = fields.Char(string='Spouse Complete Name')
    place_of_birth = fields.Char(string='Place of Birth') 
    study_field = fields.Char(string='Study Field')
    study_school = fields.Char(string='Study School')
    emergency_contact = fields.Char(string='Emergency Contact')
    emergency_phone = fields.Char(string='Emergency Phone')
    phone = fields.Char(string='Phone')
    pin = fields.Char(string='PIN')