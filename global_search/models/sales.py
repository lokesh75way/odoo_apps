from odoo import models, fields, api

class SaleOrderSearchResult(models.TransientModel):
    _name = 'global.search.result.sale.order'
    _description = 'Sale Orders'

    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Resource ID')
    search_id = fields.Many2one('global.search', string='Search Reference')
    
    name = fields.Char(string='Name')
    activity_summary = fields.Char(string="Activity summary")
    origin = fields.Char(string="Origin")
    reference = fields.Char(string="Reference")
    country_code = fields.Char(string="Countery Code")
    incoterm_location = fields.Char(string="Incoterm Location")

    
    