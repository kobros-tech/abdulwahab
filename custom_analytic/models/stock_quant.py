# -*- coding: utf-8 -*-
# Part of kobros-tech. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class StockQuant(models.Model):
    _inherit = 'stock.quant'


    def _get_inventory_move_values(self, qty, location_id, location_dest_id, package_id=False, package_dest_id=False):
        vals = super()._get_inventory_move_values(qty, location_id, location_dest_id, package_id=False, package_dest_id=False)

        if self.location_id.analytic_account_id:
            dict_move_line_ids = {
                'move_line_ids': [(0, 0, {
                    'product_id': self.product_id.id,
                    'product_uom_id': self.product_uom_id.id,
                    'quantity': qty,
                    'location_id': location_id.id,
                    'location_dest_id': location_dest_id.id,
                    'company_id': self.company_id.id or self.env.company.id,
                    'lot_id': self.lot_id.id,
                    'package_id': package_id.id if package_id else False,
                    'result_package_id': package_dest_id.id if package_dest_id else False,
                    'owner_id': self.owner_id.id,
                    # custom
                    'analytic_distribution': self.location_id.analytic_distribution
                })],
            }
            vals['move_line_ids'] = dict_move_line_ids['move_line_ids']

        return vals

