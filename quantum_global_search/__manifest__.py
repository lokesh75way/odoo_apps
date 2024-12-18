# -*- coding: utf-8 -*-
{
    'name': "Global Search",

    'summary': "Global Search",

    'description': """
    """,

    'author': "75Way",
    'website': "https://www.75way.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/global_search_views.xml',
        'views/global_search_menuitem.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'quantum_global_search/static/src/js/global_search.js'
        ],
        'web.assets_common': [
            'quantum_global_search/static/src/css/styles.css',  # Path to your CSS file
        ],
    }
}

