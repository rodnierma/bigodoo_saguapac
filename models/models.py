from odoo import models,fields

class TipoInmueble(models.Model):
    _name = 'sg.tipo.inmueble'
    _descripcion = "Tipo Inmueble"

    name = fields.Char(string="Nombre")


class Tags(models.Model):
    _name = 'sg.tag'
    _descripcion = "Etiquetas"

    name = fields.Char(string="Nombre")


class Inmuebles(models.Model):
    _name = "sg.inmueble"
    _descripcion = "Inmuebles"

    name = fields.Char("Nombre")
    street = fields.Text("Direccion")
    value = fields.Float(string="Valor de propiedad", default=0)
    currency_id = fields.Many2one("res.currency", string="Moneda")
    type = fields.Many2one("sg.tipo.inmueble", string="Tipo Inmueble")
    tag_ids = fields.Many2many("sg.tag", string="Etiquetas")
    partner_ids = fields.Many2many("res.partner", string="Interesados")
    operation = fields.Selection(selection=[("venta","Venta"),("compra","Compra"),("alquiler","Alquiler")], 
                                 string="Tipo de inmueble",default="venta")

    image = fields.Binary("Imagen")
    user_id = fields.Many2one("res.users", string="Responsable", default=lambda self:self.env.user.id)
    company_id = fields.Many2one("res.company", string="Compañía", default=lambda self:self.env.company.id)
    owner_id = fields.Many2one("res.partner", string="Propietario")
    date = fields.Date("Fecha de Alta")
    codigo_catastral = fields.Char("Codigo Catastral")



class ResParter(models.Model):
    _inherit = 'res.partner'

    inmueble_ids = fields.Many2many("sg.inmueble", string="Inmuebles")


