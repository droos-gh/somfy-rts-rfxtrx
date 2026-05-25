from homeassistant.components.cover import CoverEntity, CoverEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, CONF_DEVICE_ID, CONF_UNIT, CMD_STOP, CMD_UP, CMD_DOWN


def _build_rfy_packet(device_id: str, unit: str, cmd: int) -> str:
    # RFY packet: 0C 1A 00 [seq] [id1][id2][id3] [unit] [cmd] [rpt] 00 00 00
    return f"0c1a0000{device_id}{unit}{cmd:02x}01000000"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([SomfyRtsCover(hass, entry, data)])


class SomfyRtsCover(CoverEntity):
    _attr_has_entity_name = True
    _attr_name = None
    _attr_is_closed = None  # RTS is one-way, state is always unknown
    _attr_supported_features = (
        CoverEntityFeature.OPEN | CoverEntityFeature.CLOSE | CoverEntityFeature.STOP
    )

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, data: dict) -> None:
        self.hass = hass
        self._data = data
        self._device_uid = f"{data[CONF_DEVICE_ID]}_{data[CONF_UNIT]}"
        self._attr_unique_id = self._device_uid
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self._device_uid)},
            name=data["name"],
            manufacturer="Somfy",
            model="RTS",
        )

    async def _send(self, cmd: int) -> None:
        packet = _build_rfy_packet(self._data[CONF_DEVICE_ID], self._data[CONF_UNIT], cmd)
        await self.hass.services.async_call("rfxtrx", "send", {"event": packet})

    async def async_open_cover(self, **kwargs) -> None:
        await self._send(CMD_UP)

    async def async_close_cover(self, **kwargs) -> None:
        await self._send(CMD_DOWN)

    async def async_stop_cover(self, **kwargs) -> None:
        await self._send(CMD_STOP)
