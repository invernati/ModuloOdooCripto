# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class reparto(models.Model):
#     _name = 'reparto.reparto'
#     _description = 'reparto.reparto'

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


class empleado(models.Model):
    _name = 'reparto.empleado'
    _description = 'Define los atributos del empleado'

    # Atributos
    dniEmpleado = fields.Char(string='DNI', required=True)
    nombreEmpleado = fields.Char(string='Nombre y apellidos', required=True)
    fechaNacimiento = fields.Date(string='Fecha Nacimiento', required=True, default=fields.date.today())
    direccionEmpleado = fields.Char(string='Direccion', required=True)
    telefonoEmpleado = fields.Char(string='Telefono', required=True)
    edad = fields.Integer('Edad', compute='_getEdad')

    # Relacion de tablas
    vehiculo_ids = fields.Many2many('reparto.vehiculo', string='Vehiculo')




    def name_get(self):
        listaEmpleado = []
        for empleado in self:
            listaEmpleado.append((empleado.id, empleado.nombreEmpleado))
        return listaEmpleado

    @api.depends('fechaNacimiento')
    def _getEdad(self):
        hoy = date.today()
        for empleado in self:
            empleado.edad = relativedelta(hoy, empleado.fechaNacimiento).years

    @api.constrains('fechaNacimiento')
    def _checkEdad(self):
        for empleado in self:
            if (empleado.edad < 18):
                raise exceptions.ValidationError("El empleado no puede ser menor de edad")

    @api.constrains('dniCliente')
    def _checkDNI(self):
        for empleado in self:
            if (len(empleado.dniCliente) > 9):
                raise exceptions.ValidationError("El DNI no puede tener mas 9 caracteres")
            if (len(empleado.dniCliente) < 9):
                raise exceptions.ValidationError("El DNI no puede tener menos 9 caracteres")

class vehiculo(models.Model):
    _name = 'reparto.vehiculo'
    _description = 'Define los atributos del vehiculo'

    # Atributos
    idVehiculo = fields.Integer(string='id', required=True)
    nombreVehiculo = fields.Char(string='Nombre Vehiculo', required=True)
    matriculaVehiculo = fields.Char(string='Matricula', required=True)
    modeloVehiculo = fields.Char(string='Modelo', required=True)
    tipoVehiculo = fields.Selection(string='Tipo Vehiculo', selection=[('f','Coche'),('b','Furgoneta'), ('c','Coche')], help='Red para la moneda')


    #Relacion entre tablas
    empleado_ids = fields.Many2many('reparto.empleado', string='Empleado')


    # Relacion entre modulos
    moneda_ids = fields.Many2one('comprador.moneda', string='Moneda')



    def name_get(self):
        listaVehiculos = []
        for vehiculo in self:
            listaVehiculos.append((vehiculo.id, vehiculo.nombreVehiculo))
        return listaVehiculos