import random
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant

from .const import DOMAIN, CONF_DEVICE_ID, CONF_UNIT


def _generate_unique_device_id(hass: HomeAssistant) -> str:
    existing = {
        entry.data[CONF_DEVICE_ID]
        for entry in hass.config_entries.async_entries(DOMAIN)
        if CONF_DEVICE_ID in entry.data
    }
    while True:
        candidate = f"{random.randint(0x000001, 0xFFFFFF):06x}"
        if candidate not in existing:
            return candidate


class SomfyRtsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(
        self, user_input: dict | None = None
    ) -> config_entries.FlowResult:
        errors: dict[str, str] = {}

        if user_input is not None:
            device_id = _generate_unique_device_id(self.hass)
            await self.async_set_unique_id(device_id)
            return self.async_create_entry(
                title=user_input["name"],
                data={
                    "name": user_input["name"],
                    CONF_DEVICE_ID: device_id,
                    CONF_UNIT: "01",
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required("name"): str}),
            errors=errors,
        )
