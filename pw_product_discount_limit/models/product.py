# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    pw_discount_limit = fields.Float(string="Discount Limit(%)")


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pw_discount_limit = fields.Float(string="Discount Limit(%)")
