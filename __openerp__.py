# -*- coding: utf-8 -*-
{
    'name': "Extender modulo de productos",

    'summary': """
        Modulo de estructura y campos extras para
        productos """,

    'description': """
        Módulo y estructura para campos extras en el moduoo de Productos
    """,

    'author': "YBD <brocard@gmail.com>",
    'website': "http://damecode.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}