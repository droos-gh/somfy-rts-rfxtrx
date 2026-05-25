from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, CONF_DEVICE_ID, CONF_UNIT, CMD_PROGRAM, CMD_MY
from .cover import _build_rfy_packet


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        SomfyRtsProgramButton(hass, entry, data),
        SomfyRtsMyButton(hass, entry, data),
    ])


class _SomfyRtsButton(ButtonEntity):
    _attr_has_entity_name = True

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, data: dict) -> None:
        self.hass = hass
        self._data = data
        self._device_uid = f"{data[CONF_DEVICE_ID]}_{data[CONF_UNIT]}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self._device_uid)},
            name=data["name"],
            manufacturer="Somfy",
            model="RTS",
        )

    async def _send(self, cmd: int) -> None:
        packet = _build_rfy_packet(self._data[CONF_DEVICE_ID], self._data[CONF_UNIT], cmd)
        await self.hass.services.async_call("rfxtrx", "send", {"event": packet})


class SomfyRtsProgramButton(_SomfyRtsButton):
    _attr_name = "Programme"
    _attr_icon = "mdi:remote"

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, data: dict) -> None:
        super().__init__(hass, entry, data)
        self._attr_unique_id = f"{self._device_uid}_program"

    async def async_press(self) -> None:
        await self._send(CMD_PROGRAM)


class SomfyRtsMyButton(_SomfyRtsButton):
    _attr_name = "My"
    _attr_icon = "mdi:heart-circle-outline"

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, data: dict) -> None:
        super().__init__(hass, entry, data)
        self._attr_unique_id = f"{self._device_uid}_my"

    async def async_press(self) -> None:
        await self._send(CMD_MY)
