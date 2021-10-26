# -*- coding: utf-8 -*-
{
    'name': "Partner (Customer/Supplier) Approval",

    'summary': """
         partner approval 
         Customer approval 
         Access to user Role
         partner & Customer create control
         """,
    'sequence': -36,
    'description': """
        Partner Approval module is made to allow you to approve or reject contacts only by the
                            contact manager.
    """,
    'author': "iBOS Limited",
    'website': "https://ibos.io",
    'category': 'Tools',
    'version': '13.0.1.0.0',
    'depends': ['base', 'contacts', 'purchase', 'point_of_sale'],
    # always loaded
    'data': [
        'security/security.xml',
        'views/assets.xml',
        'views/res_partner_approval.xml',
        'views/purchase_order_approval.xml',
        'views/pos_config.xml',
    ],
    'qweb': [],
    'demo': [],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
