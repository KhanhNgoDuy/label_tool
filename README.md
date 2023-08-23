# Set up
Phần mềm gán nhãn tự động sử dụng CLI.
Camera sử dụng để thu dữ liệu là Flir camera, cần cài thêm phần mềm SpinView để config camera (chỉnh độ sáng, tiêu cự, ...)

`https://www.flir.com/products/spinnaker-sdk/?vertical=machine+vision&segment=iis`

Cài thư viện PySpin để thu ảnh dùng Python

`pip install pyspin`

# Hướng dẫn sử dụng

* Khi thu dữ liệu thì chạy file `main.py`.
* Chọn tên cho folder bằng cách nhập vào command line. Tên thường đặt theo syntax s<n>_\<name\> với \<n\> là số thứ tự của folder, \<name\> là tên người thực hiện.
* Bấm "space" để bắt đầu thu dữ liệu. Bấm "a" khi bắt đầu thực hiện hành động và "b" khi kết thúc hành động.
* Hiện tại số hành động đang được để là 19. Sau khi thực hiện xong 19 hành động, bấm "space" để kết thúc 1 video. Sau khi bấm "space", 1 folder gồm file video.mp4 và annotation.csv sẽ được tạo ra.
* Nếu không bấm "space" khi kết thúc, video sẽ không xem được.
* Nếu không thực hiện đủ 19 hành động hoặc người bấm không bấm đủ 19 lần, chương trình sẽ gặp lỗi và không tạo file annotation.

# Pose Estimation bằng Mediapipe
Cài đặt Mediapipe

`pip install mediapipe`

Tải model pose estimation tại section Models:
* Hand Landmarker (21 hand joints):
  `https://developers.google.com/mediapipe/solutions/vision/hand_landmarker`
* Pose Landmarker (6 pose joints):
  `https://developers.google.com/mediapipe/solutions/vision/pose_landmarker`

Lưu các model đã tải vào folder `pose_estimation`. Sử dụng code trong notebook `extract_pose.ipynb` để trích xuất khớp xương từ video đã thu.

Mỗi video tạo ra 1 file `.npy`, là một tensor có kích thước $`T\times48\times3`$, với $T$ là số frame của video gốc.
