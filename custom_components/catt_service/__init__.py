from __future__ import annotations

import logging

from catt.controllers import setup_cast
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry, device_registry

from .const import DOMAIN


_LOGGER = logging.getLogger(__name__)

def setup(hass, config):

    def handle_cast_site(call):
        entity_id = call.data.get("entity_id")
        ent_reg = entity_registry.async_get(hass)
        dev_reg = device_registry.async_get(hass)
        entity = ent_reg.async_get(entity_id)
        _LOGGER.debug(f'entity {entity}')
        device_id = entity.device_id
        device = dev_reg.async_get(device_id)
        _LOGGER.debug(f'device {device}')

        url = call.data.get("url")

        cst = setup_cast(
            device.name,
        )
        cst.kill()

        cst = setup_cast(
            device.name,
            controller="dashcast",
            action="load_url",
            prep="app",
        )
        cst.load_url(url)
        return True


    hass.services.register(DOMAIN, "cast_site", handle_cast_site)
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    return True
