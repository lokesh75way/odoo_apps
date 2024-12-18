# models/global_search.py
from odoo import models, fields, api

class PartnerSearchResult(models.TransientModel):
    _name = 'global.search.result.partner'
    _description = 'Partners'

    name = fields.Char(string='Name')
    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Resource ID')
    search_id = fields.Many2one('global.search', string='Search Reference')
    
    activity_summary = fields.Char(string='Activity Summary') 
    display_name = fields.Char(string='Display Name') 
    parent_name = fields.Char(string='Parent Name') 
    company_registry = fields.Char(string='Company Registry') 
    website = fields.Char(string='Website') 
    street = fields.Char(string='Street') 
    street2 = fields.Char(string='Street 2')
    zip = fields.Char(string='ZIP') 
    city = fields.Char(string='City') 
    country_code = fields.Char(string='Country Code') 
    email = fields.Char(string='Email') 
    phone = fields.Char(string='Phone') 
    mobile = fields.Char(string='Mobile') 
    commercial_company_name = fields.Char(string='Commercial Company Name') 
    company_name = fields.Char(string='Company Name') 
    additional_info = fields.Char(string='Additional Info') 
    phone_sanitized = fields.Char(string='Phone Sanitized')