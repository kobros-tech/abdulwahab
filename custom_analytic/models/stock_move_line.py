# -*- coding: utf-8 -*-
# Part of kobros-tech. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockMoveLine(models.Model):
    _name = "stock.move.line"
    _inherit = ['stock.move.line', 'analytic.mixin']

    analytic_distribution = fields.Json()

