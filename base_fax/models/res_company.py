# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'
    fax_adapter_ids = fields.One2many(
        string='Fax Adapters',
        comodel_name='fax.adapter',
        inverse_name='company_id',
        help='Company that adapter is associated with',
    )
