# -*- coding: utf-8 -*-
###################################################################################
#
#    iBOS Limited.
#    Copyright (C) 2021-TODAY iBOS Limited (<https://www.ibos.io>).
#    Author: Kamrul Hasan (<https://www.ibos.io>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

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
