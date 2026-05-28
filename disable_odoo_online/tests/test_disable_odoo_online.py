# Copyright 2024 level4 (https://level4.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestDisableOdooOnline(common.TransactionCase):
    def test_session_info_show_account_default(self):
        """By default, show_account should be True (menu visible)."""
        session_info = self.env["ir.http"].session_info()
        self.assertTrue(session_info.get("disable_odoo_online_show_account", True))

    def test_session_info_hide_account_enabled(self):
        """When hide_account is True, menu should be hidden."""
        self.env["ir.config_parameter"].sudo().set_param(
            "disable_odoo_online.hide_account", "True"
        )
        session_info = self.env["ir.http"].session_info()
        self.assertTrue(session_info["disable_odoo_online_hide_account"])

    def test_session_info_hide_account_disabled(self):
        """When hide_account is False, menu should be visible."""
        self.env["ir.config_parameter"].sudo().set_param(
            "disable_odoo_online.hide_account", "False"
        )
        session_info = self.env["ir.http"].session_info()
        self.assertFalse(session_info["disable_odoo_online_hide_account"])
