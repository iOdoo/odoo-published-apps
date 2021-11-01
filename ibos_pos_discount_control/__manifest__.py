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
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
