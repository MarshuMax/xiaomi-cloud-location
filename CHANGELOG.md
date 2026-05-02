# Changelog

## v1.3.0 (2026-05-02)

### Added
- **Family group support**: track family members' devices via Xiaomi v3 API (`/find/v3/device/status/list`)
- Entity names show family member nicknames from `familyInfo`
- `owner_name` and `is_family` attributes on device tracker entities

### Fixed
- **Xiaomi v3 API**: migrate to `/find/v3/device/status/list` for all device + family data
- **WGS-84 coordinates**: apply GCJ2WGS conversion on autonavi (GCJ-02) coordinates
- **HA 2026.x**: `Config` import removed from `homeassistant.core`
- **HA 2026.x**: `HomeAssistantType` → `HomeAssistant`
- **HA 2026.x**: `SOURCE_TYPE_GPS` → string literal `'gps'`
- **HA 2026.x**: `async_forward_entry_setup` → `async_forward_entry_setups` with list parameter
- **HA 2026.x**: `ConfigFlow` → `OptionsFlow` for options handler
- **HA 2026.x**: `entry_type: "device"` → `"service"`
- **Python 3.14**: `async_timeout.timeout(loop=)` → `async_timeout.timeout()`
- **API format**: handle `gpsInfo` (single dict) replacing `gpsInfoExtra` (array)
- **Resilience**: use `.get()` with defaults for all dict access in device_tracker
