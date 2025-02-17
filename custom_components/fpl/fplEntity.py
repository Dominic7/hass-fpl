"""BlueprintEntity class"""
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, VERSION, ATTRIBUTION


class FplEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry, account, sensorName):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.account = account
        self.sensorName = sensorName

    @property
    def unique_id(self):
        """Return the ID of this device."""
        id = "{}{}{}".format(
            DOMAIN, self.account, self.sensorName.lower().replace(" ", "")
        )
        return id

    @property
    def name(self):
        return f"{DOMAIN.upper()} {self.account} {self.sensorName}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.account)},
            "name": f"Account {self.account}",
            "model": VERSION,
            "manufacturer": "Florida Power & Light",
        }

    def defineAttributes(self):
        return {}

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        attributes = {
            "attribution": ATTRIBUTION,
            "integration": "FPL",
        }
        attributes.update(self.defineAttributes())
        return attributes

    def getData(self, field):
        return self.coordinator.data.get(self.account).get(field)
