# Mộc Coffee — Website demo

Website giới thiệu và bán hàng mẫu cho thương hiệu cà phê **Mộc Coffee**. Dự án được viết bằng HTML, CSS và JavaScript thuần trong một file `index.html`, phù hợp để học cách xây dựng giao diện web cơ bản.

## 🌐 Xem website

- **Website GitHub Pages:** https://mulsulinh.github.io/python-journey/projects/moc-coffee/
- **Mã nguồn:** [index.html](./index.html)

> Nếu website chưa mở được, hãy kiểm tra mục **Settings → Pages** trong repository `python-journey` và chờ GitHub hoàn tất triển khai.

## ✨ Tính năng hiện có

- **Trang giới thiệu:** phần mở đầu, thông điệp thương hiệu và các mục điều hướng.
- **Danh sách 22 sản phẩm mẫu:** gồm cà phê hạt & bột, cà phê tiện lợi và dụng cụ pha chế.
- **Lọc sản phẩm theo danh mục:** xem tất cả sản phẩm hoặc lọc theo từng nhóm.
- **Giỏ hàng tương tác:** thêm sản phẩm, giảm số lượng/bỏ sản phẩm và tự tính số lượng cùng tổng tiền.
- **Biểu mẫu đặt hàng demo:** nhập tên người nhận, số điện thoại, địa chỉ và ghi chú.
- **Tạo và sao chép nội dung đơn hàng:** tổng hợp sản phẩm, số lượng và tổng tiền thành văn bản để người dùng sao chép.
- **Giao diện thích ứng:** bố cục thay đổi theo kích thước màn hình điện thoại và máy tính.
- **Hình ảnh sản phẩm:** sử dụng ảnh từ Unsplash; cần kết nối Internet để tải ảnh.
- **Hiển thị năm hiện tại:** năm ở chân trang tự cập nhật bằng JavaScript.

## 🧰 Công nghệ sử dụng

| Công nghệ | Vai trò |
|---|---|
| HTML5 | Cấu trúc nội dung và biểu mẫu |
| CSS3 | Màu sắc, bố cục, thẻ sản phẩm và giao diện responsive |
| JavaScript | Hiển thị/lọc sản phẩm, giỏ hàng, tính tổng tiền và tạo nội dung đơn hàng |
| GitHub | Lưu trữ mã nguồn và theo dõi thay đổi |
| GitHub Pages | Có thể dùng để xuất bản website tĩnh |

Không cần cài thư viện hay framework JavaScript để chạy bản demo hiện tại.

## 🗂️ Cấu trúc dự án

```text
projects/
└── moc-coffee/
    ├── README.md
    └── index.html
```

CSS và JavaScript hiện nằm trực tiếp bên trong `index.html`; dự án chưa tách thành các file riêng.

## 📋 Những thay đổi từ khi đưa website vào repository học tập

1. **Đưa website vào repository `python-journey`:** sao chép file `website-ca-phe/index.html` từ repository `openclaw` sang `projects/moc-coffee/index.html`.
2. **Giữ nguyên mã nguồn website khi chuyển:** bản `index.html` trong dự án này có cùng nội dung với file nguồn tại thời điểm sao chép; chưa ghi nhận chỉnh sửa tính năng mới trong lần chuyển này.
3. **Bổ sung tài liệu README:** mô tả tính năng, công nghệ, cách chạy và các giới hạn để người khác hiểu dự án.
4. **Chuẩn bị đường dẫn GitHub Pages:** dự án có thể được xuất bản như website tĩnh nếu Pages được bật và triển khai thành công.

> Lịch sử trên chỉ ghi nhận những thay đổi đã xác định được. Các cập nhật tiếp theo về giao diện hoặc chức năng nên được bổ sung vào mục này khi thực sự thay đổi mã nguồn.

## ▶️ Cách chạy

### Chạy trực tiếp trên GitHub Pages

1. Mở repository `MulSuLinh/python-journey`.
2. Vào **Settings → Pages**.
3. Trong **Build and deployment**, chọn **Deploy from a branch**.
4. Chọn nhánh `main` và thư mục `/(root)`, sau đó nhấn **Save**.
5. Sau khi triển khai xong, mở đường dẫn website ở phần đầu README.

### Chạy trên máy tính

1. Tải hoặc clone repository về máy.
2. Mở thư mục `projects/moc-coffee`.
3. Mở file `index.html` bằng trình duyệt; hoặc dùng tiện ích Live Server trong VS Code.

## ⚠️ Giới hạn hiện tại

- Đây là **bản demo giao diện**, chưa phải cửa hàng trực tuyến hoàn chỉnh.
- Đơn hàng chỉ được tạo thành văn bản để sao chép; **không gửi đến người bán và không được lưu trên máy chủ**.
- Chưa có cơ sở dữ liệu, tài khoản người dùng, quản lý kho, quản lý đơn hàng hoặc trang quản trị.
- Chưa tích hợp cổng thanh toán, vận chuyển hay API backend.
- Giỏ hàng lưu trong bộ nhớ JavaScript của trang; tải lại trang có thể làm mất giỏ hàng.
- Giá và sản phẩm là dữ liệu mẫu, cần xác minh trước khi sử dụng cho hoạt động kinh doanh thật.
- Ảnh tải từ Unsplash nên cần Internet và có thể thay đổi theo nguồn ảnh.

## 🔜 Hướng phát triển tiếp theo

- Lưu giỏ hàng bằng `localStorage`.
- Tách HTML, CSS và JavaScript thành các file riêng.
- Kết nối backend và cơ sở dữ liệu để lưu đơn hàng thật.
- Bổ sung trang quản trị sản phẩm và đơn hàng.
- Tích hợp phương thức liên hệ, vận chuyển và thanh toán an toàn khi cần.

---

**Trạng thái:** Website demo tĩnh phục vụ học tập và trình diễn giao diện.