# Network Ping Monitor

A lightweight Python tool for continuously monitoring network connectivity, latency, packet loss and intermittent communication failures.

I originally created this project as a simple way to collect evidence when troubleshooting devices with intermittent connectivity problems. Instead of running individual ping tests manually, the tool continuously monitors a host and keeps a historical record that can be analyzed later.

---

## 📡 What does it do?

Network Ping Monitor continuously sends ICMP requests to a hostname or IP address and records the result of each test.

For every monitoring session, the application tracks:

- Date and time
- Host or IP address
- Connection status (`OK` / `FAIL`)
- Response latency
- Total packets sent
- Successful and failed requests
- Packet loss percentage
- Average latency
- Minimum latency
- Maximum latency

Monitoring results are automatically stored in a CSV file for later analysis.

---

## 💡 Why I built it

Intermittent network problems can be difficult to troubleshoot.

A device may be working normally when an IT technician checks it, even though users report that it disconnects several times during the day.

Running:

```bash
ping 192.168.1.50
```

can tell us what is happening at that moment, but it doesn't provide a structured historical record for later analysis.

This project started from a simple idea:

> **What if I leave the device monitored and analyze the failures afterward?**

Network Ping Monitor automates that process.

---

## ✨ Features

### Continuous monitoring

Continuously monitors a hostname or IP address using ICMP requests.

### Host validation

Before monitoring begins, the application verifies that the hostname or IP address can be resolved.

Invalid or empty destinations are rejected and the user is prompted again.

### Configurable monitoring interval

The user can define how often a ping should be executed.

```text
Ping interval in seconds [1]: 5
```

Pressing Enter uses the default interval of `1` second.

Decimal intervals are also supported:

```text
0.5
2.5
5
```

### Automatic CSV logging

Each ping result is automatically stored in:

```text
ping_log.csv
```

When running the Python script, the log is stored alongside the script.

When running a compiled executable, the log is stored alongside the executable.

### Real-time statistics

During monitoring, the application continuously calculates:

- Total packets
- Successful requests
- Failed requests
- Packet loss
- Average latency
- Minimum latency
- Maximum latency

### Graceful termination

Monitoring can be stopped using:

```text
Ctrl + C
```

The application then displays the final statistics for the monitoring session.

---

## ⚙️ How it works

When the application starts, it asks for the hostname or IP address to monitor:

```text
Where are you going to ping: 192.168.1.50
```

It then asks for the monitoring interval:

```text
Ping interval in seconds [1]: 2
```

The monitoring session begins:

```text
Monitoring: 192.168.1.50
Interval: 2.0 seconds

2026-09-24 08:30:21 | 192.168.1.50 | OK | Latency: 4 ms
Packets: 1 | Loss: 0.00% | Avg: 4.00 ms | Min: 4 ms | Max: 4 ms
--------------------------------------------------------------------------------
```

If the device stops responding:

```text
2026-09-24 08:31:04 | 192.168.1.50 | FAIL | Latency: --- ms
Packets: 23 | Loss: 4.35% | Avg: 3.92 ms | Min: 2 ms | Max: 8 ms
--------------------------------------------------------------------------------
```

The monitoring process continues until the user stops it with `Ctrl + C`.

---

## 📊 CSV Logging

Monitoring results are stored using the following structure:

```csv
date,hour,host,state,latency_ms
2026-09-24,08:30:21,192.168.1.50,OK,4
2026-09-24,08:30:23,192.168.1.50,OK,3
2026-09-24,08:30:25,192.168.1.50,FAIL,---
2026-09-24,08:30:27,192.168.1.50,OK,5
```

The generated file can later be analyzed using tools such as:

- Microsoft Excel
- Python
- Pandas
- Power BI

> `ping_log.csv` is excluded from the Git repository through `.gitignore` because it contains runtime-generated monitoring data.

---

## 📈 Statistics

