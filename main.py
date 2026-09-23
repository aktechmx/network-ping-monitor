import subprocess
import csv
import time
import re
from datetime import datetime


def get_host():
    """Ask the user for the hostname or IP address to monitor."""

    while True:
        host = input("Where are you going to ping: ").strip()

        if host:
            return host

        print("Host cannot be empty. Please try again...")


def ping_host(host):
    """Ping a host once and return its status and latency."""

    resultado = subprocess.run(
        ["ping", "-n", "1", host],
        capture_output=True,
        text=True
    )

    # Buscar la latencia en la respuesta
    match = re.search(r"time[=<](\d+)ms", resultado.stdout)

    if resultado.returncode == 0 and match:
        estado = "OK"
        latencia = int(match.group(1))
    else:
        estado = "FAIL"
        latencia = None

    return estado, latencia


def monitor(host):
    ARCHIVO = "ping_log.csv"

    total_pings = 0
    successful_pings = 0
    failed_pings = 0
    latencies = []

    with open(ARCHIVO, "a", newline="") as archivo:

        writer = csv.writer(archivo)

        if archivo.tell() == 0:
            writer.writerow([
                "date",
                "hour",
                "host",
                "state",
                "latency_ms"
            ])

        try:

            while True:

                ahora = datetime.now()

                # Ejecutar ping
                estado, latencia = ping_host(host)

                total_pings += 1

                # Actualizar estadísticas
                if estado == "OK":
                    successful_pings += 1
                    latencies.append(latencia)
                else:
                    failed_pings += 1

                # Guardar en CSV
                writer.writerow([
                    ahora.strftime("%Y-%m-%d"),
                    ahora.strftime("%H:%M:%S"),
                    host,
                    estado,
                    latencia if latencia is not None else "---"
                ])

                archivo.flush()

                # Calcular estadísticas
                packet_loss = (failed_pings / total_pings) * 100

                if latencies:
                    average_latency = sum(latencies) / len(latencies)
                    min_latency = min(latencies)
                    max_latency = max(latencies)
                else:
                    average_latency = 0
                    min_latency = 0
                    max_latency = 0

                # Mostrar resultado del ping
                print(
                    f"{ahora.strftime('%Y-%m-%d %H:%M:%S')} | "
                    f"{host} | "
                    f"{estado} | "
                    f"Latency: {latencia if latencia is not None else '---'} ms"
                )

                # Mostrar estadísticas
                print(
                    f"Packets: {total_pings} | "
                    f"Loss: {packet_loss:.2f}% | "
                    f"Avg: {average_latency:.2f} ms | "
                    f"Min: {min_latency} ms | "
                    f"Max: {max_latency} ms"
                )

                print("-" * 80)

                time.sleep(1)

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


def main():
    host = get_host()

    print(f"\nMonitoring: {host}")

    monitor(host)


if __name__ == "__main__":
    main()