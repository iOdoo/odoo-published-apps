# -*- coding: utf-8 -*-
{
    'name': "Discount Control on POS",

    'summary': """
         POS Discount Control | 
         Every POS can control discount | 
         Discount Control | 
         """,
    'sequence': -10,
    'description': """
         POS Discount Control | 
         Every POS can control discount | 
         Discount Control | 
         Discount Control on POS|
         Salesman/ Cashier can't sale with discount.
    """,
    'author': "iBOS Limited",
    'website': "http://ibos.io",
    'category': 'Point Of Sale',
    'version': '13.0.1.0.0',
    'depends': ['base', 'point_of_sale'],
    # always loaded
    'data': [
        'views/assets.xml',
        'views/pos_config.xml',
    ],
    'qweb': [],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
