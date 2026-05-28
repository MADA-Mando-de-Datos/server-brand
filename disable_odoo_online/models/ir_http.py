from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        session_data = super().session_info()
        show_account_str = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("disable_odoo_online.show_account", "True")
        )
        session_data["disable_odoo_online_show_account"] = show_account_str != "False"
        return session_data
