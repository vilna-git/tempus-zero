# Tempus Zero - Silent Haptic Alarm Watch

A wearable silent alarm system using Raspberry Pi Zero W with integrated haptic motors and real-time clock display, designed to wake users without disturbing others in shared living spaces.

## 💡 Project Overview

**Tempus Zero** (Latin: "Time Zero") is a prototype smart alarm watch that uses **haptic feedback** instead of sound to wake users. Perfect for:
- Shared bedrooms (dorms, family homes)
- Partners with different schedules  
- Light sleepers who don't want to disturb others
- Anyone seeking a gentler wake-up experience

### The Problem
Traditional alarm clocks disrupt everyone in the room, making it difficult for people with different schedules to coexist peacefully.

### Our Solution
A comfortable wearable device that delivers customizable vibration patterns directly to the user, providing a personal wake-up experience without external noise.

## 🎯 Key Features

### Hardware
- **Raspberry Pi Zero W**: Compact embedded system with WiFi connectivity
- **Dual Haptic Motors**: Adafruit DRV2605 controlled vibration
- **16x2 LCD Display**: Real-time clock with alarm time display
- **Lithium-Ion Battery**: 3.7V rechargeable with PowerBoost 1000 charging module
- **3D-Printed Enclosure**: Ergonomic design for sleep comfort (Fusion 360)

### Software
- **Python-based firmware**: I2C communication for motor control and display
- **Customizable alarm strength**: Three intensity levels (Low, Medium, High)
- **Real-time clock**: Continuous time display with alarm monitoring
- **SSH configuration**: Remote setup via Raspberry Pi controller app

### User Experience
- Set alarm time and vibration strength via command-line interface
- LCD shows current time and configured alarm
- Silent haptic wake-up at specified time
- Comfortable form factor for overnight wear

## 🏗️ System Architecture

### Hardware Components

| Component | Model | Purpose |
|-----------|-------|---------|
| Microcontroller | Raspberry Pi Zero W | Main processing unit |
| Haptic Driver | Adafruit DRV2605 | Motor control with 119 vibration effects |
| Vibration Motors | Generic 3V motors (×2) | Haptic feedback generation |
| Display | 16x2 LCD (I2C) | Time and alarm display |
| Battery | 3.7V LiPo 2000mAh | Power supply |
| Charger | Adafruit PowerBoost 1000 | Battery management |
| Enclosure | Custom 3D print | Wearable housing |

### Circuit Design

The system uses I2C communication protocol to minimize GPIO pin usage:
- **I2C Bus 3**: DRV2605 haptic motor controller
- **I2C Bus 1**: 16x2 LCD display
- **Power distribution**: 5V from PowerBoost to all components
- **Motor output**: Dual vibration motors in parallel

![Circuit Diagram](images/FinalCircuit.png)

### Software Architecture

```
User Input → SSH Terminal → Python Script → I2C Communication → Hardware Response
                                    ↓
                              Alarm Monitoring Loop
                                    ↓
                          Time Check (1Hz polling)
                                    ↓
                    Match Detected → Trigger Haptic Feedback
```

## 💻 Code Implementation

### Core Functionality

```python
# Initialize I2C bus and haptic driver
i2c = I2C(3)
drv = adafruit_drv2605.DRV2605(i2c)

# Set vibration effect based on user preference
if strength == "Low":
    drv.sequence[0] = adafruit_drv2605.Effect(119)
elif strength == "Medium":
    drv.sequence[0] = adafruit_drv2605.Effect(1)
else:  # High
    drv.sequence[0] = adafruit_drv2605.Effect(47)

# Main alarm loop
while True:
    current_time = str(datetime.now().time())[0:5]
    if current_time == alarm_time:
        drv.play()  # Activate haptic feedback
    display.lcd_display_string(current_time, 2)
    sleep(1)
```

## 🚀 Getting Started

### Prerequisites

**Hardware:**
- Raspberry Pi Zero W with SD card (8GB+)
- All components listed in Bill of Materials
- Soldering equipment
- 3D printer access (or service)

**Software:**
- Raspbian OS
- Python 3.7+
- Required libraries:
  ```bash
  pip install adafruit-circuitpython-drv2605
  pip install adafruit-extended-bus
  pip install RPLCD
  ```

### Installation

1. **Flash Raspberry Pi OS**
   ```bash
   # Use Raspberry Pi Imager to flash SD card
   # Enable SSH during setup
   ```

2. **Connect to Raspberry Pi**
   ```bash
   # Use Raspberry Pi Controller app or terminal
   ssh pi@raspberrypi.local
   # Default password: raspberry (change immediately!)
   ```

