# ha-catt-service

This is an alternative to [AlexxIT/DashCast](https://github.com/AlexxIT/DashCast) using [Cast All The Things](https://github.com/skorokithakis/catt/)

It basically wraps [catt cast_site \<url\>](https://github.com/skorokithakis/catt), and also stops any other cast in the process.

## Installation

1. Add HACS repository

    [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=jrobichaud&repository=ha-catt-service&category=integration)

2. Restart Home assistant

3. Add integration

    [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=catt_service)

## Usage

```yaml
service: catt_service.cast_site
data:
  device_id: media_player.my_chromecast
  url: https://en.wikipedia.org/wiki/Rickrolling
```
