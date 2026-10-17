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

- **⚡ 1-Click Khởi chạy Tự Phục Hồi (`Start-MinoTMProxy.bat`):** Tự động phát hiện môi trường Python, tự cài đặt thư viện thiếu. Nếu máy thiếu Python hoặc gặp lỗi thư viện C++, tool tự động tải môi trường Python 3.12 độc lập siêu tốc qua `uv` và chạy ngay không cần cài đặt gì thêm.
- **🎨 Giao diện Dual-Mode Siêu Đẹp (Cyber Dark / Light Tech):**
  - **Cyber Dark Enclave (Mặc định):** Tông màu không gian sâu (`#07090e`), neon cyan/emerald phát sáng tinh tế, font JetBrains Mono sắc nét.
  - **Light Tech Laboratory:** Chế độ sáng sang trọng, độ tương phản cao, dịu mắt và chuyên nghiệp.
  - Chuyển đổi 1 chạm bằng nút trên thanh công cụ hoặc phím tắt **`Alt + T`**.
- **🛠️ Tối ưu hóa Ribbon & Thanh Công Cụ Chuẩn DevTools:**
  - Đồng bộ chiều cao chuẩn `32px` cho tất cả các ô nhập (`Search`, `Highlight`, `Intercept`) và nút hành động (`Resume All`).
  - Thanh thao tác Flow (Replay, Duplicate, Revert, Delete, Mark, Download, Export, Resume, Abort) dạng thanh ngang hiện đại, không bị nhảy khung.
  - Nút **Quickaction** (Replay/Resume ở cuối dòng) chuyển màu hover êm ái (`#e0f2fe` ở Light Mode, neon cyan ở Dark Mode), không bị chữ đen xì.
  - Khử 100% lỗi **Headers Clipping** & **Nested Scrollbars** (giá trị Cookie, CSP, Token dài tự xuống dòng mượt mà).
  - Bảng tra cứu Status Code có màu ngọc lục bảo (`200 OK`), hổ phách (`3xx Redirect`) và đỏ san hô (`4xx/5xx Error`) sắc nét.
- **📱 Hỗ trợ đầy đủ cho Điện thoại (Android & iOS):** Tự động nhận diện chính xác địa chỉ IP LAN thật của máy tính (bỏ qua card mạng ảo), cung cấp sẵn script bật/tắt proxy nhanh qua cáp ADB.
- **🔐 Tự Động Đồng Bộ & Cài Đặt Chứng Chỉ CA:** Tự động đồng bộ chứng chỉ SSL riêng của từng máy tính và hỗ trợ 1 chạm cài thẳng vào hệ thống `/system/etc/security/cacerts/` cho máy Android đã root.

---

## 📂 Cấu trúc thư mục

```text
MinoTMProxy/
│
├── main.py                     # [KHUYÊN DÙNG] Khởi chạy trực tiếp bằng Python với Live Request Log siêu rõ ràng
├── run.py                      # Alias ngắn gọn của main.py (python run.py)
├── Start-MinoTMProxy.bat       # Khởi động tool 1 chạm bằng file .bat cho Windows
├── requirements.txt            # Khai báo thư viện mitmproxy
├── README.md                   # Hướng dẫn sử dụng chi tiết
│
├── custom_web/                 # Gói giao diện Cyber / Light tùy biến
│   ├── modern-pro.css          # Master stylesheet tùy biến giao diện
│   ├── index.html              # Entry point HTML tích hợp topbar và theme
│   ├── theme.js                # Xử lý đổi theme (Alt+T) và Resume All
│   └── apply_theme.py          # Script tự động gắn theme vào mitmproxy
│
├── scripts/                    # Bộ công cụ hỗ trợ proxy nhanh (Python & BAT)
│   ├── terminal_logger.py      # Bộ lọc in log request/response trực tiếp siêu rõ ràng trên console
│   ├── Bat-Proxy-Phone.py      # Bật proxy trên điện thoại tự động qua ADB (Python)
│   ├── Tat-Proxy-Phone.py      # Tắt proxy trên điện thoại qua ADB (Python)
│   ├── Bat-Proxy-Windows.py    # Bật proxy hệ thống Windows (Python, áp dụng ngay tức thì)
│   ├── Tat-Proxy-Windows.py    # Tắt proxy hệ thống Windows (Python)
│   ├── Bat-Proxy-Phone.bat     # Bật proxy điện thoại (file .bat)
│   ├── Tat-Proxy-Phone.bat     # Tắt proxy điện thoại (file .bat)
│   ├── Bat-Proxy-Windows.bat   # Bật proxy Windows (file .bat)
│   ├── Tat-Proxy-Windows.bat   # Tắt proxy Windows (file .bat)
│   ├── Cai-Cert-Android-Root.bat # Cài chứng chỉ CA vào Android /system (Root)
│   ├── get_ip.py               # Tự động dò IP LAN chính xác của máy tính
│   └── sync_certs.py           # Tự động đồng bộ và nạp chứng chỉ CA qua ADB
│
└── certificates/               # Thư mục chứng chỉ SSL/CA
    ├── mitmproxy-ca-cert.cer   # Chứng chỉ cho Windows / Android User
    ├── mitmproxy-ca-cert.pem   # Chứng chỉ định dạng PEM
    ├── c8750f0d.0              # Chứng chỉ định dạng Android System Root CA
    └── HD-Cai-Chung-Chi.txt    # Hướng dẫn cài đặt chứng chỉ chi tiết
```

