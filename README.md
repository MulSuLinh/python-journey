# OpenClaw — Trợ lý AI cá nhân mã nguồn mở

> Bản dịch/tóm lược tiếng Việt từ [repository chính thức OpenClaw](https://github.com/openclaw/openclaw). Đây là tài liệu tham khảo trong repository học tập này, không phải bản phát hành chính thức của OpenClaw.

OpenClaw là trợ lý AI mã nguồn mở có thể chạy trên máy tính hoặc máy chủ do bạn quản lý. Nó kết nối với các ứng dụng nhắn tin và điều phối các phiên làm việc thông qua một **Gateway** trung tâm.

## Tính năng chính

- **Kết nối nhiều nền tảng:** hỗ trợ các kênh như Discord, iMessage, Slack, Microsoft Teams, Telegram, WhatsApp và nhiều nền tảng khác.
- **Tự quản lý dữ liệu:** trạng thái, bộ nhớ và thông tin xác thực có thể được lưu trên phần cứng do bạn quản lý.
- **Gateway trung tâm:** điều phối kết nối và các phiên làm việc của trợ lý.
- **Có thể mở rộng:** cho phép lựa chọn mô hình AI, công cụ và plugin.
- **Ứng dụng đồng hành:** dự án có các ứng dụng cho macOS, iOS, Android, Windows và Linux; tính năng cụ thể phụ thuộc từng nền tảng.

## Cài đặt

> Hãy đọc hướng dẫn chính thức trước khi cài đặt và kiểm tra yêu cầu hệ thống mới nhất tại https://docs.openclaw.ai/.

### macOS, Linux hoặc WSL2

Mở terminal và chạy lệnh cài đặt do dự án cung cấp:

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

### Windows PowerShell

Mở PowerShell và chạy:

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

### Cài qua npm

Nếu Node.js đáp ứng phiên bản mà tài liệu chính thức yêu cầu, có thể cài bằng:

```bash
npm install -g openclaw@latest --allow-scripts=openclaw
```

## Bắt đầu nhanh

Sau khi cài đặt, chạy trình hướng dẫn cấu hình:

```bash
openclaw onboard --install-daemon
```

Kiểm tra trạng thái Gateway:

```bash
openclaw gateway status
```

Mở giao diện điều khiển:

```bash
openclaw dashboard
```

Nếu lệnh hoặc yêu cầu phiên bản đã thay đổi, hãy ưu tiên hướng dẫn trong [tài liệu chính thức](https://docs.openclaw.ai/).

## Các thành phần chính

| Thành phần | Vai trò |
|---|---|
| **Gateway** | Điểm điều phối trung tâm cho các kết nối và phiên làm việc. |
| **Control UI** | Giao diện để quản lý và tương tác với Gateway. |
| **Channels** | Các nền tảng nhắn tin được kết nối với trợ lý. |
| **Models** | Mô hình AI được cấu hình để xử lý yêu cầu. |
| **Plugins và tools** | Bổ sung khả năng và tích hợp với những hệ thống khác. |
| **Companion apps / nodes** | Ứng dụng hoặc thiết bị đồng hành tùy nền tảng. |

## Bảo mật

OpenClaw có thể tương tác với tin nhắn, công cụ và môi trường máy tính của bạn. Vì vậy:

- Xem tin nhắn đến từ người khác là **dữ liệu không đáng tin cậy**.
- Kiểm tra quyền của công cụ và cấu hình sandbox trước khi cho phép thực thi tác vụ.
- Không công khai Gateway ra Internet nếu chưa hiểu rõ các rủi ro và biện pháp bảo vệ.
- Không chia sẻ khóa API, mật khẩu hoặc thông tin xác thực.
- Trước khi kết nối người dùng khác hoặc mở truy cập từ xa, hãy đọc [hướng dẫn bảo mật chính thức](https://docs.openclaw.ai/).

## Tài liệu và liên kết

- [Repository chính thức trên GitHub](https://github.com/openclaw/openclaw)
- [Tài liệu OpenClaw](https://docs.openclaw.ai/)
- [Trang chủ OpenClaw](https://openclaw.ai/)

## Phát triển từ mã nguồn

Các bước tổng quát được tài liệu dự án hướng dẫn:

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm build
pnpm ui:build
```

Repository sử dụng pnpm workspace; hãy xem tài liệu chính thức để biết phiên bản Node.js/pnpm được hỗ trợ và các bước phát triển cập nhật.

## Giấy phép

Dự án OpenClaw được phát hành theo giấy phép MIT. Hãy kiểm tra tệp LICENSE trong [repository chính thức](https://github.com/openclaw/openclaw) để biết điều khoản áp dụng.

---

*Tài liệu tiếng Việt này được viết để hỗ trợ việc đọc hiểu. Tài liệu chính thức bằng tiếng Anh và repository nguồn là nơi cần ưu tiên khi có khác biệt hoặc thông tin cập nhật.*
