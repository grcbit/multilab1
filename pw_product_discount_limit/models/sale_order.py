# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('discount')
    def onchange_discount(self):
        discount_limit = self.product_id.pw_discount_limit or self.product_id.categ_id.pw_discount_limit
        has_group = self.env.user.has_group('pw_product_discount_limit.group_pw_allow_discount')
        if not has_group and self.product_id and discount_limit > 0 and discount_limit < self.discount:
            raise UserError(_('You cannot apply discount more than (%d %%) on this product, Please contact your administrator !' % discount_limit))
