# Network Ping Monitor

A simple network monitoring tool developed in Python to continuously monitor a host or IP address.

The main purpose of this project is to have a simple way to identify connection failures, latency changes, and packet loss while keeping a log that can be reviewed later.

I originally created this tool to help troubleshoot network connectivity issues where I needed more information than just running a normal ping command.

## Features

- Monitor an IP address or hostname continuously
- Validate the host before starting the monitoring process
- Configure the ping interval
- Display connection status as `OK` or `FAIL`
- Measure latency for each successful ping
- Calculate packet loss
- Show average, minimum, and maximum latency
- Keep track of successful and failed packets
- Save the monitoring results automatically to a CSV file
- Display final statistics when the monitoring process is stopped

## Requirements

- Windows
- Python 3.x

The current version uses the Windows `ping` command.

No additional Python libraries are required. The project only uses modules included with Python.

## Installation

Clone the repository:

```bash
git clone https://github.com/aktechmx/network-ping-monitor.git
```

Open the project folder:

```bash
cd network-ping-monitor
```

Run the program:

```bash
python main.py
```

## How to Use

The program will first ask for the IP address or hostname that you want to monitor:

```text
Where are you going to ping: 8.8.8.8
```

Then you can define how frequently the ping should be executed:

```text
Ping interval in seconds [1]:
```

Press `Enter` to use the default interval of **1 second**.

### Example

```text
Where are you going to ping: 8.8.8.8
Ping interval in seconds [1]: 2

Monitoring: 8.8.8.8
Interval: 2.0 seconds

2026-09-26 09:10:15 | 8.8.8.8 | OK | Latency: 18 ms
Packets: 1 | Loss: 0.00% | Avg: 18.00 ms | Min: 18 ms | Max: 18 ms
--------------------------------------------------------------------------------
2026-09-26 09:10:17 | 8.8.8.8 | OK | Latency: 17 ms
Packets: 2 | Loss: 0.00% | Avg: 17.50 ms | Min: 17 ms | Max: 18 ms
--------------------------------------------------------------------------------
```

To stop the monitoring process, press:

```text
Ctrl + C
```

The application will display the final statistics before closing.

## CSV Log

The application automatically creates a file named:

```text
ping_log.csv
```

The file is stored in the same directory where the Python script or compiled executable is located.

The CSV contains the following information:

```csv
date,hour,host,state,latency_ms
2026-09-26,09:10:15,8.8.8.8,OK,18
2026-09-26,09:10:17,8.8.8.8,OK,17
2026-09-26,09:10:19,8.8.8.8,FAIL,---
```

This makes it easier to review the connection behavior later or use the information in Excel, Power BI, or another analysis tool.

## Build Executable

The project can also be compiled as a standalone Windows executable using PyInstaller.

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --clean --name PingMonitor main.py
```

The executable will be generated inside:

```text
dist/
```

The final file will be:

```text
dist/PingMonitor.exe
```

The executable can run on a Windows computer without requiring Python to be installed.

## Project Structure

```text
network-ping-monitor/
│
├── main.py
├── README.md
├── .gitignore
└── ping_log.csv    # Generated automatically and ignored by Git
```

## Current Limitations

The current version was developed for Windows because the ping process uses the Windows `-n` parameter.

At this stage, the application runs from the command line and monitors one host at a time.

## Future Improvements

Some improvements that could be added in future versions:

- Graphical interface
- Real-time latency chart
- Monitor multiple hosts
- Export monitoring statistics
- Configuration file
- Linux and macOS support
- Additional network diagnostics

## Author

**Armando Zuñiga**

IT Infrastructure / Network Support

GitHub: [aktechmx](https://github.com/aktechmx)