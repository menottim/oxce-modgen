# OXCE Common Mod Patterns

Seven complete, working mod examples. Each includes `metadata.yml` and the primary `.rul` file.

__Note on sprites:__ Examples that add new items reuse existing vanilla sprite indices (bigSprite, floorSprite, handSprite). This generator does not create custom artwork. If a fresh sprite sheet is required, the user must supply it and update the indices accordingly.

---

## 1. Balance Mod — Laser Weapon Stat Overrides

Increases accuracy and adjusts sell prices for the three vanilla laser weapons.

__metadata.yml__
```yaml
name: Laser Balance
version: "1.0"
description: "Adjusts laser weapon accuracy and sell prices."
author: modgen
master: xcom1
```

__Ruleset/laser-balance.rul__
```yaml
items:
  - type: STR_LASER_PISTOL
    costSell: 20000
    accuracySnap: 65
    accuracyAimed: 90

  - type: STR_LASER_RIFLE
    costSell: 35000
    accuracySnap: 75
    accuracyAimed: 110

  - type: STR_HEAVY_LASER
    costSell: 50000
    accuracySnap: 55
    accuracyAimed: 100
```

---

## 2. New Item — Plasma Sniper Rifle

Adds a new weapon, its research entry, and display strings. Reuses existing plasma sprite indices.

__metadata.yml__
```yaml
name: Plasma Sniper Rifle
version: "1.0"
description: "Adds a high-powered plasma sniper rifle and its research."
author: modgen
master: xcom1
```

__Ruleset/plasma-sniper.rul__
```yaml
items:
  - type: STR_PLASMA_SNIPER
    costBuy: 0
    costSell: 80000
    weight: 12
    bigSprite: 32
    floorSprite: 32
    handSprite: 96
    bulletSprite: 8
    fireSound: 18
    hitSound: 19
    hitAnimation: 46
    power: 80
    damageType: 4
    accuracySnap: 50
    accuracyAimed: 120
    tuSnap: 40
    tuAimed: 70
    clipSize: -1
    battleType: 1
    twoHanded: true
    invWidth: 1
    invHeight: 3
    requires:
      - STR_PLASMA_SNIPER

research:
  - name: STR_PLASMA_SNIPER
    cost: 500
    points: 25
    dependencies:
      - STR_PLASMA_RIFLE

extraStrings:
  - type: en-US
    strings:
      STR_PLASMA_SNIPER: Plasma Sniper Rifle
      STR_PLASMA_SNIPER_UFOPEDIA: >
        An ultra-long-range plasma weapon optimized for precision fire.
        Requires two hands to operate. Cannot accept an external clip.
```

---

## 3. Research Tree — Faster Laser Research

Halves the research cost for all five vanilla laser research topics.

__metadata.yml__
```yaml
name: Fast Laser Research
version: "1.0"
description: "Halves time-units required to research all laser technologies."
author: modgen
master: xcom1
```

__Ruleset/fast-laser-research.rul__
```yaml
research:
  - name: STR_LASER_WEAPONS
    cost: 100

  - name: STR_LASER_PISTOL
    cost: 50

  - name: STR_LASER_RIFLE
    cost: 75

  - name: STR_HEAVY_LASER
    cost: 100

  - name: STR_LASER_CANNON
    cost: 150
```

---

## 4. Starting Base — Extra Scientists and Engineers

Boosts the starting personnel count and adds additional starting items.

__metadata.yml__
```yaml
name: Headstart Base
version: "1.0"
description: "Begin with extra scientists, engineers, and supplies."
author: modgen
master: xcom1
```

__Ruleset/headstart-base.rul__
```yaml
startingBase:
  - type: xcom1
    scientists: 20
    engineers: 15
    items:
      STR_STINGRAY_LAUNCHER: 2
      STR_STINGRAY_MISSILES: 20
      STR_INTERCEPTOR: 2
      STR_SKYRANGER: 1
      STR_RIFLE: 10
      STR_PISTOL: 5
      STR_PISTOL_CLIP: 20
      STR_RIFLE_CLIP: 30
      STR_GRENADE: 10
      STR_SMOKE_GRENADE: 5
      STR_MEDI_KIT: 4
      STR_MOTION_SCANNER: 2
```

---

## 5. Difficulty Scaling — Aim and Armor Multipliers

Adjusts alien aim and armor multipliers across all five difficulty tiers.

__metadata.yml__
```yaml
name: Difficulty Scaling
version: "1.0"
description: "Rebalances alien aim and armor multipliers per difficulty level."
author: modgen
master: xcom1
```

__Ruleset/difficulty-scaling.rul__
```yaml
difficulty:
  - type: 0
    aimAndArmorMultiplier:
      - 0.5   # alien aim multiplier
      - 0.5   # alien armor multiplier

  - type: 1
    aimAndArmorMultiplier:
      - 0.75
      - 0.75

  - type: 2
    aimAndArmorMultiplier:
      - 1.0
      - 1.0

  - type: 3
    aimAndArmorMultiplier:
      - 1.25
      - 1.25

  - type: 4
    aimAndArmorMultiplier:
      - 1.5
      - 1.5
```

---

## 6. Economy Mod — Doubled Facility Maintenance

Doubles the monthly upkeep cost for six common base facilities.

__metadata.yml__
```yaml
name: Hard Economy
version: "1.0"
description: "Doubles monthly maintenance costs for major base facilities."
author: modgen
master: xcom1
```

__Ruleset/hard-economy.rul__
```yaml
facilities:
  - type: STR_GENERAL_STORES
    monthlyCost: 10000

  - type: STR_LABORATORY
    monthlyCost: 150000

  - type: STR_WORKSHOP
    monthlyCost: 150000

  - type: STR_LARGE_RADAR_SYSTEM
    monthlyCost: 150000

  - type: STR_MISSILE_DEFENSE
    monthlyCost: 200000

  - type: STR_HYPER_WAVE_DECODER
    monthlyCost: 300000
```

---

## 7. QoL Mod — Skyranger Troop Capacity

Increases Skyranger soldier capacity to 18 and vehicle capacity to 4.

__metadata.yml__
```yaml
name: Big Skyranger
version: "1.0"
description: "Expands Skyranger capacity: 18 soldiers and 4 vehicles."
author: modgen
master: xcom1
```

__Ruleset/big-skyranger.rul__
```yaml
crafts:
  - type: STR_SKYRANGER
    soldiers: 18
    vehicles: 4
```
