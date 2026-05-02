
"""Support for the Xiaomi device tracking."""
import logging


from homeassistant.components.device_tracker.config_entry import TrackerEntity
from homeassistant.const import (
    ATTR_BATTERY_LEVEL,
    ATTR_GPS_ACCURACY,
    ATTR_LATITUDE,
    ATTR_LONGITUDE,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import device_registry
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.restore_state import RestoreEntity

from homeassistant.helpers.entity import Entity

from .const import (
    DOMAIN,
    COORDINATOR,
    SIGNAL_STATE_UPDATED
)


_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, config_entry, async_add_entities):
    """Configure a dispatcher connection based on a config entry."""

    coordinator = hass.data[DOMAIN][config_entry.entry_id][COORDINATOR]
    devices = []
    for i in range(len(coordinator.data)):
        devices.append(XiaomiDeviceEntity(hass, coordinator, i))
        # _LOGGER.debug("device is : %s", i)
    async_add_entities(devices, True)

class XiaomiDeviceEntity(TrackerEntity, RestoreEntity, Entity):
    """Represent a tracked device."""

    def __init__(self, hass, coordinator, vin) -> None:
        """Set up device entity."""
        self._hass = hass
        self._vin = vin
        self.coordinator = coordinator
        self._unique_id = coordinator.data[vin].get("did",
            coordinator.data[vin].get("imei", ""))
        self._model = coordinator.data[vin].get("model", "unknown")
        self._owner_name = coordinator.data[vin].get("owner_name", "")
        self._is_family = coordinator.data[vin].get("is_family", False)
        self._icon = "mdi:cellphone-android"
        self.sw_version = coordinator.data[vin].get("version", "")
        # Show family owner name in entity name if available
        if self._owner_name:
            self._name = self._owner_name
        else:
            self._name = self._model

    async def async_update(self):
        """Update Colorfulclouds entity."""   
        _LOGGER.debug("async_update")
        await self.coordinator.async_request_refresh()
    async def async_added_to_hass(self):
        """Subscribe for update from the hub"""

        _LOGGER.debug("device_tracker_unique_id: %s", self._unique_id)

        async def async_update_state():
            """Update sensor state."""
            await self.async_update_ha_state(True)

        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )
        
    @property
    def battery_level(self):
        """Return battery value of the device."""
        return self.coordinator.data[self._vin].get("device_power", 0)

    @property
    def device_state_attributes(self):
        """Return device specific attributes."""
        data = self.coordinator.data[self._vin]
        attrs = {
            "last_update": data.get("device_location_update_time", ""),
            "coordinate_type": data.get("coordinate_type", ""),
            "device_phone": data.get("device_phone", ""),
            "imei": data.get("did", data.get("imei", "")),
            "model": data.get("model", ""),
        }
        if data.get("is_family"):
            attrs["owner_name"] = data.get("owner_name", "")
            attrs["is_family"] = True
        return attrs

    @property
    def latitude(self):
        """Return latitude value of the device."""
        return self.coordinator.data[self._vin].get("device_lat", None)

    @property
    def longitude(self):
        """Return longitude value of the device."""
        return self.coordinator.data[self._vin].get("device_lon", None)

    @property
    def location_accuracy(self):
        """Return the gps accuracy of the device."""
        return self.coordinator.data[self._vin].get("device_accuracy", 0)

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return self._icon

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def unique_id(self):
        """Return the unique ID."""
        return self._unique_id
    @property
    def device_info(self):
        """Return the device info."""
        return {
            "identifiers": {(DOMAIN, self._unique_id)},
            "name": self._name,
            "manufacturer": "Xiaomi",
            "entry_type": "service",
            "sw_version": self.sw_version,
            "model": self._name
        }

    @property
    def should_poll(self):
        """Return the polling requirement of the entity."""
        return False

    @property
    def source_type(self):
        """Return the source type, eg gps or router, of the device."""
        return 'gps'

        

