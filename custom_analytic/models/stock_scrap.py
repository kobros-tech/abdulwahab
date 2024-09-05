# -*- coding: utf-8 -*-
# Part of kobros-tech. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class StockScrap(models.Model):
    _inherit = 'stock.scrap'


    def _prepare_move_values(self):
        vals = super()._prepare_move_values()

        if self.location_id:
            vals = {
                'name': self.name,
                'origin': self.origin or self.picking_id.name or self.name,
                'company_id': self.company_id.id,
                'product_id': self.product_id.id,
                'product_uom': self.product_uom_id.id,
                'state': 'draft',
                'product_uom_qty': self.scrap_qty,
                'location_id': self.location_id.id,
                'scrapped': True,
                'scrap_id': self.id,
                'location_dest_id': self.scrap_location_id.id,
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
                # 'restrict_partner_id': self.owner_id.id,
                'picked': True,
                'picking_id': self.picking_id.id
            }

        return vals

