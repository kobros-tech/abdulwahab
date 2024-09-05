# -*- coding: utf-8 -*-
# Part of kobros-tech. See LICENSE file for full copyright and licensing details.

import json
from odoo import fields, models, api, _


class StockLocation(models.Model):
    
    _name = "stock.location"
    _inherit = ['stock.location', 'analytic.mixin']
    

    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string="Analytic Account",
        copy=False, check_company=True,  # Unrequired company
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")


    @api.depends_context('company')
    @api.depends('analytic_account_id')
    def _compute_analytic_distribution(self):

        for record in self:
            analytic_account_id = record.analytic_account_id.id
            record.analytic_distribution = {analytic_account_id: 100}

    
    