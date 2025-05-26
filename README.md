# AI-GEN using TensorFlow and FastAPI

Dự án AI-GEN sử dụng TensorFlow và FastAPI để huấn luyện và triển khai mô hình phân loại ảnh đa nhãn, kết hợp với crawler để thu thập dữ liệu từ Google.

## Tài Nguyên Và HDSD

---------------- Cài đặt thư viện ----------------
```bash
# Backend API
pip install fastapi uvicorn python-multipart

# TensorFlow & xử lý ảnh
pip install tensorflow pillow numpy

# Xử lý dữ liệu & mô hình
pip install scikit-learn pandas

# Cào ảnh từ Google
pip install icrawler


=================================================================
|                   Huấn Luyện TensorFlow                       |
=================================================================
1. Crawler
   - Chạy chương trình để thu thập dataset tự động (images).
   - Khuyến khích lấy ít dữ liệu vì cần chỉnh sửa thủ công:
      5 dữ liệu cho mỗi label.
   - Có thể chỉnh sửa số lượng dữ liệu trong biến "number_of_each".

2. Write
   - Tạo file CSV để lọc và xử lý dữ liệu từ dataset thu thập được.
      Dữ liệu mẫu, không đầy đủ.

3. Điều chỉnh
   - Sử dụng file `pre_dataset.csv`.
   - Kiểm tra xem ảnh có thể thêm tag (nhãn) nào ngoài các tag có sẵn hay không.
   - Thêm tag cho ảnh bằng cách thêm dấu phẩy "," và tên tag phía sau.
   - Tag phải nằm trong danh sách nhãn được định nghĩa trong `labels.py`.
   - Nên gán nhiều tag cho một ảnh để tăng độ chính xác của AI sau khi học.

4. Rewrite
   - Chạy chương trình để chuyển đổi `pre_dataset.csv` thành `pro_dataset.csv`:
      Là dữ liệu AI có thể học được.

5. Train
   - Chạy chương trình để đọc `pro_dataset.csv` và huấn luyện mô hình, tạo file keras trong thư mục `model`.


* Các bước dưới chỉ dùng cho kiểm tra đầu ra của AI,
* Không phục vụ cho việc học máy.

6. Chạy server
   - Mở terminal và chạy lệnh sau để khởi động server:
         uvicorn main:app --reload

7. Check
   - Kiểm tra ảnh đầu vào có hợp lệ không.

8. Predict
   - AI đọc ảnh mẫu, phân tích và trả về kết quả dưới dạng JSON.


=================================================================
|                            UPDATE                             |
=================================================================
25/05/2025
   -suffix crawler
      cào ảnh ít bị trùng lặp hơn mỗi lần cào
   -ensemble learning
      phương pháp kết hợp hiệu quả nhiều file keras để có kết quả tốt hơn
   -json returning
      predict bây giờ sẽ trả về JSON


=================================================================
|                         UP COMMING                            |
=================================================================
   -predict write 
      chương trình write set up tự động sử dụng chính AI để predict label
      vẫn cần kiểm tra lại độ chính xác của predict để tăng độ chính xác của dữ liệu
   -automatic server
      chạy server không cần lệnh
            uvicorn main:app --reload