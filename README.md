# Xiaomi Cloud Location for Home Assistant

[中文说明](README_zh.md)

Track Xiaomi phones and family members' devices via Xiaomi Cloud Find Device API.

## Features

- **Multiple device tracking** — personal and family group devices in one account
- **Family member nicknames** — entity names show the person's name, not model number
- **WGS-84 coordinates** — proper GCJ-02 conversion for accurate map display
- **HA 2026.x + Python 3.14** — fully compatible with latest Home Assistant
- **Services** — `xiaomi_cloud.find`, `xiaomi_cloud.noise`, `xiaomi_cloud.lost`, `xiaomi_cloud.clipboard`

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

Maintained by [@MarshuMax](https://github.com/MarshuMax)
