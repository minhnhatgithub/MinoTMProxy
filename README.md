# 🚀 MinoTMProxy — Modern Dark Pro Traffic Inspector

<p align="center">
  <img src="https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/docs/src/static/logo.svg" width="90" alt="MinoTMProxy Logo">
</p>

<p align="center">
  <b>Bản phân phối tùy biến mitmproxy Web UI với giao diện Dark Pro hiện đại, đẳng cấp như Reqable & Proxyman.</b><br>
  <i>Chỉ cần tải về và nhấp đúp là chạy ngay — Bắt request HTTPS mượt mà trên Điện thoại & Máy tính!</i>
</p>

---

## ✨ Điểm nổi bật của MinoTMProxy

- **⚡ 1-Click Khởi chạy (`Start-MinoTMProxy.bat`):** Tự động phát hiện môi trường, tự cài đặt thư viện thiếu, tự động patch giao diện Dark Pro và mở trình duyệt trực tiếp.
- **🎨 Giao diện Dark Theme Pro:** Lấy cảm hứng từ Linear, GitHub Dark và Chrome DevTools. Tông màu sâu êm mắt (`#0b0e14`), font monospaced JetBrains sắc sảo, độ tương phản cao, làm việc ban đêm không mỏi mắt.
- **🛠️ Đã sửa triệt để các lỗi giao diện gốc:**
  - Khử 100% lỗi **Headers Clipping** & **Nested Scrollbars** (giá trị Cookie, CSP, Token dài tự xuống dòng mượt mà).
  - Khắc phục lỗi che khuất nút **Quickactions** (nút Replay / Resume có ô chuyên dụng `38px`, căn giữa sắc nét).
  - Bảng tra cứu Status Code có màu ngọc lục bảo (`200 OK`), hổ phách (`3xx Redirect`) và đỏ san hô (`4xx/5xx Error`) rực rỡ.
  - Splitter phân chia bảng luồng và bảng chi tiết mượt mà, dễ kéo thả.
- **📱 Hỗ trợ đầy đủ cho Điện thoại (Android & iOS):** Tự động nhận diện địa chỉ IP mạng LAN của máy tính, cung cấp sẵn script bật/tắt proxy nhanh qua cáp ADB.
- **🔐 Đi kèm bộ chứng chỉ CA & Script Root:** Tích hợp sẵn chứng chỉ CA và script đẩy chứng chỉ vào hệ thống `/system/etc/security/cacerts/` cho máy Android đã root.

---

## 📂 Cấu trúc thư mục

```text
MinoTMProxy/
│
├── Start-MinoTMProxy.bat       # [CLICK VÀO ĐÂY] Khởi động tool 1 chạm
├── requirements.txt            # Danh sách thư viện phụ thuộc
├── README.md                   # Hướng dẫn sử dụng chi tiết
│
├── custom_web/                 # Gói giao diện Dark Pro tùy biến
│   ├── modern-pro.css          # Master stylesheet tùy biến giao diện
│   ├── index.html              # Entry point HTML đã tích hợp theme
│   └── apply_theme.py          # Script tự động gắn theme vào mitmproxy
│
├── scripts/                    # Bộ công cụ hỗ trợ proxy nhanh
│   ├── Bat-Proxy-Phone.bat     # Bật proxy trên điện thoại tự động qua ADB
│   ├── Tat-Proxy-Phone.bat     # Tắt proxy trên điện thoại
│   ├── Bat-Proxy-Windows.bat   # Bật proxy hệ thống Windows
│   ├── Tat-Proxy-Windows.bat   # Tắt proxy hệ thống Windows
│   └── Cai-Cert-Android-Root.bat # Cài chứng chỉ CA vào Android /system (Root)
│
└── certificates/               # Thư mục chứng chỉ SSL/CA
    ├── mitmproxy-ca-cert.cer   # Chứng chỉ cho Windows / Android User
    ├── mitmproxy-ca-cert.pem   # Chứng chỉ định dạng PEM
    ├── c8750f0d.0              # Chứng chỉ định dạng Android System Root CA
    └── HD-Cai-Chung-Chi.txt    # Hướng dẫn cài đặt chứng chỉ chi tiết
```