---

## 🚀 Hướng dẫn sử dụng nhanh (Quick Start)

### Cách 1: Khởi chạy bằng Python (Khuyên Dùng — Log CMD Siêu Rõ Ràng)
Mở cửa sổ dòng lệnh và chạy:
```bash
python main.py
# hoặc:
python run.py
```
- Tool sẽ tự động nhận diện điện thoại Android cắm cáp USB (ADB) và tự động bật proxy.
- Trình duyệt tự mở trang Web UI tại: **`http://127.0.0.1:8081/?token=123`** (Mật khẩu: `123`).
- Toàn bộ request/response sẽ được **in trực tiếp theo thời gian thực (Live Request Log)** trên cửa sổ CMD cực kỳ rõ ràng, kèm thời gian, HTTP method, status code và URL!

### Cách 2: Khởi chạy 1-Click bằng file `.bat`
Nhấp đúp chuột vào file **`Start-MinoTMProxy.bat`**.

---

### Bước 2: Bắt gói tin trên Điện thoại (Android & iOS)

#### 1. Đặt Proxy trên điện thoại:
- **Tự động 100% (Android cắm cáp USB bật ADB):**
  - Tool `main.py` sẽ **tự động nhận diện và cấu hình proxy qua USB** khi khởi động!
  - Hoặc chạy riêng: `python scripts/Bat-Proxy-Phone.py`
- **Cách thủ công qua Wi-Fi (Android & iPhone):**
  - Đảm bảo điện thoại và máy tính kết nối **chung một mạng Wi-Fi**.
  - Vào **Cài đặt Wi-Fi** trên điện thoại -> Chọn Wi-Fi đang dùng -> **Chỉnh sửa / Nâng cao**.
  - Phần **Proxy** chọn **Thủ công (Manual)**:
    - **Tên máy chủ proxy (Host):** Nhập IP máy tính (in trên cửa sổ tool, ví dụ: `192.168.1.14`).
    - **Cổng (Port):** `8080`.
  - Nhấn **Lưu**.

#### 2. Cài đặt chứng chỉ SSL/HTTPS:
- Mở trình duyệt trên điện thoại truy cập: **`http://mitm.it`**
- Chọn hệ điều hành máy bạn (**Android** hoặc **Apple**):
  - **Với iPhone:** Tải hồ sơ -> Vào Cài đặt -> Cài đặt hồ sơ -> Vào *Cài đặt chung > Giới thiệu > Cài đặt tin cậy chứng nhận* -> Bật **Tin cậy toàn bộ** cho mitmproxy.
  - **Với Android thường:** Tải file `.cer` về -> Vào *Cài đặt > Bảo mật > Chứng chỉ CA* -> Cài đặt file vừa tải.
  - **Với Android đã Root (bắt 100% app không bị chặn SSL):** 
    - Chạy script `scripts\Cai-Cert-Android-Root.bat`.
    - Hoặc cài Magisk Module **MagiskTrustUserCerts** / **AlwaysTrustUserCerts**.
    - Nếu app có SSL Pinning: Cài thêm **LSPosed** + module **TrustMeAlready** hoặc bypass bằng Frida.

---

### Bước 3: Bắt gói tin trên Máy tính (Windows PC)
- Muốn bắt request từ trình duyệt hoặc ứng dụng trên máy tính:
  - Chạy file: `python scripts/Bat-Proxy-Windows.py` (hoặc click `scripts\Bat-Proxy-Windows.bat`).
  - Cài đặt chứng chỉ gốc bằng cách nhấp đúp file `certificates\mitmproxy-ca-cert.cer` -> Cài vào mục **Trusted Root Certification Authorities**.
- Khi xong việc, chỉ cần chạy: `python scripts/Tat-Proxy-Windows.py` (hoặc `scripts\Tat-Proxy-Windows.bat`).

---

## 🛠️ Quản lý & Tắt Proxy khi không sử dụng
- **Tắt proxy trên điện thoại:** Chạy `python scripts/Tat-Proxy-Phone.py` (hoặc `scripts\Tat-Proxy-Phone.bat`).
- **Dừng công cụ:** Nhấn **`Ctrl + C`** trên cửa sổ CMD. Tool sẽ tự động tắt proxy trên điện thoại trước khi thoát.

---

## 📝 Bản quyền & Ghi công
- Phát triển và đóng gói bởi **minhnhatgithub**.
- Dựa trên nền tảng mã nguồn mở mạnh mẽ của **mitmproxy**.
