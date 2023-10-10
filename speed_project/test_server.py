# import requests
# import time


# def upload():
#     ave_speed = []

#     with open("text.txt", "rb") as data:
#         for _ in range(3):
#             files = {"files": ("text.txt", data)}
#             start_time = time.time()
#             # print(start_time)
#             response = requests.post("http://127.0.0.1:8000/upload", files=files)
#             end_time = time.time()
#             # print(end_time)

#             if response.status_code != 200:
#                 return (
#                     f"Unable to upload to the url, Status Code: {response.status_code}"
#                 )

#             file_size = len(open("text.txt", "rb").read()) / 1024  # convert bits to KB
#             # print(file_size)
#             upload_time = end_time - start_time
#             # print(upload_time)
#             upload_speed = (file_size / upload_time) / (1024 * 1024)  # convert KB to MB
#             ave_speed.append(upload_speed)
#             # print(upload_speed)
#             # print(ave_speed)
#     upload_speed = sum(ave_speed) / len(ave_speed)
#     print(upload_speed)
#     return upload_speed


# upload_speed = upload()
# if upload_speed:
#     print(f"Upload Speed: {upload_speed:.2f} mbps")
# requests.delete("http://127.0.0.1:8000/upload")
