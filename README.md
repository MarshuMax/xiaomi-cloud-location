# Xiaomi Cloud Location for Home Assistant

Home Assistant integration for Xiaomi Cloud device tracking, including **family group positioning**.

Fork of [fineemb/xiaomi-cloud](https://github.com/fineemb/xiaomi-cloud) with full HA 2026.x, Python 3.14, and Xiaomi v3 API compatibility.

## What's new in v1.3.0

- **Family group support**: Track all family members' devices with one account (no need to add each family member's credentials)
- **v3 Find Device API**: Uses Xiaomi's latest `/find/v3/device/status/list` endpoint
- **WGS-84 coordinates**: Proper GCJ-02 → WGS-84 conversion for accurate map display
- **HA 2026.x compatible**: All breaking changes fixed (Config, HomeAssistantType, SOURCE_TYPE_GPS, etc.)
- **Python 3.14 compatible**: `async_timeout` loop parameter removed

## Features

- Track Xiaomi/Redmi phones via Xiaomi Cloud Find Device API
- **Family member device tracking** - one account covers the whole family
- Entity names show family member nicknames
- Device location with WGS-84 coordinates
- Services: `xiaomi_cloud.find`, `xiaomi_cloud.noise`, `xiaomi_cloud.lost`, `xiaomi_cloud.clipboard`

## Installation

### Via HACS

[![Add repository to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=MarshuMax&repository=xiaomi-cloud-location&category=integration)

Or manually:
1. HACS → Integrations → ⋮ → Custom repositories
2. URL: `https://github.com/MarshuMax/xiaomi-cloud-location`
3. Category: Integration

### Manual

Copy `custom_components/xiaomi_cloud/` to your Home Assistant `config/custom_components/` directory.

## Setup

1. Settings → Devices & Services → Add Integration → **Xiaomi Cloud**
2. Enter your Xiaomi account credentials (phone number or Xiaomi ID)
3. Verify the account shows your devices at [i.mi.com/find](https://i.mi.com/find) — including family tab

After setup, device trackers appear as `device_tracker.xxx` entities. Family members' devices show their nickname as the entity name.

## Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| Scan Interval | 60 min | How often to fetch location |
| Coordinate Type | original | Location coordinate system |

## Credits

Original: [@fineemb](https://github.com/fineemb)  
Maintainer: [@MarshuMax](https://github.com/MarshuMax)
