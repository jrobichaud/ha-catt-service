from homeassistant import config_entries
from .const import DOMAIN


class FlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input):
        if self._async_current_entries():
            return self.async_abort(reason="already_configured")
        return self.async_create_entry(title="CATT Service", data={})
