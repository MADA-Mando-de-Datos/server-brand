from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    disable_odoo_online_hide_account = fields.Boolean(
        string="Hide 'My Odoo.com account' menu",
        config_parameter="disable_odoo_online.hide_account",
        default=False,
        help="Check to hide the My Odoo.com account entry in the user dropdown menu",
    )

    def set_values(self):
        """Force persistence of the parameter even when False."""
        super().set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "disable_odoo_online.hide_account",
            str(bool(self.disable_odoo_online_hide_account)),
        )
