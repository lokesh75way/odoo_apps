from odoo import models, fields, api

class InventoryProductSearchResult(models.TransientModel):
    _name = 'global.search.result.inventory.product'
    _description = 'Inventory Product'

    name = fields.Char(string='Name')
    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Resource ID')
    search_id = fields.Many2one('global.search', string='Search Reference')
    activity_summary = fields.Char(string="Activity summary")
    default_code = fields.Char(string="Default code")
    l10n_in_hsn_code = fields.Char(string="l10n_in_hsn_code")
    l10n_in_hsn_description = fields.Char(string="l10n_in_hsn_description")

    
class InventoryTransferSearchResult(models.TransientModel):
    _name = 'global.search.result.inventory.transfer'
    _description = 'Inventory Transfer'

    name = fields.Char(string='Name')
    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Resource ID')
    search_id = fields.Many2one('global.search', string='Search Reference')
    
    activity_summary = fields.Char(string="Activity summary")
    name = fields.Char(string="Name")
    origin = fields.Char(string="Origin")
    country_code = fields.Char(string="Country code")
    
class InventoryProductVariantSearchResult(models.TransientModel):
    _name = 'global.search.result.inventory.product.varient'
    _description = 'Inventory Product variant'

    name = fields.Char(string='Name')
    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Resource ID')
    search_id = fields.Many2one('global.search', string='Search Reference')
    
    activity_summary = fields.Char(string="Activity summary")
    name = fields.Char(string="Name")
    origin = fields.Char(string="Origin")
    products_availability = fields.Char(string="Products availability")
    country_code = fields.Char(string="Country code")
    
    default_code = fields.Char(string="default_code")
    combination_indices = fields.Char(string="combination_indices")
    l10n_in_hsn_code = fields.Char(string="l10n_in_hsn_code")
    l10n_in_hsn_description = fields.Char(string="l10n_in_hsn_description")
