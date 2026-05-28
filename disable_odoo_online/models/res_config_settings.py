from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    disable_odoo_online_show_account = fields.Boolean(
        string="Show 'My Odoo.com account' menu",
        config_parameter="disable_odoo_online.show_account",
        default=True,
        help="Uncheck to hide the My Odoo.com account entry in the user dropdown menu",
)
    def set_values(self):
        """Force persistence of the parameter when unchecked."""
        super().set_values()
        # Only save if explicitly changed (not default)
        if not self.disable_odoo_online_show_account:
            self.env["ir.config_parameter"].sudo().set_param(
                "disable_odoo_online.show_account",
                "False",
            )
