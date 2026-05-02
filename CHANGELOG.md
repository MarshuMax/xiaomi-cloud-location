# Changelog

## v1.3.0 (2026-05-02)

### Added
- **Family group support**: Now tracks family members' devices via v3 Find Device API (`/find/v3/device/status/list`)
- Entity names show family member nicknames from `familyInfo`

### Fixed
- **Xiaomi v3 API**: Migrated from deprecated `/find/device/full/status` to `/find/v3/device/status/list`
- **WGS-84 coordinates**: Apply GCJ2WGS conversion on autonavi (GCJ-02) coordinates for accurate map positioning
- **HA 2026.x**: `Config` import removed from `homeassistant.core`
- **HA 2026.x**: `HomeAssistantType` → `HomeAssistant`
- **HA 2026.x**: `SOURCE_TYPE_GPS` → string literal `'gps'`
- **HA 2026.x**: `async_forward_entry_setup` → `async_forward_entry_setups` with list parameter
- **HA 2026.x**: `ConfigFlow` → `OptionsFlow` for options handler
- **HA 2026.x**: `entry_type: "device"` → `"service"`
- **Python 3.14**: `async_timeout.timeout(loop=)` → `async_timeout.timeout()`
- **API format**: Handle `gpsInfo` (single dict) replacing `gpsInfoExtra` (array)
- **Resilience**: Use `.get()` with defaults for all dict access in device_tracker

## v1.2.7

- Fix sign acquisition failure caused by HA upgrade

## v1.2.5

- Fix configuration page login issue
- Add version to manifest.json
