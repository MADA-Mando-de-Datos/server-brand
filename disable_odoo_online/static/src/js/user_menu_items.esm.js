import { registry } from "@web/core/registry";
import { session } from "@web/session";
import "@web/webclient/user_menu/user_menu_items";

const userMenuRegistry = registry.category("user_menuitems");

userMenuRegistry.remove("documentation");
userMenuRegistry.remove("support");

// Hide odoo_account menu if show_account is False (unchecked)
if (!session.disable_odoo_online_hide_account) {
    userMenuRegistry.remove("odoo_account");
}
