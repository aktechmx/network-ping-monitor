import csv
import os
import re
import socket
import subprocess
import sys
import time
from datetime import datetime


def get_application_path():
    """Get the folder where the script or executable is located."""

    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)

    return os.path.dirname(os.path.abspath(__file__))


def validate_host(host):
    """Check if the hostname or IP address can be resolved."""

    try:
        socket.gethostbyname(host)
        return True

    except socket.gaierror:
        return False


def get_host():
    """Ask the user for the hostname or IP address to monitor."""

    while True:
        host = input("Where are you going to ping: ").strip()

        if not host:
            print("Host cannot be empty. Please try again...")
            continue

        if validate_host(host):
            return host

        print(
            "Host could not be resolved. "
            "Please check the hostname or IP address."
        )


def get_interval():
    """Ask the user for the ping interval in seconds."""

    while True:
        value = input("Ping interval in seconds [1]: ").strip()

        # If the user presses Enter, use 1 second as default
        if not value:
            return 1.0

        try:
            interval = float(value)

            if interval > 0:
                return interval

            print("Interval must be greater than 0...")

        except ValueError:
            print("Please enter a valid number...")


def ping_host(host):
    """Ping the host one time and return the status and latency."""

    result = subprocess.run(
        ["ping", "-n", "1", host],
        capture_output=True,
        text=True,
        check=False
    )

    # Check if the host answered the ping
    if result.returncode == 0:
        status = "OK"

        # Get the latency from Windows ping in English or Spanish
        match = re.search(
            r"(?:time|tiempo)[=<](\d+)ms",
            result.stdout,
            re.IGNORECASE
        )

        if match:
            latency = int(match.group(1))
        else:
            latency = None

    else:
        status = "FAIL"
        latency = None

    return status, latency


def monitor(host, interval):
    """Start monitoring the IP address or hostname."""

    app_path = get_application_path()

    # Create a timestamp for the log file
    start_time = datetime.now()
    timestamp = start_time.strftime("%Y-%m-%d_%H-%M-%S")

    # Create a different CSV file for each monitoring session
    safe_host = host.replace(":", "-")
    csv_filename = f"ping_{safe_host}_{timestamp}.csv"
    csv_file = os.path.join(app_path, csv_filename)

    total_pings = 0
    successful_pings = 0
    failed_pings = 0
    latencies = []

    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "date",
            "hour",
            "host",
            "state",
            "latency_ms"
        ])

        try:

            while True:

                current_time = datetime.now()

                # Run the ping
                status, latency = ping_host(host)

                total_pings += 1

                # Update ping statistics
                if status == "OK":
                    successful_pings += 1

                    if latency is not None:
                        latencies.append(latency)

                else:
                    failed_pings += 1

                # Save the result in the CSV file
                writer.writerow([
                    current_time.strftime("%Y-%m-%d"),
                    current_time.strftime("%H:%M:%S"),
                    host,
                    status,
                    latency if latency is not None else "---"
                ])

                # Save the information immediately
                file.flush()

                # Calculate current statistics
                packet_loss = (failed_pings / total_pings) * 100

                if latencies:
                    average_latency = sum(latencies) / len(latencies)
                    min_latency = min(latencies)
                    max_latency = max(latencies)

                else:
                    average_latency = 0
                    min_latency = 0
                    max_latency = 0

                # Show the current ping result
                print(
                    f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} | "
                    f"{host} | "
                    f"{status} | "
                    f"Latency: "
                    f"{latency if latency is not None else '---'} ms"
                )

                # Show the current statistics
                print(
                    f"Packets: {total_pings} | "
                    f"Loss: {packet_loss:.2f}% | "
                    f"Avg: {average_latency:.2f} ms | "
                    f"Min: {min_latency} ms | "
                    f"Max: {max_latency} ms"
                )

                print("-" * 80)

                # Wait before the next ping
                time.sleep(interval)

        except KeyboardInterrupt:

            print("\nMonitoring stopped.")

            print("\nFinal statistics:")
            print(f"Total packets: {total_pings}")
            print(f"Successful: {successful_pings}")
            print(f"Failed: {failed_pings}")

            if total_pings > 0:
                print(f"Packet loss: {packet_loss:.2f}%")

            if latencies:
                print(f"Average latency: {average_latency:.2f} ms")
                print(f"Minimum latency: {min_latency} ms")
                print(f"Maximum latency: {max_latency} ms")

            print(f"\nLog saved as: {csv_filename}")

            input("\nPress Enter to close...")


def main():
    """Start the Network Ping Monitor."""

    host = get_host()
    interval = get_interval()

    print(f"\nMonitoring: {host}")
    print(f"Interval: {interval} seconds")

    monitor(host, interval)


if __name__ == "__main__":
    main()