import time
import requests
import os

#  I created a class for this just because I want clean code and I want to implement OOP into my work


class SpeedTest:
    def __init__(self):
        # create a list that will contain the previous three records of the speed tests
        self.speed_tests = []
        self.ave_speed = []

    # Function to perform a download speed test.
    # Input: url - URL of the file to download
    # Output: download_speed - download speed in Mbps

    def dowload_speed(self, url, save_directory):
        start_time = time.time()
        # print(start_time)
        response = requests.get(url)
        end_time = time.time()

        if response.status_code != 200:
            # Print an error message if the download failed
            print(f"Failed to download file. Status Code: {response.status_code}")
            return None
        # loop will run the download speed test 3 times and calucalte the average speed
        for _ in range(3):
            file_name = url.split("/")[-1]
            # print(file_name)
            file_path = os.path.join(save_directory, file_name)
            # print(file_path)
            file_size = int(response.headers.get("content-length", 0))
            # print(file_size)
            download_time = end_time - start_time
            # print(download_time)
            download_speed = file_size / download_time / (1024 * 1024)  # Mbps
            self.speed_tests.append(download_speed)

        avarage_value = float(sum(self.speed_tests))
        return avarage_value

    def upload(self):
        with open("text.txt", "rb") as data:
            for _ in range(3):
                files = {"files": ("text.txt", data)}
                start_time = time.time()
                # print(start_time)
                response = requests.post("http://127.0.0.1:8000/upload", files=files)
                end_time = time.time()
                # print(end_time)

                if response.status_code != 200:
                    return f"Unable to upload to the url, Status Code: {response.status_code}"

                file_size = (
                    len(open("text.txt", "rb").read()) / 1024
                )  # convert bits to KB
                # print(file_size)
                upload_time = end_time - start_time
                # print(upload_time)
                upload_speed = (file_size / upload_time) / (
                    1024 * 1024
                )  # convert KB to MB
                self.ave_speed.append(upload_speed)
                # print(upload_speed)
                # print(ave_speed)
        upload_speed = sum(self.ave_speed) / len(self.ave_speed)
        print(upload_speed)
        return upload_speed
