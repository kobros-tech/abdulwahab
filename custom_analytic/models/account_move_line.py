# -*- coding: utf-8 -*-
# Part of kobros-tech. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, Command, _
from odoo.tools import frozendict, format_date, float_compare, Query


class AccountMoveLine(models.Model):
    _name = "account.move.line"
    _inherit = ['account.move.line', 'analytic.mixin']

    
    @api.depends('account_id', 'partner_id', 'product_id')
    def _compute_analytic_distribution(self):
        

        cache = {}
        for line in self:
            if line.display_type == 'product' or not line.move_id.is_invoice(include_receipts=True):
                arguments = frozendict({
                    "product_id": line.product_id.id,
                    "product_categ_id": line.product_id.categ_id.id,
                    "partner_id": line.partner_id.id,
                    "partner_category_id": line.partner_id.category_id.ids,
                    "account_prefix": line.account_id.code,
                    "company_id": line.company_id.id,
                })
                if arguments not in cache:
                    cache[arguments] = self.env['account.analytic.distribution.model']._get_distribution(arguments)
                line.analytic_distribution = cache[arguments] or line.analytic_distribution
            
            
            # custom
            if line.move_id.stock_move_id:
                for stock_move_line in line.move_id.stock_move_id.move_line_ids:
                    if stock_move_line.analytic_distribution != False:
                        line.analytic_distribution = stock_move_line.analytic_distribution

            