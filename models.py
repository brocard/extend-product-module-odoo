# -*- coding: utf-8 -*-

from openerp import models, fields, api

class res_product(models.Model):

    _inherit = "product.template"

    article = fields.Text(string="Artículo")
    supplier_list = fields.Char(string="Info Proveedores")

    standard_price_1 = fields.Float(string="Precio coste 1")
    standard_price_2 = fields.Float(string="Precio coste 2")
    standard_price_3 = fields.Float(string="Precio coste 3")

    # onchange handler
    #@api.onchange('list_price')
    #def _onchange_price(self):
        # set auto-changing field
    #    self.lst_price = self.list_price * 1.4