# -*- coding: utf-8 -*-
# Part of kobros-tech. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class StockScrap(models.Model):
    _inherit = 'stock.scrap'


    def _prepare_move_values(self):
        vals = super()._prepare_move_values()

        if self.location_id.analytic_account_id:
            dict_move_line_ids = {
                'move_line_ids': [(0, 0, {
                    'product_id': self.product_id.id,
                    'product_uom_id': self.product_uom_id.id,
                    'quantity': self.scrap_qty,
                    'location_id': self.location_id.id,
                    'location_dest_id': self.scrap_location_id.id,
                    'package_id': self.package_id.id,
                    'owner_id': self.owner_id.id,
                    'lot_id': self.lot_id.id,
                    # custom
                    'analytic_distribution': self.location_id.analytic_distribution
                })],
            }
            vals['move_line_ids'] = dict_move_line_ids['move_line_ids']

        return vals

