from odoo import models, fields, api
    
class AccountInvoiceSearchResult(models.TransientModel):
    _name = 'global.search.result.account.invoice'
    _description = 'Account Invoice'

    name = fields.Char(string='Name')
    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Resource ID')
    search_id = fields.Many2one('global.search', string='Search Reference')
    
    activity_summary = fields.Char(string="Activity summary")
    country_code = fields.Char(string="Country code")
    payment_reference = fields.Char(string="Payment reference")
    invoice_source_email = fields.Char(string="Invoice source email")
    invoice_partner_display_name = fields.Char(string="Invoice partner display name")
    invoice_origin = fields.Char(string="Invoice origin")
    l10n_in_gstin = fields.Char(string="l10n_in_gstin")
    l10n_in_shipping_bill_number = fields.Char(string="l10n_in_shipping_bill_number")

    
class AccountPaymentSearchResult(models.TransientModel):
    _name = 'global.search.result.account.payment'
    _description = 'Account Payment'

    name = fields.Char(string='Name')
    model = fields.Char(string='Model')
    res_id = fields.Integer(string='Resource ID')
    search_id = fields.Many2one('global.search', string='Search Reference')
    
    activity_summary = fields.Char(string="Activity summary")
    payment_reference = fields.Char(string="Payment reference")
    payment_method_code = fields.Char(string="payment method code")
    country_code = fields.Char(string="Country code")
    invoice_source_email = fields.Char(string="Invoice source email")
    invoice_partner_display_name = fields.Char(string="Invoice partner display name")
    invoice_origin = fields.Char(string="Invoice origin")
    l10n_in_gstin = fields.Char(string="l10n_in_gstin")
    l10n_in_shipping_bill_number = fields.Char(string="l10n_in_shipping_bill_number")
