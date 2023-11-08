# ha-catt-service

This is an alternative to [AlexxIT/DashCast](https://github.com/AlexxIT/DashCast) using [Cast All The Things](https://github.com/skorokithakis/catt/)

It basically wraps [catt cast_site \<url\>](https://github.com/skorokithakis/catt), and also stops any other cast in the process.

## Usage

```yaml
service: catt_service.cast_site
data:
  entity_id: media_player.my_chromecast
  url: https://example.com
```