3. **Install Dependencies**
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip i2c-tools
   sudo pip3 install adafruit-circuitpython-drv2605
   sudo pip3 install adafruit-extended-bus
   sudo pip3 install RPLCD
   ```

4. **Enable I2C**
   ```bash
   sudo raspi-config
   # Interface Options → I2C → Enable
   sudo reboot
   ```

5. **Upload Code**
   ```bash
   # Copy alarm_controller.py to /home/pi/
   cd /home/pi
   python3 alarm_controller.py
   ```

### Usage

1. Power on the watch
2. Connect via SSH (or use Raspberry Pi Controller app)
3. Run the alarm script:
   ```bash
   python3 alarm_controller.py
   ```
4. Enter alarm time (HH:MM format): `07:30`
5. Select vibration strength: `Low`, `Medium`, or `High`
6. Alarm activates at specified time with haptic feedback
7. Press Ctrl+C to exit

## 📊 Design Evolution

### Version 1: Component Layout
Initial breadboard prototype with all components exposed for testing.

![Design V1](images/DesignV1_components_.png)

### Version 2: Compact Assembly  
Integration of components into a wearable form factor.

![Design V2](images/DesignV2.png)

### Version 3: Final Enclosure
3D-printed housing with ergonomic wrist strap design.

![Design V3](images/DesignV3Top.png)
![Final Design](images/FinalDesign.png)

## 💰 Project Cost

**Total Project Cost: $7,724**

| Category | Cost |
|----------|------|
| Hardware Components | $93.58 |
| Miscellaneous (tools, materials) | $130.00 |
| Projected Labor (150 hrs @ $50/hr) | $7,500.00 |

*See [cost_breakdown.pdf](docs/cost_breakdown.pdf) for detailed breakdown*

## 🎓 Academic Context

**Course**: NYU RAD 40 - Student Leadership Development Program  
**Team**: Oleksandra Kovalenko, Siddhant Bhatnagar, Kushal Mamillapalli  
**Timeline**: Fall 2023  
**Deliverables**: Working prototype, documentation, final presentation

### Learning Outcomes
- ✅ Embedded systems design and programming
- ✅ I2C communication protocol implementation
- ✅ 3D CAD modeling (Fusion 360)
- ✅ Soldering and circuit assembly
- ✅ User-centered design thinking
- ✅ Project management (Wrike)
- ✅ Team collaboration and division of labor

## 📁 Project Structure

```
tempus-zero/
├── code/
│   └── alarm_controller.py    # Main Python firmware
├── images/
│   ├── CodeFlowChartFinal.png     # System flowchart
│   ├── DesignV1_components_.png   # Component layout
│   ├── DesignV2.png               # Assembly design
│   ├── DesignV3Top.png            # Enclosure top view
│   ├── FinalCircuit.png           # Circuit schematic
│   └── FinalDesign.png            # Final product render
├── docs/
│   └── cost_breakdown.pdf         # Bill of materials
├── README.md                      # This file
├── LICENSE                        # MIT License
└── .gitignore                     # Git ignore rules
```

## 🔧 Technical Specifications

**Power:**
- Input: 5V USB-C (charging)
- Battery: 3.7V 2000mAh LiPo
- Runtime: ~8-12 hours continuous operation
- Charging: 2-3 hours via PowerBoost 1000

**Dimensions:**
- Watch module: 60mm × 40mm × 25mm
- Wrist strap: Adjustable fabric band
- Total weight: ~85g

**Communication:**
- WiFi: 802.11 b/g/n (2.4GHz)
- I2C: Bus 1 (display), Bus 3 (haptic controller)
- SSH: Remote configuration

## 🐛 Known Issues & Future Improvements

### Current Limitations
- Manual alarm entry (no mobile app interface)
- Single alarm support
- No snooze functionality
- Fabric strap not waterproof

### Planned Enhancements
- [ ] Bluetooth iOS/Android app for wireless alarm setting
- [ ] Multiple alarm scheduling
- [ ] Snooze and gradual wake features
- [ ] Sleep tracking integration
- [ ] Waterproof enclosure design
- [ ] Smaller form factor (custom PCB)

## 🤝 Team Contributions

**Oleksandra Kovalenko**: Embedded programming, I2C implementation, system integration  
**Siddhant Bhatnagar**: Circuit design, soldering, hardware assembly  
**Kushal Mamillapalli**: 3D modeling (Fusion 360), enclosure design, CAD iterations

## 📄 License

MIT License - Free to use for educational and personal projects.

## 🙏 Acknowledgments

- NYU MakerSpace for fabrication resources
- Roman (SLDP Mentor) for project guidance
- Adafruit for excellent hardware documentation
- Raspberry Pi Foundation for accessible embedded computing

## 📧 Contact

Questions about the project? Open an issue on GitHub.

---

**⚠️ Disclaimer**: This is a student prototype project. Not intended for commercial use or medical applications. Always consult proper alarm systems for critical wake-up requirements.

**Sleep well, wake gently.** 🌙✨
