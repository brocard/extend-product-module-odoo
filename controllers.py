# -*- coding: utf-8 -*-
from openerp import http

# class ProductEdu(http.Controller):
#     @http.route('/product_edu/product_edu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_edu/product_edu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_edu.listing', {
#             'root': '/product_edu/product_edu',
#             'objects': http.request.env['product_edu.product_edu'].search([]),
#         })

#     @http.route('/product_edu/product_edu/objects/<model("product_edu.product_edu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_edu.object', {
#             'object': obj
#         })