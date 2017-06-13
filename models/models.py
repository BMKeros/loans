# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Loan(models.Model):
    _name = "loan.loan"

    def _get_default_date(self):
        return fields.Date.from_string(fields.Date.today())

    code = fields.Char(string="Loan Code")
    description = fields.Char(string="Loan Description")
    amount = fields.Monetary(string="Loan Amount")
    application_date = fields.Date(string="Application Date")
    approval_date = fields.Date(string="Approval Date", default=lambda self: self._get_default_date())


class LoanPeriod(models.Model):
    _name = "loan.loan_period"

    name = fields.Char(string="Period Name")


class LoanType(models.Model):
    _name = "loan.loan_type"

    code = fields.Char(string="Code")
    name = fields.Char(string="Name")



class LoanEmployee(models.Model):
    _name = "loan.loan_employee"

    _
    # class local_addons/loans(models.Model):
    #     _name = 'local_addons/loans.local_addons/loans'

    #     name = fields.Char()
    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         self.value2 = float(self.value) / 100
