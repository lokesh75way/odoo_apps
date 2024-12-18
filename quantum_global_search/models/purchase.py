# models/global_search.py
from odoo import models, fields, api

class PurchaseSearchResult(models.TransientModel):
    _name = 'global.search.result.purchase'
    _description = 'Purchase'

    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Resource ID')
    search_id = fields.Many2one('global.search', string='Search Reference')
    
    name = fields.Char(string='Name')
    activity_summary = fields.Char(string="Activity Summery")
    origin = fields.Char(string="Origin")
    country_code = fields.Char(string="Counery Code")
    incoterm_location = fields.Char(string="Incoterm Location")
    