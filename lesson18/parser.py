import argparse
import json
import pathlib
import re
from collections import Counter


class LogsParser:

    def __init__(self, logs_source, json_file):
        self.logs_source: pathlib.Path = pathlib.Path(logs_source)
        self.json_file: pathlib.Path = pathlib.Path(json_file).absolute()

        self.log_files = []

        if self.logs_source.is_dir():
            self.log_files = sorted(list([log_file.absolute() for log_file in sorted(self.logs_source.glob("**/*"))]))
        elif self.logs_source.is_file():
            self.log_files.append(self.logs_source.absolute())
        else:
            raise FileExistsError("Incorrect path to source folder or log file")
        self.LOG_LINE_PATTERN = re.compile(
            pattern=r'((?:\d{1,3}\.){3}\d{1,3}|(?:[a-f0-9]{1,4}:){7}[a-f0-9]{1,4}|::\d)\s+-\s+-\s+\[.*?\+\d+\]\s+"(GET|HEAD|POST|PUT|DELETE|OPTIONS)\s+(\/?.*?)\s+HTTP\/1\.\d"\s+(\d+)\s+(\d+)',
            flags=re.IGNORECASE
        )

    def _get_lines_from_logs(self):
        file_lines = []
        for log_file in self.log_files:
            with open(file=str(log_file), mode="r") as f:
                for line in f.readlines():
                    file_lines.append(line)
        return file_lines

    def save_report(self):
        with open(file=str(self.json_file), mode="w") as f:
            data = {
                "requests_total": self.get_total_number_of_requests(),
                "requests_by_type": self.get_requests_by_type(),
                "top_10_ip_addresses": self.get_top_10_ip_addresses(),
                "top_10_longest_requests": self.get_top_10_longest_requests(),
                "top_10_client_error_requests": self.get_top_10_client_error_requests(),
                "top_10_server_error_requests": self.get_top_10_server_error_requests()
            }
            f.write(json.dumps(data, indent=4))

    def get_total_number_of_requests(self):
        return sum(1 for line in self._get_lines_from_logs() if line)

    def get_requests_by_type(self):
        requests_by_type = {
            "GET": 0,
            "HEAD": 0,
            "POST": 0,
            "PUT": 0,
            "DELETE": 0,
            "OPTIONS": 0
        }
        for line in self._get_lines_from_logs():
            match = self.LOG_LINE_PATTERN.search(string=line)
            if match:
                request_type = match.group(2)
                if request_type == "GET":
                    requests_by_type["GET"] += 1
                if request_type == "HEAD":
                    requests_by_type["HEAD"] += 1
                if request_type == "POST":
                    requests_by_type["POST"] += 1
                if request_type == "PUT":
                    requests_by_type["PUT"] += 1
                if request_type == "DELETE":
                    requests_by_type["DELETE"] += 1
                if request_type == "OPTIONS":
                    requests_by_type["OPTIONS"] += 1

        return requests_by_type

    def get_top_10_ip_addresses(self):
        ip_addresses = []
        for line in self._get_lines_from_logs():
            match = self.LOG_LINE_PATTERN.search(string=line)
            if match:
                ip_addresses.append(match.group(1))
        top_10_addresses = []
        for ip in Counter(ip_addresses).most_common(10):
            top_10_addresses.append({"ip": ip[0], "count": ip[1]})
        return top_10_addresses

    def get_top_10_longest_requests(self):
        all_requests = []
        for line in self._get_lines_from_logs():
            match = self.LOG_LINE_PATTERN.search(string=line)
            if match:
                all_requests.append(
                    {
                        "method": match.group(2),
                        "url": match.group(3),
                        "ip": match.group(1),
                        "duration": int(match.group(5))
                    }
                )
        top_10_longest = sorted(all_requests, key=lambda d: d["duration"], reverse=True)[0:10]
        return top_10_longest

    def get_top_10_client_error_requests(self):
        client_error_requests = []
        for line in self._get_lines_from_logs():
            match = self.LOG_LINE_PATTERN.search(string=line)
            if match:
                if 400 <= int(match.group(4)) < 500:
                    client_error_requests.append(
                        {
                            "method": match.group(2),
                            "url": match.group(3),
                            "status": int(match.group(4)),
                            "ip": match.group(1),
                            "duration": int(match.group(5))
                        }
                    )
        url_and_status = {f'{error.get("url")} === {error.get("status")}' for error in client_error_requests}

        res_list = []
        for us in url_and_status:
            res_list.append(
                {
                    "url": us.split(sep=" === ")[0],
                    "status": us.split(sep=" === ")[1]
                }
            )
        if len(res_list) > 10:
            res_list = res_list[0:10]
        return res_list

    def get_top_10_server_error_requests(self):
        server_error_requests = []
        for line in self._get_lines_from_logs():
            match = self.LOG_LINE_PATTERN.search(string=line)
            if match:
                if 500 <= int(match.group(4)) < 600:
                    server_error_requests.append(
                        {
                            "method": match.group(2),
                            "url": match.group(3),
                            "status": int(match.group(4)),
                            "ip": match.group(1),
                        }
                    )
        url_and_status = {f'{error.get("url")} === {error.get("status")}' for error in server_error_requests}

        res_list = []
        for us in url_and_status:
            res_list.append(
                {
                    "url": us.split(sep=" === ")[0],
                    "status": us.split(sep=" === ")[1]
                }
            )
        if len(res_list) > 10:
            res_list = res_list[0:10]
        return res_list


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        prog="log_parser",
    )
    arg_parser.add_argument(
        "--input",
        action="store",
        help="Path to directory with log files or path to specific log file"
    )
    args = arg_parser.parse_args()

    logs_parser = LogsParser(logs_source=args.input, json_file="report.json")
    logs_parser.save_report()
