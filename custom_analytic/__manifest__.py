# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#############################################################################
#
#    kobros-tech Pvt. Ltd.
#
#    Copyright (C) 2020-TODAY kobros-tech(<https://www.linkedin.com/company/kobros-tech/>).
#    Author: Mohamed Alkobrosli(<https://www.linkedin.com/in/mohamed-alkobrosly/>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': "Custom module for analytic account",
    'description': """
        Custom module for analytic account
    """,
    'author': 'Abou Sajid (Mohamed Alkobrosli)',
    'company': 'kobros-tech',
    'maintainer': 'Mohamed Moustafa Alkobrosli',
    'website': "https://www.kobros-tech.com",
    'license': "AGPL-3",
    'depends': [
        'account',
        'stock', 
        'mrp',
        'mrp_account',
    ],
    'data': [
        "views/stock_location_views.xml",
        "views/stock_move_line_views.xml",
        "views/mrp_production_views.xml",
    ],
}
