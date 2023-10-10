from speed_test import SpeedTest

# Function to perform an upload speed test.
# Input: url - URL to which the file will be uploaded
#        file_path - Path to the file to be uploaded
# Output: upload_speed - upload speed in Mbps


# def upload_speed_test(upload_url):
#     with open("sample-2mb-text-file.txt", "rb") as file:
#         start_time = time.time()
#         # upload test is a post request, we are sending files to a destination and seeing how long it takes
#         response = requests.post(upload_url, files={"file": file})
#         end_time = time.time()

#         # If the upload was successful (HTTP status code 200)
#         if response.status_code != 200:
#             # Print an error message if the upload failed
#             print(f"Failed to upload file. Status Code: {response.status_code}")
#             return None

#         file_size = int(response.headers.get("content-length", 0))
#         upload_time = end_time - start_time
#         upload_speed = file_size / upload_time / (1024 * 1024)  # Mbps
#         return upload_speed


def main():
    url = "http://ipv4.download.thinkbroadband.com/5MB.zip"
    save_directory = "myproject"
    # file_path = "5MB.zip"

    # Perform the download speed test
    download = SpeedTest()
    download_speed = download.dowload_speed(url, save_directory)
    if download_speed:
        print(f"Download Speed: {download_speed:.2f} Mbps")

    # Perform the upload speed test
    upload = SpeedTest()
    upload_speed = upload.upload()
    if upload_speed:
        print(f"Upload Speed: {upload_speed:.2f} Mbps")


if __name__ == "__main__":
    main()


# what if I did a speed a speed test project that actually has an open MQTT connection to a device and monitors the connections constantly in intervals of 5 minutes or even
