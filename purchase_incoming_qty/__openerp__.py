# coding: utf-8
###############################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://www.vauxoo.com>).
#    All Rights Reserved
###############################################################################
#    Credits:
#    Coded by: Katherine Zaoral <kathy@vauxoo.com>
#    Planified by: Nhomar Hernandez <nhomar@vauxoo.com>
#    Audited by: Nhomar Hernandez <nhomar@vauxoo.com>
###############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

{
    "name": "Purchase Incoming Quantity",
    "summary": "Differentiate the Purchase Virtual Incoming Inventory",
    "version": "8.0.0.1.6",
    "author": "Vauxoo",
    "license": "AGPL-3",
    "website": "http://www.vauxoo.com/",
    "category": "Inventory Control",
    "depends": [
        "stock",
    ],
    "data": [
        "view/product_view.xml",
    ],
    "demo": [],
    "test": [],
    "qweb": [],
    "js": [],
    "css": [],
    "installable": False,
}
