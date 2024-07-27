# -*- coding: utf-8 -*-
{
    'name': "todo",

    'summary': """
        Sample Bitbriks' todo app to demonstrate how to use React with Odoo.""",

    'description': """
        Build Odoo's standalone UI with Reactjs.
    """,

    'author': "Bitbriks",
    'website': "https://bitbriks.com",
    'installable': True,
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
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
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        ####################################################
        ##      Javascript files to build React app       ##
        ####################################################
        'todo.assets': [
            'todo/static/src/index.js',
            'todo/static/src/components/*.js',
            'todo/static/src/index.css',
            'todo/static/src/components/*.css'
        ]
    }
}
