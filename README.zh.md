<div align="center">

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:764ba2,100:667eea&height=200&section=header&text=🔓%20俄罗斯免费VPN&fontSize=42&fontColor=ffffff&fontAlignY=20&desc=免费VPN配置%20%7C%20每6小时更新&descAlignY=58&descSize=16&descColor=aaaacc"/>
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=200&section=header&text=🔓%20俄罗斯免费VPN&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=免费VPN配置%20%7C%20每6小时更新&descAlignY=58&descSize=16&descColor=f0e6ff"/>
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=200&section=header&text=🔓%20俄罗斯免费VPN&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=免费VPN配置%20%7C%20每6小时更新&descAlignY=58&descSize=16&descColor=f0e6ff" alt="Free VPN Russia — 俄罗斯免费VPN配置 2025-2026，支持 Happ、Incy、v2rayNG"/>
</picture>

<br/>

<!-- LANG_SWITCH_START -->
<div align="center">

# [🇷🇺](README.md) &nbsp;&nbsp;&nbsp; [🇬🇧](README.en.md) &nbsp;&nbsp;&nbsp; [🇸🇦](README.ar.md) &nbsp;&nbsp;&nbsp; 🇨🇳

</div>
<!-- LANG_SWITCH_END -->

<br/><br/>

<!-- STATS_START -->
<a href="https://raw.githubusercontent.com/aviamastersgh/vpn-free-russia/main/all_configs.txt"><img src="https://img.shields.io/badge/全部配置-732-4C8BF5?style=for-the-badge&logo=server&logoColor=white" alt="All configs"/></a>
<a href="https://raw.githubusercontent.com/aviamastersgh/vpn-free-russia/main/verified_configs.txt"><img src="https://img.shields.io/badge/已验证-500-2ea44f?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Verified configs"/></a>
<a href="https://raw.githubusercontent.com/aviamastersgh/vpn-free-russia/main/ru_configs.txt"><img src="https://img.shields.io/badge/俄罗斯绕过-69-2ea44f?style=for-the-badge&logo=checkmarx&logoColor=white" alt="RU configs"/></a>
<img src="https://img.shields.io/badge/更新时间-2026_07_06_15%3A00_UTC-f97316?style=for-the-badge&logo=clockify&logoColor=white" alt="Updated"/>
<!-- STATS_END -->

<a href="https://t.me/NosokVPNBot?start=partner_8655864538"><img src="https://img.shields.io/badge/Telegram-@NosokVpnBot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram VPN 机器人"/></a>
<a href="https://github.com/aviamastersgh/vpn-free-russia"><img src="https://img.shields.io/github/stars/aviamastersgh/vpn-free-russia?style=for-the-badge&color=yellow" alt="Stars"/></a>

<br/><br/>

**VLESS · VMess · Shadowsocks · Trojan · Hysteria2 · TUIC**

*俄罗斯免费VPN配置 · 绕过俄罗斯通信监管局（РКН）封锁 · 支持 Happ、Incy、v2ray*

</div>

---

## 📑 目录

