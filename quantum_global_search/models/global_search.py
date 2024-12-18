# models/global_search.py
from odoo import models, fields, api

class GlobalSearch(models.TransientModel):
    _name = 'global.search'
    _description = 'Global Search'

    name = fields.Char(string='Search Term')
    
    search_results_partners = fields.One2many('global.search.result.partner', 'search_id', string='Partners')
    
    search_results_employees = fields.One2many('global.search.result.employee', 'search_id', string='Employees')
    
    search_results_purchase = fields.One2many('global.search.result.purchase', 'search_id', string='Purchase')
    
    search_results_sale_orders = fields.One2many('global.search.result.sale.order', 'search_id', string='Sale orders')
    
    search_results_account_invoices = fields.One2many('global.search.result.account.invoice', 'search_id', string='Account Invoices')
    search_results_account_payments = fields.One2many('global.search.result.account.payment', 'search_id', string='Account Payments')
    
    search_results_inventory_products = fields.One2many('global.search.result.inventory.product', 'search_id', string='Inventory products')
    search_results_inventory_transfers = fields.One2many('global.search.result.inventory.transfer', 'search_id', string='Inventory Transfer')
    search_results_inventory_product_varients = fields.One2many('global.search.result.inventory.product.varient', 'search_id', string='Inventory product varient')
    search_results_manufacturing_orders = fields.One2many('global.search.result.manufacturing.order', 'search_id', string='Manufacturing orders')
    
    fields_by_model = {
        # Employee
        'hr.employee': ['activity_summary', 'name', 'job_title', 'work_phone', 'mobile_phone', 'work_email', 'private_email', 'spouse_complete_name', 'place_of_birth', 'study_field', 'study_school', 'emergency_contact', 'emergency_phone', 'phone', 'pin'],
          
        # Partner
        'res.partner': ['activity_summary', 'name', 'display_name', 'parent_name', 'company_registry', 'website', 'street', 'street2', 'zip', 'city', 'country_code', 'email', 'phone', 'mobile', 'commercial_company_name', 'company_name', 'additional_info', 'phone_sanitized'],
        
         # Sale
        'sale.order':  [ 'name', 'activity_summary', 'origin', 'reference', 'country_code', 'incoterm_location'],
        
        # Purchase
        'purchase.order':  ['name', 'activity_summary', 'origin', 'country_code', 'incoterm_location'],
        
        # Inventory
        'stock.picking': ['activity_summary', 'name', 'origin', 'country_code'],
        'product.template': ['activity_summary', 'name', 'default_code', 'l10n_in_hsn_code', 'l10n_in_hsn_description'],
        'product.product': ['activity_summary', 'default_code', 'combination_indices', 'name', 'l10n_in_hsn_code', 'l10n_in_hsn_description'],
        
        
        # accounting
        'account.move': ['activity_summary', 'name', 'country_code', 'payment_reference', 'invoice_source_email', 'invoice_partner_display_name', 'invoice_origin', 'l10n_in_gstin', 'l10n_in_shipping_bill_number'],
        'account.payment': ['activity_summary', 'payment_reference', 'payment_method_code', 'country_code', 'name', 'invoice_source_email', 'invoice_partner_display_name', 'invoice_origin', 'l10n_in_gstin', 'l10n_in_shipping_bill_number'],
        
        # Manufacturing
        'mrp.production': ['activity_summary', 'name', 'origin'],
        }
    
    search_models = list(fields_by_model.keys())

    
    # Format data by model name
    def format_data_by_model_name(self, model, record):
        match model:
            case 'res.partner':
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'res_id': record.id,
                    'activity_summary': record.activity_summary,
                    'name': record.name,
                    'display_name': record.display_name,
                    'parent_name': record.parent_name,
                    'company_registry': record.company_registry,
                    'website': record.website,
                    'street': record.street,
                    'street2': record.street2,
                    'zip': record.zip,
                    'city': record.city,
                    'country_code': record.country_code,
                    'email': record.email,
                    'phone': record.phone,
                    'mobile': record.mobile,
                    'commercial_company_name': record.commercial_company_name,
                    'company_name': record.company_name,
                    'additional_info': record.additional_info,
                    'phone_sanitized': record.phone_sanitized
                    
                }
            case 'hr.employee':
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'res_id': record.id,
                    'activity_summary': record.activity_summary, 
                    'job_title': record.job_title,
                    'work_phone': record.work_phone,
                    'mobile_phone': record.mobile_phone,
                    'work_email': record.work_email,
                    'private_email': record.private_email,
                    'spouse_complete_name': record.spouse_complete_name,
                    'place_of_birth': record.place_of_birth,
                    'study_field': record.study_field,
                    'study_school': record.study_school,
                    'emergency_contact': record.emergency_contact,
                    'emergency_phone': record.emergency_phone,
                    'phone': record.phone,
                    'pin': record.pin
                }
            case 'purchase.order':
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'res_id': record.id,
                    'activity_summary': record.activity_summary,
                    'origin': record.origin,
                    'country_code': record.country_code,
                    'incoterm_location': record.incoterm_location 
                }
            case 'sale.order':
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'reference': record.reference,
                    'res_id': record.id,
                    'activity_summary': record.activity_summary,
                    'origin': record.origin,
                    'country_code': record.country_code,
                    'incoterm_location': record.incoterm_location,
                }
            case 'account.move':
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'res_id': record.id,
                    'activity_summary': record.activity_summary,
                    'country_code': record.country_code,
                    'payment_reference': record.payment_reference,
                    'invoice_source_email': record.invoice_source_email,
                    'invoice_partner_display_name': record.invoice_partner_display_name,
                    'invoice_origin': record.invoice_origin,
                    'l10n_in_gstin': record.l10n_in_gstin,
                    'l10n_in_shipping_bill_number': record.l10n_in_shipping_bill_number,

                }
            case 'account.payment':
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'res_id': record.id,
                    'activity_summary': record.activity_summary,
                    'payment_reference': record.payment_reference,
                    'payment_method_code': record.payment_method_code,
                    'country_code': record.country_code,
                    'invoice_source_email': record.invoice_source_email,
                    'invoice_partner_display_name': record.invoice_partner_display_name,
                    'invoice_origin': record.invoice_origin,
                    'l10n_in_gstin': record.l10n_in_gstin,
                    'l10n_in_shipping_bill_number': record.l10n_in_shipping_bill_number,
                }
            case 'product.template':
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'res_id': record.id,
                    'activity_summary': record.activity_summary,
                    'default_code': record.default_code,
                    'l10n_in_hsn_code': record.l10n_in_hsn_code,
                    'l10n_in_hsn_description': record.l10n_in_hsn_description,

                }
            case 'stock.picking':
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'res_id': record.id,
                    'activity_summary': record.activity_summary,
                    'origin': record.origin,
                    'country_code': record.country_code,
                }
            case 'product.product':
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'res_id': record.id,
                    'activity_summary': record.activity_summary,
                    'default_code': record.default_code,
                    'combination_indices': record.combination_indices,
                    'l10n_in_hsn_code': record.l10n_in_hsn_code,
                    'l10n_in_hsn_description': record.l10n_in_hsn_description,
                }
            case 'mrp.production':
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'res_id': record.id,
                    'origin': record.origin,
                    'activity_summary': record.activity_summary,
                }
            case default:
                return {
                    'id': record.id,
                    'name': record.name,
                    'model': model,
                    'res_id': record.id
                }

    
    def get_data_by_model_name(self, model, records):
        results = []
        for record in records:
            result = self.format_data_by_model_name(model, record)
            results.append((0, 0, result))
        if model == 'res.partner':
            self.search_results_partners = results
        if model == 'hr.employee':
            self.search_results_employees = results
        if model == 'purchase.order':
            self.search_results_purchase = results
        if model == 'sale.order':
            self.search_results_sale_orders = results
        if model == 'account.move':
            self.search_results_account_invoices = results
        if model == 'account.payment':
            self.search_results_account_payments = results
        if model == 'product.template':
            self.search_results_inventory_products = results
        if model == 'stock.picking':
            self.search_results_inventory_transfers = results
        if model == 'product.product':
            self.search_results_inventory_product_varients = results
        if model == 'mrp.production':
            self.search_results_manufacturing_orders = results
    
    
    def get_domain_by_model_name(self, model, search_term):
        char_fields = self.fields_by_model[model]
        
        # Build the domain to search across all char fields
        domain = ['|'] * (len(char_fields) - 1)  # Add '|' for OR conditions
        for field in char_fields:
            domain.append((field, 'ilike', search_term))
        
        return domain
 
    def global_search(self):
        search_term = self.name
        self.search_results_partners = [(5, 0, 0)]
        self.search_results_employees = [(5, 0, 0)]
        self.search_results_account_invoices = [(5, 0, 0)]
        self.search_results_account_payments = [(5, 0, 0)]
        self.search_results_inventory_product_varients = [(5, 0, 0)]
        self.search_results_inventory_products = [(5, 0, 0)]
        self.search_results_inventory_transfers = [(5, 0, 0)]
        self.search_results_purchase = [(5, 0, 0)]
        self.search_results_manufacturing_orders = [(5, 0, 0)]
        self.search_results_sale_orders = [(5, 0, 0)]
        
        if search_term == False:
            return
        
        for model in self.search_models:
            try:
                domain = self.get_domain_by_model_name(model, search_term)
                if model not in self.env:
                    print(f"'{model}' model does not exist")
                    return
                db = self.env[model]
                records = db.search(domain)
                self.get_data_by_model_name(model, records)
            except:
                print(f"Error in '{model}'")