---

## 🚀 Hướng dẫn sử dụng nhanh (Quick Start)

### Bước 1: Khởi động công cụ
Nhấp đúp chuột vào file **`Start-MinoTMProxy.bat`**.
- Tool sẽ tự động kiểm tra Python và mitmproxy.
- Trình duyệt sẽ tự động mở trang quản lý traffic tại: **`http://127.0.0.1:8081/?token=123`**
- Mật khẩu đăng nhập (nếu hỏi): `123`
- Tool sẽ hiển thị rõ IP máy tính của bạn trong mạng LAN (ví dụ: `192.168.1.101`).

---

### Bước 2: Bắt gói tin trên Điện thoại (Android & iOS)

#### 1. Đặt Proxy trên điện thoại:
- **Cách tự động (Dành cho Android cắm cáp USB có bật ADB):**
  - Chạy file `scripts\Bat-Proxy-Phone.bat` -> Xong ngay lập tức!
- **Cách thủ công (Android & iPhone):**
  - Đảm bảo điện thoại và máy tính kết nối **chung một mạng Wi-Fi**.
  - Vào **Cài đặt Wi-Fi** trên điện thoại -> Nhấn vào mạng Wi-Fi đang kết nối -> Chọn **Chỉnh sửa / Nâng cao**.
  - Phần **Proxy** chọn **Thủ công (Manual)**:
    - **Tên máy chủ proxy (Host):** Nhập IP máy tính (được in trên cửa sổ tool, ví dụ: `192.168.1.101`).
    - **Cổng (Port):** `8080`.
  - Nhấn **Lưu**.

#### 2. Cài đặt chứng chỉ SSL/HTTPS:
- Sau khi đã kết nối Proxy, mở trình duyệt trên điện thoại truy cập vào: **`http://mitm.it`**
- Chọn hệ điều hành máy bạn (**Android** hoặc **Apple**):
  - **Với iPhone:** Tải hồ sơ -> Vào Cài đặt -> Cài đặt hồ sơ -> Vào *Cài đặt chung > Giới thiệu > Cài đặt tin cậy chứng nhận* -> Bật công tắc **Tin cậy toàn bộ** cho mitmproxy.
  - **Với Android thường:** Tải file `.cer` về -> Vào *Cài đặt > Bảo mật > Cài đặt nâng cao > Cài đặt từ bộ nhớ > Chứng chỉ CA* -> Chọn cài đặt file vừa tải.
  - **Với Android đã Root (bắt 100% app không bị chặn SSL):** 
    - Chạy script `scripts\Cai-Cert-Android-Root.bat`.
    - Hoặc cài Magisk Module **MagiskTrustUserCerts** / **AlwaysTrustUserCerts**.
    - Nếu app có SSL Pinning: Cài thêm **LSPosed** + module **TrustMeAlready** hoặc bypass bằng Frida.

---

### Bước 3: Bắt gói tin trên Máy tính (Windows PC)
- Muốn bắt request của trình duyệt hoặc các ứng dụng trên máy tính:
  - Chạy file `scripts\Bat-Proxy-Windows.bat`.
  - Cài đặt chứng chỉ gốc bằng cách nhấp đúp file `certificates\mitmproxy-ca-cert.cer` -> Cài vào mục **Trusted Root Certification Authorities**.
- Khi xong việc, chỉ cần chạy file `scripts\Tat-Proxy-Windows.bat` để trở về mạng bình thường.

---

## 🛠️ Quản lý & Tắt Proxy khi không sử dụng
- **Tắt proxy trên điện thoại:** Chạy `scripts\Tat-Proxy-Phone.bat` hoặc chuyển proxy Wi-Fi về `None / Không có`.
- **Dừng công cụ:** Đóng cửa sổ dòng lệnh `Start-MinoTMProxy.bat`.

---

## 📝 Bản quyền & Ghi công
- Phát triển và đóng gói bởi **minhnhatgithub**.
- Dựa trên nền tảng mã nguồn mở mạnh mẽ của **mitmproxy**.
