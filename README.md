# AI-GEN using TensorFlow and FastAPI

=================================================================
|            Cài đặt các thư viện cần thiết với pip             |
=================================================================
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
   - Chạy chương trình để thu thập dataset tự động.
   - Khuyến khích lấy ít dữ liệu hơn so với phương pháp auto.
   - Có thể chỉnh sửa số lượng dữ liệu trong biến "number_of_each".

2. Write
   - Tạo file CSV để lọc và xử lý dữ liệu từ dataset thu thập được.

3. Chỉnh tay
   - Sử dụng file `pre_dataset.csv`.
   - Kiểm tra xem ảnh có thể thêm tag (nhãn) nào ngoài các tag có sẵn hay không.
   - Thêm tag cho ảnh bằng cách thêm dấu phẩy "," và tên tag phía sau.
   - Tag phải nằm trong danh sách nhãn được định nghĩa trong `labels.py`.
   - Nên gán nhiều tag cho một ảnh để tăng độ chính xác của AI.

4. Rewrite
   - Chạy chương trình để chuyển đổi `pre_dataset.csv` thành `pro_dataset.csv` dùng cho AI học.

5. Train
   - Chạy chương trình để đọc `pro_dataset.csv` và huấn luyện mô hình, tạo file keras trong thư mục `model`.

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