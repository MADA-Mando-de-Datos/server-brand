from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        session_data = super().session_info()
        # Read hide_account parameter - default is False (show menu)
        hide_account_str = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("disable_odoo_online.hide_account", "False")
        )
        # Convert string "True"/"False" to boolean
        session_data["disable_odoo_online_hide_account"] = hide_account_str == "True"
        return session_data
