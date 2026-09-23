# Network Ping Monitor

A lightweight Python tool for continuously monitoring network connectivity, latency and intermittent communication failures.

I originally created this project as a simple way to collect evidence when troubleshooting devices with intermittent connectivity problems. Instead of running individual ping tests manually, the tool continuously monitors a host and keeps a historical record that can be analyzed later.

---

## 📡 What does it do?

Network Ping Monitor continuously sends ICMP requests to a hostname or IP address and records the result of each test.

For every ping, the application tracks:

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

All monitoring results are also stored automatically in a CSV file.

---

## 💡 Why I built it

Intermittent network problems can be difficult to troubleshoot.

A device may be working normally when an IT technician checks it, even though users report that it disconnects several times during the day.

Running:

```bash
ping 192.168.1.50
```

can tell us what is happening at that moment, but it doesn't necessarily give us a structured historical record for later analysis.

This project started from a simple idea:

> **What if I leave the device monitored and analyze the failures afterward?**

Network Ping Monitor automates that process.

---

## ⚙️ How it works

When the application starts, it asks for the hostname or IP address to monitor:

```text
Where are you going to ping: 192.168.1.50
```

The application then continuously executes ping requests and displays the result in the console.

Example:

```text
2026-09-23 10:35:21 | 192.168.1.50 | OK | Latency: 4 ms
Packets: 25 | Loss: 0.00% | Avg: 3.84 ms | Min: 2 ms | Max: 7 ms
--------------------------------------------------------------------------------
```

If the device stops responding:

```text
2026-09-23 10:36:04 | 192.168.1.50 | FAIL | Latency: --- ms
Packets: 68 | Loss: 1.47% | Avg: 3.92 ms | Min: 2 ms | Max: 8 ms
--------------------------------------------------------------------------------
```

Monitoring continues until the user stops the application with:

```text
Ctrl + C
```

The program then displays the final statistics for the monitoring session.

---

## 📊 CSV Logging

Every connectivity test is automatically stored in:

```text
ping_log.csv
```

The file uses the following structure:

```csv
date,hour,host,state,latency_ms
2026-09-23,10:35:21,192.168.1.50,OK,4
2026-09-23,10:35:22,192.168.1.50,OK,3
2026-09-23,10:35:23,192.168.1.50,FAIL,---
2026-09-23,10:35:24,192.168.1.50,OK,5
```

This makes it possible to analyze the monitoring session later using tools such as Excel, Python, Pandas or Power BI.

> The generated `ping_log.csv` file is excluded from the repository through `.gitignore`.

---

## 📈 Statistics

During monitoring, the application calculates:

| Metric | Description |
|---|---|
| Total packets | Number of ping requests performed |
| Successful | Requests that received a valid response |
| Failed | Requests without a valid response |
| Packet loss | Percentage of failed requests |
| Average latency | Average response time of successful requests |
| Minimum latency | Lowest recorded response time |
| Maximum latency | Highest recorded response time |

When monitoring is stopped, the final statistics are displayed automatically.

---

## 🛠️ Technologies

The current version intentionally uses only Python's standard library.

- **Python**
- `subprocess` — executes Windows ping commands
- `csv` — stores monitoring results
- `datetime` — generates timestamps
- `re` — extracts latency from ping responses
- `time` — controls the monitoring interval

No external Python packages are required for the current version.

---

## 💻 Requirements

- Windows
- Python 3.x
- Network access to the device being monitored

> The current version uses the Windows `ping -n` command and is therefore designed for Windows.

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

### 4. Enter a hostname or IP address

For example:

```text
Where are you going to ping: 8.8.8.8
```

The monitoring process will start immediately.

To stop monitoring:

```text
Ctrl + C
```

---

## 🗂️ Current Project Structure

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

The tool can be useful when troubleshooting:

- Intermittent network connectivity
- Workstations that randomly disconnect
- Network printers
- Wireless devices
- Network equipment
- Devices that appear offline periodically
- Unstable connections that are difficult to reproduce manually

The CSV history can also help correlate connectivity failures with other events during troubleshooting.

---

## 🗺️ Roadmap

This is an evolving project. Some improvements I'm considering for future versions include:

- [ ] Graphical user interface
- [ ] Real-time charts
- [ ] Historical latency visualization
- [ ] Automatic outage-duration calculation
- [ ] Availability percentage
- [ ] Multiple device monitoring
- [ ] Configurable ping intervals
- [ ] Excel report generation
- [ ] Data analysis with Pandas
- [ ] Windows executable release
- [ ] Configuration file support
- [ ] Alert notifications

---

## 📌 Project Status

**Current version:** Command-line prototype

The core monitoring and CSV logging functionality is working. The project is being progressively expanded as part of my work with Python, IT automation and network troubleshooting.

---

## 👨‍💻 Author

**Armando Zuñiga**

IT Engineer focused on infrastructure, automation and data analysis.

🌐 [AKTech](https://aktech.com.mx)

---

## ⚠️ Disclaimer

This project is intended as a lightweight troubleshooting and learning tool. It is not intended to replace enterprise network monitoring platforms.