| Metric | Description |
|---|---|
| Total packets | Number of ping requests performed |
| Successful | Requests that received a valid response |
| Failed | Requests without a valid response |
| Packet loss | Percentage of failed requests |
| Average latency | Average response time of successful requests |
| Minimum latency | Lowest recorded response time |
| Maximum latency | Highest recorded response time |

---

## 🧩 Application Structure

The monitoring logic has been separated into reusable functions to make the application easier to maintain and extend.

```text
main()
 │
 ├── get_host()
 │      └── validate_host()
 │
 ├── get_interval()
 │
 └── monitor(host, interval)
          │
          ├── get_application_path()
          ├── ping_host(host)
          ├── CSV logging
          ├── Statistics
          └── Monitoring interval
```

### Main functions

| Function | Responsibility |
|---|---|
| `get_application_path()` | Determines where runtime files should be stored |
| `validate_host()` | Validates whether a hostname or IP can be resolved |
| `get_host()` | Requests and validates the monitoring destination |
| `get_interval()` | Requests and validates the monitoring interval |
| `ping_host()` | Executes a ping and returns status and latency |
| `monitor()` | Controls monitoring, statistics and CSV logging |
| `main()` | Coordinates application startup |

---

## 🛠️ Technologies

The current version uses only Python's standard library.

- **Python**
- `subprocess` — executes Windows ping commands
- `socket` — hostname and IP resolution
- `csv` — stores monitoring results
- `datetime` — generates timestamps
- `re` — extracts latency from ping responses
- `time` — controls the monitoring interval
- `os` — handles filesystem paths
- `sys` — detects script/executable execution context

No external Python packages are required.

---

## 💻 Requirements

- Windows
- Python 3.x
- Network access to the device being monitored

> The current version uses the Windows `ping -n` command and is therefore Windows-focused.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aktechmx/network-ping-monitor.git
```

### 2. Enter the project directory

```bash
cd network-ping-monitor
```

### 3. Run the application

```bash
python main.py
```

### 4. Enter the destination

```text
Where are you going to ping: 192.168.1.50
```

### 5. Select the monitoring interval

```text
Ping interval in seconds [1]: 2
```

Press Enter without entering a value to use the default `1` second interval.

### 6. Stop monitoring

```text
Ctrl + C
```

The final monitoring statistics will be displayed automatically.

---

## 🗂️ Project Structure

```text
network-ping-monitor/
│
├── main.py
├── .gitignore
└── README.md
```

Generated files such as `ping_log.csv`, Python virtual environments and PyInstaller build files are intentionally excluded from version control.

---

## 🔎 Practical Use Cases

Network Ping Monitor can help when troubleshooting:

- Intermittent network connectivity
- Workstations that randomly disconnect
- Network printers
- Wireless devices
- Network equipment
- Devices that appear offline periodically
- Unstable connections that are difficult to reproduce manually

The historical CSV log can help correlate connectivity failures with other network or system events during troubleshooting.

---

## 🗺️ Roadmap

Network Ping Monitor is an evolving project.

Potential future improvements include:

- [ ] Graphical user interface
- [ ] Real-time latency charts
- [ ] Historical latency visualization
- [ ] Automatic outage-duration calculation
- [ ] Availability percentage
- [ ] Multiple device monitoring
- [ ] Excel report generation
- [ ] Data analysis with Pandas
- [ ] Windows executable release
- [ ] Configuration file support
- [ ] Alert notifications
- [ ] Cross-platform ping support

---

## 📌 Project Status

**Current version: v1.1**

The core monitoring functionality is operational and includes host validation, configurable monitoring intervals, real-time statistics and persistent CSV logging.

The project is being progressively expanded as part of my work with Python, IT automation and network troubleshooting.

---

## 👨‍💻 Author

**Armando Zuñiga**

IT Engineer focused on infrastructure, automation and data analysis.

🌐 [AKTech](https://aktech.com.mx)

---

## ⚠️ Disclaimer

This project is intended as a lightweight troubleshooting and learning tool.

It is not intended to replace enterprise network monitoring platforms.