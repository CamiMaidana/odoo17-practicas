# -*- coding: utf-8 -*-
{
    'name': "mod_prueba",

    'summary': "Modulo de prueba",

    'description': """Modulo de prueba
    """,

    'author': "Cami Maidana",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'models/models.xml',
        'security/ir.model.access.csv',
        'views/vistamodprueba.xml',
        'views/templates.xml',
    ],
    'demo': [
    'demo/demo.xml',
    ],

    # only loaded in demonstration mode
    'installable': True,
    'application': True,
}

