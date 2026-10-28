# Mộc Coffee — Website demo

Website giới thiệu và bán hàng mẫu cho thương hiệu cà phê **Mộc Coffee**. Dự án sử dụng HTML, CSS và JavaScript thuần trong một file `index.html`, phù hợp để học và trình diễn giao diện web cơ bản.

## 🌐 Liên kết

- **Website GitHub Pages:** https://mulsulinh.github.io/python-journey/projects/moc-coffee/
- **Mã nguồn website:** [index.html](./index.html)
- **Repository đang chứa dự án:** [MulSuLinh/python-journey](https://github.com/MulSuLinh/python-journey)
- **Repository nguồn ban đầu:** [MulSuLinh/openclaw](https://github.com/MulSuLinh/openclaw)

> Đường dẫn GitHub Pages chỉ hoạt động sau khi bật Pages và GitHub triển khai thành công. Nếu chưa mở được, vào **Settings → Pages**, chọn **Deploy from a branch**, nhánh `main`, thư mục `/(root)`, rồi lưu và chờ triển khai.

## ✨ Website hiện có những gì?

### Giao diện
- Trang giới thiệu thương hiệu Mộc Coffee bằng tiếng Việt.
- Thanh điều hướng đến phần sản phẩm, giới thiệu và đặt hàng.
- Khu vực mở đầu có tiêu đề, mô tả và nút xem sản phẩm.
- Khu vực giới thiệu các cam kết của thương hiệu.
- Chân trang hiển thị tên thương hiệu và năm hiện tại.
- Tông màu cà phê, kem và vàng; thẻ sản phẩm có hình ảnh, tên, mô tả và giá.

### Sản phẩm
- Có **22 sản phẩm mẫu** thuộc 3 nhóm:
  - Cà phê hạt & bột.
  - Cà phê tiện lợi.
  - Dụng cụ pha chế.
- Có nút lọc để xem tất cả hoặc từng nhóm sản phẩm.
- Danh sách sản phẩm được tạo bằng JavaScript từ dữ liệu trong file.

### Giỏ hàng
- Thêm sản phẩm vào giỏ.
- Tăng số lượng khi thêm cùng một sản phẩm nhiều lần.
- Giảm số lượng hoặc loại sản phẩm khỏi giỏ.
- Tự cập nhật số lượng món trên nút giỏ hàng.
- Tự tính thành tiền từng sản phẩm và tổng tiền.

### Tạo đơn hàng demo
- Biểu mẫu nhập tên người nhận, số điện thoại, địa chỉ và ghi chú.
- Kiểm tra giỏ hàng có sản phẩm trước khi tạo nội dung đơn.
- Tổng hợp thông tin khách hàng, sản phẩm, số lượng và tổng tiền thành văn bản.
- Có nút sao chép nội dung đơn hàng để người dùng tự gửi.

### Hiển thị trên nhiều thiết bị
- Có CSS responsive cho màn hình máy tính, máy tính bảng và điện thoại.
- Ẩn một số liên kết điều hướng trên màn hình nhỏ và thay đổi số cột sản phẩm theo kích thước màn hình.
- Ảnh sản phẩm lấy từ Unsplash nên cần Internet để tải ảnh.

## 🧰 Công nghệ

| Công nghệ | Vai trò |
|---|---|
| HTML5 | Cấu trúc trang, nội dung và biểu mẫu |
| CSS3 | Màu sắc, bố cục, thẻ sản phẩm và responsive |
| JavaScript | Hiển thị/lọc sản phẩm, giỏ hàng, tính tiền và tạo nội dung đơn hàng |
| GitHub | Lưu trữ mã nguồn và theo dõi lịch sử thay đổi |
| GitHub Pages | Có thể xuất bản website tĩnh |

Bản hiện tại không cần cài thư viện hoặc framework JavaScript.

## 🗂️ Cấu trúc thư mục

```text
projects/
└── moc-coffee/
    ├── README.md
    └── index.html
```

CSS và JavaScript đang nằm bên trong `index.html`, chưa được tách thành file riêng.

## 🕘 Nhật ký thay đổi từ đầu phiên làm việc

Phần này ghi lại các thay đổi đã xác định được trong GitHub và các bước đã thực hiện cho dự án Mộc Coffee. Những chức năng liệt kê ở phần trên đã có sẵn trong mã nguồn khi chuyển dự án; không nên hiểu rằng tất cả đều được lập trình mới trong phiên này.

### Bước 1 — Đưa website vào repository học tập
- Lấy file website từ `website-ca-phe/index.html` trong repository `MulSuLinh/openclaw`.
- Sao chép file sang đường dẫn `projects/moc-coffee/index.html` trong repository `MulSuLinh/python-journey`.
- Giữ file nguồn ở repository ban đầu; thao tác này thêm một bản vào repository học tập, không phải di chuyển xóa file nguồn.
- Kiểm tra nội dung file sau khi sao chép. Mã nguồn đích có cùng nội dung với file nguồn tại thời điểm kiểm tra, vì vậy chưa có bằng chứng cho thấy giao diện hoặc chức năng trong HTML đã được sửa trong bước chuyển.

**Commit:** [Add Mộc Coffee website demo](https://github.com/MulSuLinh/python-journey/commit/7dfa3793cc233ae00a663ecdeff7daa656c86e65)

### Bước 2 — Kiểm tra và ghi nhận chức năng hiện có
- Xem lại mã HTML, CSS và JavaScript.
- Ghi nhận 22 sản phẩm mẫu, 3 danh mục, bộ lọc sản phẩm, giỏ hàng, tính tổng tiền, biểu mẫu và chức năng tạo/sao chép nội dung đơn hàng.
- Ghi nhận bố cục responsive, ảnh tải từ Unsplash và năm tự cập nhật ở chân trang.
- Ghi rõ các giới hạn: chưa có backend, cơ sở dữ liệu, lưu đơn hàng trên máy chủ, thanh toán hoặc quản trị cửa hàng.
- Đây là bước rà soát và mô tả mã nguồn; không phải một lần sửa tính năng đã được xác nhận trong `index.html`.

### Bước 3 — Tạo tài liệu README
- Thêm file `projects/moc-coffee/README.md`.
- Viết hướng dẫn về mục đích, tính năng, công nghệ, cấu trúc thư mục và cách chạy dự án.
- Bổ sung lịch sử thay đổi, giới hạn hiện tại và các hướng phát triển tiếp theo.
- Ghi đường dẫn GitHub Pages dự kiến cùng lưu ý rằng cần bật và kiểm tra trạng thái triển khai.

**Commit:** [Add README for Mộc Coffee website](https://github.com/MulSuLinh/python-journey/commit/48a27c5f74bbe54b50e3445ce4b8003820b11460)

### Trạng thái sau các bước trên
- [x] Có bản website tại `projects/moc-coffee/index.html`.
- [x] Có tài liệu hướng dẫn tại `projects/moc-coffee/README.md`.
- [x] Đã ghi lại hai commit liên quan đến việc thêm website và README.
- [ ] Chưa xác nhận website GitHub Pages đã triển khai và truy cập thành công.
- [ ] Chưa ghi nhận thay đổi mới về giao diện hoặc tính năng trong mã `index.html` kể từ khi sao chép.

## ▶️ Cách chạy

### Mở trực tiếp trên máy tính
1. Tải hoặc clone repository về máy.
2. Mở thư mục `projects/moc-coffee`.
3. Mở `index.html` bằng trình duyệt; hoặc dùng tiện ích Live Server trong VS Code.

### Xuất bản bằng GitHub Pages
1. Mở repository `MulSuLinh/python-journey`.
2. Vào **Settings → Pages**.
3. Trong **Build and deployment**, chọn **Deploy from a branch**.
4. Chọn nhánh `main` và thư mục `/(root)), sau đó nhấn **Save**.
5. Chờ GitHub triển khai xong rồi mở đường dẫn website ở đầu tài liệu.

## ⚠️ Giới hạn hiện tại

- Đây là **website demo tĩnh**, chưa phải cửa hàng trực tuyến hoàn chỉnh.
- Đơn hàng chỉ được tạo thành văn bản để sao chép; không tự gửi đến người bán và không lưu trên máy chủ.
- Chưa có cơ sở dữ liệu, đăng nhập, quản lý kho, quản lý đơn hàng hoặc trang quản trị.
- Chưa tích hợp cổng thanh toán, vận chuyển hay API backend.
- Giỏ hàng chỉ tồn tại trong bộ nhớ JavaScript của trang; tải lại trang có thể làm mất giỏ hàng.
- Tên, mô tả, giá và sản phẩm là dữ liệu mẫu; cần xác minh trước khi dùng cho kinh doanh thật.
- Ảnh lấy từ Unsplash nên cần Internet và có thể thay đổi theo nguồn ảnh.

## 🔜 Việc có thể làm tiếp

- [ ] Chỉnh sửa giao diện hoặc nội dung sản phẩm theo yêu cầu.
- [ ] Tách CSS và JavaScript khỏi file HTML để dễ bảo trì.
- [ ] Lưu giỏ hàng bằng `localStorage`.
- [ ] Thêm kiểm tra dữ liệu biểu mẫu tốt hơn.
- [ ] Kết nối backend và cơ sở dữ liệu để lưu đơn hàng thật.
- [ ] Xây dựng trang quản trị sản phẩm và đơn hàng.
- [ ] Tích hợp phương thức liên hệ, vận chuyển và thanh toán an toàn khi phù hợp.
- [ ] Xác minh trạng thái triển khai GitHub Pages.

---

**Trạng thái dự án:** Website demo tĩnh phục vụ học tập và trình diễn giao diện. Nhật ký thay đổi dựa trên các commit đã xác định; các thay đổi mới nên được bổ sung vào đây sau khi thực sự cập nhật mã nguồn.

## Trợ lý Mộc Coffee (bản demo)

Website có một khung chat nổi **“Hỏi Mộc AI”** ở góc dưới bên phải. Trợ lý có thể:
- Trả lời câu hỏi cơ bản về sản phẩm và giá mẫu.
- Gợi ý cà phê cho người mới dựa trên mô tả sản phẩm.
- Hướng dẫn thêm sản phẩm vào giỏ và tạo nội dung đơn hàng.
- Trả lời nhanh một số câu hỏi thường gặp về danh mục và giao hàng.

**Lưu ý kỹ thuật:** phiên bản hiện tại là trợ lý hỏi đáp theo từ khóa chạy ngay trong trình duyệt, không cần API key. Đây chưa phải mô hình AI tạo sinh; câu trả lời có giới hạn và không gửi đơn hàng đến cửa hàng. Muốn kết nối AI thật, cần xây dựng backend gọi nhà cung cấp mô hình và lưu khóa API ở phía máy chủ, không đặt khóa bí mật trực tiếp trong HTML/JavaScript công khai.

### Nhật ký cập nhật — Trợ lý chat
- Thêm nút chat nổi và cửa sổ trò chuyện có thể mở/đóng.
- Thêm câu hỏi gợi ý nhanh, ô nhập tin nhắn và phản hồi theo nhóm chủ đề.
- Bổ sung thông báo rõ ràng về giới hạn của bản demo.
- Đồng bộ phần giao diện trợ lý vào bản website-ca-phe trong openclaw và bản sao projects/moc-coffee trong python-journey.


## Quản lý bán hàng và chi tiêu

Mở trang [quan-ly.html](./quan-ly.html) để dùng bảng điều khiển quản lý Mộc Coffee.

- **Bán hàng:** ghi ngày bán, sản phẩm, số lượng, đơn giá, khách hàng/mã đơn và hình thức thanh toán; hệ thống tự tính thành tiền.
- **Chi tiêu:** ghi khoản chi, danh mục (nguyên liệu, mặt bằng, nhân sự, điện nước, vận chuyển, marketing...), số tiền và hình thức chi.
- **Báo cáo:** xem tổng doanh thu, tổng chi tiêu, chênh lệch thu–chi và số giao dịch theo khoảng ngày; có thể xuất CSV để lưu hoặc mở bằng bảng tính.
- **Lưu dữ liệu:** trình duyệt lưu dữ liệu trong `localStorage` trên thiết bị hiện tại.

**Giới hạn:** Đây là trang demo phía trình duyệt, chưa có tài khoản đăng nhập, máy chủ hay cơ sở dữ liệu chung. Dữ liệu không tự đồng bộ giữa máy tính/điện thoại và đơn đặt hàng ở trang cửa hàng chưa tự động nhập vào bảng bán hàng. Không dùng bản demo này làm sổ kế toán chính thức hoặc lưu thông tin nhạy cảm.
