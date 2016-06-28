# -*- coding: utf-8 -*-
{
    'name': "Módulo de productos con modificación",

    'summary': """
        Módulo de productos con nuevos campos e información específica del usuario""",

    'description': """
        Módulo y estructura para campos extras en el módulo de Productos y otras funcionalidades
        especificas por el cliente.
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