- [项目介绍](#-项目介绍)
- [三个文件——有什么区别](#-三个文件有什么区别)
- [快速连接](#-快速连接)
- [如何确定我需要哪个文件](#-如何确定我需要哪个文件)
- [客户端使用说明](#-如何将配置添加到客户端--分步说明)
- [支持的客户端](#-支持的客户端)
- [稳定VPN——专属密钥](#-稳定vpn专属密钥)
- [支持的协议](#-支持的协议)
- [常见问题](#-常见问题)
- [镜像地址](#-镜像地址如果github被封锁)
- [配置来源](#-配置来源)
- [免责声明](#️-免责声明)

---

## 💙 支持本项目
**本项目仅靠热情和捐赠维持。服务器测试、验证时间、镜像维护、加快更新——这一切都需要金钱和精力。**
如果这些配置今天帮到了你，非常欢迎你的支持 ❤️

最方便的支持方式：
- USDT (TRC-20) → ```TLkat7EH1LZ6aZB3nQ3yScJD1a9CSkYV1d```
- Solana (SOL) → ```H8dJ9wJmCzYqBjvPW5fXkA8dTFngmpvLfNvQcn2mJGdS```
- Bitcoin → ```bc1q376tjzk663f3kkrkvtgnqy2p9xat5klk5dytag```
> 即使是许多人的一点点支持，也能带来稳定的更新和新的镜像。
谢谢！🙏

也别忘了点个 ⭐ 星标，并分享给在俄罗斯需要免费VPN的人。

<a href="https://github.com/aviamastersgh/vpn-free-russia"><img src="https://img.shields.io/github/stars/aviamastersgh/vpn-free-russia?style=social" alt="Stars"/></a>

---

## 📖 项目介绍

本仓库是一个**公开免费VPN配置的聚合站点**，用于在俄罗斯境内绕过通信监管局（РКН）的封锁。

脚本每 **6 小时** 自动执行以下操作：
- 📥 从约15个公开来源下载配置
- 🔍 去除重复项
- ✅ 检测每台服务器的TCP可用性
- 📤 发布三个包含最新结果的文件

无需注册，无需账号。复制链接粘贴到客户端即可。

如果需要不依赖公共资源池的稳定连接，请参阅["稳定VPN——专属密钥"](#-稳定vpn专属密钥)一节。

---

## 📂 三个文件——有什么区别？

这是新手最常问的问题。这里给出简单的解释：

### `all_configs.txt` —— 所有找到的配置

包含从所有来源找到的**全部**配置（已去重）。其中部分可能目前无法使用——服务器可能过载、下线或被封锁。

➡️ **何时使用：** 有时间自己测试，或者标准文件无效时。

```
https://raw.githubusercontent.com/aviamastersgh/vpn-free-russia/main/all_configs.txt
```

### `verified_configs.txt` —— 仅可用的 ✅（推荐）

从全部配置池中，只筛选出在检测时刻能够建立**真实TCP连接**的服务器。

➡️ **何时使用：** 大多数情况下——这是入门的最佳选择。

```
https://raw.githubusercontent.com/aviamastersgh/vpn-free-russia/main/verified_configs.txt
```

### `ru_configs.txt` —— 绕过白名单限制 ⚠️

适用于**移动网络限制严格**的用户（Megafon、MTS、Beeline、T2、Yota 等运营商的白名单模式）。包含带俄罗斯IP地址（CIDR段）的配置，即使在运营商最严格的限制下也不会被封锁。这些配置来自可信来源，未经TCP检测直接发布。

➡️ **何时使用：** `verified_configs.txt` 无效，网络处于白名单模式，只能打开 Yandex、VK、Gosuslugi 等网站时。

```
https://raw.githubusercontent.com/aviamastersgh/vpn-free-russia/main/ru_configs.txt
```

### 对比表

| 文件 | 数量 | 检测方式 | 适用人群 |
|------|-----------|----------|----------|
| `all_configs.txt` | 最多 | ❌ 无检测 | 想要更多选择，愿意自行测试 |
| `verified_configs.txt` | 较少 | ✅ TCP检测 | **大多数用户** |
| `ru_configs.txt` | 约50–150 | ⚠️ 无检测 | 移动网络白名单模式 |

---

## ⚡ 快速连接

复制所需链接，作为订阅添加到任意VPN客户端：

**推荐（可用服务器）：**
```
https://raw.githubusercontent.com/aviamastersgh/vpn-free-russia/main/verified_configs.txt
```

**全部配置：**
```
https://raw.githubusercontent.com/aviamastersgh/vpn-free-russia/main/all_configs.txt
```

**绕过白名单（移动网络）：**
```
https://raw.githubusercontent.com/aviamastersgh/vpn-free-russia/main/ru_configs.txt
```

**如果GitHub被封锁** —— 使用GitHack镜像：
```
https://raw.githack.com/aviamastersgh/vpn-free-russia/main/verified_configs.txt
```

---

## 🤔 如何确定我需要哪个文件？

**第一步：** 检查不使用VPN时能否打开 `google.com`？

- **能** → 普通网络（黑名单模式）。使用 `verified_configs.txt`。
- **不能，但 Yandex/VK/Gosuslugi 能打开** → 白名单模式。使用 `ru_configs.txt`。
- **什么都打不开** → 完全没有网络，配置无法解决问题。

**第二步：** 将链接作为订阅添加到客户端（说明见下文）。

**第三步：** 点击"延迟测试"/"Real Delay"——选择数值为绿色的服务器。

---

## 📱 如何将配置添加到客户端 —— 分步说明

### Android — v2rayNG

1. 从 [v2rayNG](https://github.com/2dust/v2rayNG/releases) 的GitHub页面下载
2. 打开应用 → ☰（菜单）→ **"订阅组"**
3. **+** → 粘贴订阅链接 → 保存
4. 主界面点击 **"更新订阅"**
5. 选择组 → **"真实延迟"**（不是TCP ping！）
6. 选择延迟最小的服务器（绿色）→ ▶️

### Android — Karing

1. 从 [Karing](https://github.com/KaringX/karing/releases) 的GitHub页面下载
2. 添加配置文件 → "添加订阅" → 粘贴链接
3. 更新间隔：1小时
4. 设置 → "自动选择" → 开启
5. 点击盾牌图标 🛡️ —— 客户端自动选择最佳服务器

### Android — NekoBox

1. 下载 [NekoBox](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases)
2. 配置文件 → "添加" → "URL" → 粘贴链接
3. 点击配置文件 → "更新" → 选择服务器 → 连接

### iOS — Streisand（免费）

1. 从App Store安装 [Streisand](https://apps.apple.com/us/app/streisand/id6450534064)
2. **+** → "从剪贴板导入" 或输入订阅URL
3. 加载完成后选择服务器 → "连接"

### iOS — Karing（免费，推荐）

1. 从App Store安装 [Karing](https://apps.apple.com/us/app/karing/id6472431552)
2. 添加配置文件 → "添加订阅" → 粘贴链接
3. 开启自动选择

### iOS — v2Box（免费）

1. 从App Store安装 [v2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690)
2. Subscriptions → **+** → 粘贴URL → 保存 → 更新

### Windows — v2rayN

1. 下载 [v2rayN](https://github.com/2dust/v2rayN/releases) → 解压 → 以管理员身份运行
2. 设置 → 区域预设 → "俄罗斯" → 重启
3. 订阅组 → 组设置 → **+** → 粘贴链接
4. 订阅组 → "无代理更新"
5. 选择配置 → 右键 → "真实延迟测试"
6. 按延迟排序 → 选择最佳 → 回车

### Windows — Karing

1. 下载 [Karing](https://github.com/KaringX/karing/releases) → 以管理员身份运行
2. 添加配置文件 → "添加订阅" → 粘贴链接 → 间隔1小时
3. 设置 → 自动选择 → 间隔10分钟，误差150毫秒
4. 点击盾牌图标 🛡️

---

## 📱 支持的客户端

| 客户端 | 平台 | 免费 | 链接 |
|--------|-----------|-----------|--------|
| **Karing** | Android / iOS / Windows / macOS | ✅ | [GitHub](https://github.com/KaringX/karing/releases) · [iOS](https://apps.apple.com/us/app/karing/id6472431552) |
| **v2rayNG** | Android | ✅ | [GitHub](https://github.com/2dust/v2rayNG/releases) |
| **v2rayN** | Windows / macOS / Linux | ✅ | [GitHub](https://github.com/2dust/v2rayN/releases) |
| **Streisand** | iOS | ✅ | [App Store](https://apps.apple.com/us/app/streisand/id6450534064) |
| **v2Box** | iOS | ✅ | [App Store](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) |
| **NekoBox** | Android | ✅ | [GitHub](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases) |
| **Hiddify** | Android / Windows / macOS | ✅ | [GitHub](https://github.com/hiddify/hiddify-next/releases) |
| **Happ** | Android / iOS | ✅ | [Play](https://play.google.com/store/apps/details?id=com.happproxy) · [iOS](https://apps.apple.com/us/app/happ-proxy-utility/id6504287215) |

---

## 🔒 稳定VPN——专属密钥

公共配置免费，但没有任何保证：服务器可能过载、变更，有时速度较慢。对于公共来源的聚合服务来说，这是正常现象。

如果需要专属服务器上的稳定连接，可通过Telegram机器人获取专属密钥：

<div align="center">

### 🤖 [@NosokVPNBot](https://t.me/NosokVPNBot?start=partner_8655864538)

<a href="https://t.me/NosokVPNBot?start=partner_8655864538"><img src="https://img.shields.io/badge/获取稳定VPN-@NosokVpnBot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="稳定VPN Telegram机器人"/></a>

*专属密钥 · 独立服务器 · 稳定连接*

</div>

---

## 🔒 支持的协议

| 协议 | 抗РКН封锁能力 | 特点 |
|----------|-------------------|------|
| **VLESS + Reality** | 🥇 最强 | 伪装成真实网站的HTTPS流量 |
| **VLESS + XTLS** | 🥇 最强 | 先进加密，对DPI检测不可见 |
| **Trojan** | 🥈 高 | 模拟HTTPS连接 |
| **VMess** | 🥉 中等 | 经典协议，兼容性广 |
| **Shadowsocks** | 🥉 中等 | 快速轻量 |
| **Hysteria2** | ✅ 良好 | 基于UDP的协议，速度快 |
| **TUIC** | ✅ 良好 | 基于QUIC的现代协议 |

---

## ❓ 常见问题

<details>
<summary><strong>添加了配置，但一个都不能用，怎么办？</strong></summary>

1. 确认使用的是 `verified_configs.txt`，而不是 `all_configs.txt`
2. 点击"真实延迟测试"（不是TCP ping——它无法反映VPN的真实可用性）
3. 换一个客户端试试——有时一个客户端"看不到"的配置，另一个客户端能识别
4. 移动网络下可尝试 `ru_configs.txt`
5. 手动更新订阅——配置每6小时更新一次

</details>

<details>
<summary><strong>"TCP ping"和"真实延迟"有什么区别？</strong></summary>

**TCP ping** —— 检测端口是否开放。服务器可能有响应，但VPN本身可能无法工作（端口开放但服务过载或已崩溃）。

**真实延迟（Real Delay）** —— 客户端实际建立VPN连接，并通过该连接检测网络可用性。绿色数字表示VPN真实可用。

选择可用服务器时请始终使用**真实延迟**。

</details>

<details>
<summary><strong>为什么配置昨天能用，今天却不行了？</strong></summary>

公共免费服务器没有稳定性保证。它们可能被РКН封锁、因用户过多而过载，或被所有者下线。

因此订阅每6小时更新一次。在客户端中开启**自动更新**（间隔1-2小时）——这是保持配置持续可用的最可靠方式。

</details>

<details>
<summary><strong>使用公共VPN配置安全吗？</strong></summary>

公共配置来自陌生运营方的免费服务器。主要风险在于：服务器所有者理论上可以看到通过其转发的未加密流量，且无法保证不被记录日志。

**建议：** 不要通过公共配置传输密码和银行信息。如需更高隐私保护，请使用独立服务器上的专属密钥。

</details>

<details>
<summary><strong>如果GitHub被封锁怎么办？</strong></summary>

使用镜像地址——即使GitHub被封锁也能正常访问：

| 镜像 | 使用方法 |
|---------|-------------------|
| **GitHack**（推荐） | 将上述任意链接中的 `raw.githubusercontent.com` 替换为 `raw.githack.com` |
| **jsDelivr** | `https://cdn.jsdelivr.net/gh/aviamastersgh/vpn-free-russia@main/verified_configs.txt` |

</details>

<details>
<summary><strong>可以在路由器或多台设备上使用这些配置吗？</strong></summary>

可以。**v2rayN**（Windows）和 **Karing**（全平台）客户端支持TUN模式，可将设备全部流量导入VPN。路由器可使用支持Mihomo（Clash Meta）的客户端——例如OpenWrt上的OpenClash。

</details>

<details>
<summary><strong>该选择哪种协议：VLESS、Shadowsocks 还是 Hysteria2？</strong></summary>

要获得最强的抗РКН封锁能力——选择 **VLESS + Reality**：它将流量伪装成访问真实HTTPS网站的请求，使DPI难以识别。**Hysteria2** 在基于UDP的连接上速度表现出色。**Shadowsocks** 和 **VMess** 是较老的协议，但依然可用，并被客户端广泛支持。

</details>

---

## 🌍 镜像地址（如果GitHub被封锁）

| 镜像 | `verified_configs.txt` | `all_configs.txt` | `ru_configs.txt` |
|---------|----------------------|-------------------|------------------|
| **GitHack** | [链接](https://raw.githack.com/aviamastersgh/vpn-free-russia/main/verified_configs.txt) | [链接](https://raw.githack.com/aviamastersgh/vpn-free-russia/main/all_configs.txt) | [链接](https://raw.githack.com/aviamastersgh/vpn-free-russia/main/ru_configs.txt) |
| **jsDelivr** | [链接](https://cdn.jsdelivr.net/gh/aviamastersgh/vpn-free-russia@main/verified_configs.txt) | [链接](https://cdn.jsdelivr.net/gh/aviamastersgh/vpn-free-russia@main/all_configs.txt) | [链接](https://cdn.jsdelivr.net/gh/aviamastersgh/vpn-free-russia@main/ru_configs.txt) |

> **GitHack** —— 实时代理，始终保持最新。**jsDelivr** —— CDN，缓存时间可能长达24小时。

---

## 📋 配置来源

| # | 仓库 | 协议 |
|---|-------------|-----------|
| 1 | [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia) | VLESS, Reality, RU CIDR |
| 2 | [barry-far/V2ray-Configs](https://github.com/barry-far/V2ray-Configs) | VLESS, VMess, SS, Trojan |
| 3 | [mahdibland/V2RayAggregator](https://github.com/mahdibland/V2RayAggregator) | 混合 |
| 4 | [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers) | 混合 |
| 5 | [peasoft/NoMoreWalls](https://github.com/peasoft/NoMoreWalls) | 混合 |
| 6 | [freefq/free](https://github.com/freefq/free) | VMess |
| 7 | [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe) | 混合 |
| 8 | [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree) | VMess |

> 我们不生成也不出售服务器——仅对公共来源进行聚合和验证。

---

## ‼️ 免责声明

*作者并非上述VPN配置的所有者、开发者或提供者。本仓库是一个独立的、聚合公开可用数据的信息平台。*

*本资料面向此类信息合法的国家公民，包括用于研究和教育目的。*

*作者不鼓励也不倡导将VPN用于违反法律的目的。使用责任由用户自行承担。*

*请仅将VPN用于合法目的：保护个人数据、安全远程访问、网络隐私保护。*

*所有信息均按"原样"提供，不保证准确性和时效性。*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:764ba2,100:667eea&height=100&section=footer" alt="footer"/>
