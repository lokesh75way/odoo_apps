from odoo import models, fields, api

class ManufacturingOrderSearchResult(models.TransientModel):
    _name = 'global.search.result.manufacturing.order'
    _description = 'Manufacturing Orders'

    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Resource ID')
    search_id = fields.Many2one('global.search', string='Search Reference')
    
    name = fields.Char(string='Name')
    origin = fields.Char(string="Origin")
    activity_summary = fields.Char(string="Activity summary")