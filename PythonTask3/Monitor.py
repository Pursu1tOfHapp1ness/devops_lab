import psutil
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
Interval = int(config["interval"]["Interval"])
OutputFile = config["output_file"]["Output_File"]


class MonitorUtil:
    temp = 1

    @staticmethod
    def monitoring():
        total_memory = psutil.virtual_memory().total / 1024 ** 3
        used_memory = psutil.virtual_memory().used / 1024 ** 3
        cpu_load = psutil.cpu_percent(interval=Interval)
        network_inf_bytes_sent = psutil.net_io_counters().bytes_sent / 1024 ** 3
        network_inf_bytes_recv = psutil.net_io_counters().bytes_recv / 1024 ** 3
        network_inf_packets_sent = psutil.net_io_counters().packets_sent
        network_inf_packets_recv = psutil.net_io_counters().packets_recv
        network_inf_errin = psutil.net_io_counters().errin
        network_inf_errout = psutil.net_io_counters().errout
        network_inf_dropin = psutil.net_io_counters().dropin
        network_inf_dropout = psutil.net_io_counters().dropout
        io_inf_read_count = psutil.disk_io_counters().read_count
        io_inf_write_count = psutil.disk_io_counters().write_count
        io_inf_read_bytes = psutil.disk_io_counters().read_bytes / 1024 ** 3
        io_inf_write_bytes = psutil.disk_io_counters().write_bytes / 1024 ** 3
        io_inf_read_time = psutil.disk_io_counters().read_time / 1000
        io_inf_write_time = psutil.disk_io_counters().write_time / 1000
        output = ["Total memory = %s GB\n" % total_memory,
                  "Used memory = %s GB\n" % used_memory,
                  "CPU Load (in percents) = %s\n" % cpu_load,
                  "Number of Gbytes sent = %s\n" % network_inf_bytes_sent,
                  "Number of Gbytes sent = %s\n" % network_inf_bytes_recv,
                  "Number of packets sent = %s\n" % network_inf_packets_sent,
                  "Number of packets received = %s\n" % network_inf_packets_recv,
                  "Total number of errors while receiving = %s\n" % network_inf_errin,
                  "Total number of errors while sending = %s\n" % network_inf_errout,
                  "Total number of incoming packets which were dropped = %s\n" % network_inf_dropin,
                  "Total number of outgoing packets which were dropped = %s\n" % network_inf_dropout,
                  "Number of reads = %s\n" % io_inf_read_count,
                  "Number of writes = %s\n" % io_inf_write_count,
                  "Number of Gbytes read = %s\n" % io_inf_read_bytes,
                  "Number of Gbytes written = %s\n" % io_inf_write_bytes,
                  "Time spent reading from disk (in seconds) = %s\n" % io_inf_read_time,
                  "Time spent writing to disk (in seconds) = %s\n" % io_inf_write_time]
        time_stamp = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        snap_print = "SNAPSHOT %s : %s\n" % (str(MonitorUtil.temp), time_stamp)
        with open(OutputFile, "a") as f:
            f.write(snap_print)
            for i in output:
                f.write(str(i))
        MonitorUtil.temp = MonitorUtil.temp + 1


if __name__ == "__main__":
    MonitorUtil.monitoring()

