# -*- coding: utf-8 -*-
{
    'name': "Expenditure",

    'summary': """
        Management Expenditure """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Peter Dinh",
    'website': "https://github.com/peter-dinh",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        #'controllers/controllers.py',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}