# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class comprador(models.Model):
#     _name = 'comprador.comprador'
#     _description = 'comprador.comprador'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import models, fields, exceptions, api


class cliente(models.Model):
    _name = 'comprador.cliente'
    _description = 'Define los atributos del cliente'

    # Atributos
    dniCliente = fields.Char(string='DNI', required=True)
    nombreCliente = fields.Char(string='Nombre y apellidos', required=True)
    fechaNacimiento = fields.Date(string='Fecha Nacimiento', required=True, default=fields.date.today())
    edad = fields.Integer('Edad', compute='_getEdad')

    # Relacion de tablas
    moneda_ids = fields.Many2many('comprador.moneda', string='Moneda')
    empleado_ids = fields.Many2one('reparto.empleado', string='Empleado')


    def name_get(self):
        listaCliente = []
        for cliente in self:
            listaCliente.append((cliente.id, cliente.nombreCliente))
        return listaCliente

    @api.depends('fechaNacimiento')
    def _getEdad(self):
        hoy = date.today()
        for cliente in self:
            cliente.edad = relativedelta(hoy, cliente.fechaNacimiento).years

    @api.constrains('fechaNacimiento')
    def _checkEdad(self):
        for cliente in self:
            if (cliente.edad < 18):
                raise exceptions.ValidationError("El cliente no puede ser menor de edad")

    @api.constrains('dniCliente')
    def _checkDNI(self):
        for cliente in self:
            if (len(cliente.dniCliente) > 9):
                raise exceptions.ValidationError("El DNI no puede tener mas 9 caracteres")
            if (len(cliente.dniCliente) < 9):
                raise exceptions.ValidationError("El DNI no puede tener menos 9 caracteres")

class moneda(models.Model):
    _name = 'comprador.moneda'
    _description = 'Define los atributos de la moneda'

    # Atributos
    idMoneda = fields.Integer(string='id', required=True)
    nombreMoneda = fields.Char(string='Nombre Moneda', required=True)
    fechaMoneda = fields.Date(string='Fecha Creacion', required=True, default=fields.date.today())
    precioMoneda = fields.Integer(string='Precio', required=True)
    cantidadMoneda = fields.Integer(string='Cantidad', required=True)
    redMoneda = fields.Selection(string='Red de la Moneda', selection=[('f','ERZ20'),('b','Bep2'), ('c','Arbitum One')], help='Red para la moneda')


    #Relacion entre tablas
    cliente_ids = fields.Many2one('comprador.cliente', string='Cliente')

    # Relacion entre modulos



    def name_get(self):
        listaMonedas = []
        for moneda in self:
            listaMonedas.append((moneda.id, moneda.nombreMoneda))
        return listaMonedas