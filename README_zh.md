# Xiaomi Cloud Location for Home Assistant

通过小米云服务"查找设备"追踪小米手机及家庭成员设备。

## 功能

- **多设备追踪**：一个账号覆盖个人及家庭组全部设备
- **家庭成员昵称**：实体名称显示成员称呼而非机型代号
- **WGS-84 坐标**：GCJ-02 坐标系自动修正，地图定位准确
- **HA 2026.x + Python 3.14**：完整兼容最新 Home Assistant
- **服务调用**：`xiaomi_cloud.find`、`xiaomi_cloud.noise`、`xiaomi_cloud.lost`、`xiaomi_cloud.clipboard`

## 安装

### HACS 安装（推荐）

[![通过 HACS 添加仓库](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=MarshuMax&repository=xiaomi-cloud-location&category=integration)

手动步骤：
1. HACS → 集成 → 右上角 ⋮ → 自定义仓库
2. URL：`https://github.com/MarshuMax/xiaomi-cloud-location`
3. 类别：Integration

### 手动安装

将 `custom_components/xiaomi_cloud/` 复制到 Home Assistant 的 `config/custom_components/` 目录。

## 配置

1. 设置 → 设备与服务 → 添加集成 → 搜索 **Xiaomi Cloud**
2. 输入小米账号（手机号或小米 ID）和密码
3. 用同账号登录 [i.mi.com/find](https://i.mi.com/find) 确认能看到设备（包括"家庭成员"标签页）

添加后，设备追踪实体会显示为 `device_tracker.xxx`。家庭成员设备会显示昵称。

## 配置选项

| 选项 | 默认值 | 说明 |
|--------|---------|-------------|
| 位置更新时间间隔 | 60 分钟 | 位置拉取频率 |
| 坐标体系 | original | 坐标类型（baidu/google/original） |

## 常见问题

### 地图定位不准？

插件已自动将 GCJ-02 坐标转为 WGS-84，精度取决于手机 GPS 信号。如果偏差仍然较大，可能是手机在室内或地下室。

### 找不到家庭成员的设备？

确保该账号在 [i.mi.com/find](https://i.mi.com/find) 的"家庭成员"标签页里能看到目标设备。另外确认家庭成员的手机上已开启"查找设备"功能。

### 定位长时间不更新？

默认扫描间隔是 60 分钟。如果需要更频繁的更新，在配置选项中调低间隔值（最低 60 秒）。注意频繁定位会增加手机耗电。

维护者：[@MarshuMax](https://github.com/MarshuMax)
