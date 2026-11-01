# HỆ THỐNG CƠ SỞ TRI THỨC (KNOWLEDGE-BASED SYSTEMS)
### Học phần: Các Hệ Cơ Sở Tri Thức - Chương trình Cao học CNTT
**Học viên:** Dương Tùng Lâm | **MSSV:** 2500444 | **Lớp:** CNTT 20.2  
**Kho lưu trữ GitHub:** [Lamdt198/delightful-mendeleev](https://github.com/Lamdt198/delightful-mendeleev)

---

## 📌 Giới thiệu dự án

Dự án này hiện thực hóa hai phân hệ nền tảng của môn học Các Hệ Cơ Sở Tri Thức:
1. **Hệ chuyên gia Suy diễn lùi (Backward Chaining Inference Engine):** Hiện thực giải thuật suy luận hướng đích 4 bước chuẩn hóa, hỗ trợ đệ quy chứng minh đích con và truy vết cây chứng minh (Proof Tree Trace).
2. **Pipeline Tiền xử lý & Chuẩn hóa Dữ liệu Tri thức Văn bản tiếng Việt:** Xử lý triệt để 4 vấn đề lớn của dữ liệu web: rác HTML/Boilerplate, ngắt câu gãy từ viết tắt (`Tp. HCM`, `GS. TS`), xung đột mã ký tự Unicode (NFC vs NFD), và bảo toàn thực thể ngữ nghĩa định danh (NER).

---

## 📂 Danh mục tài liệu và mã nguồn

| Tệp tin | Định dạng | Mô tả nội dung |
|:---|:---:|:---|
| 📄 **[BAO_CAO_HE_CO_SO_TRI_THUC.docx](BAO_CAO_HE_CO_SO_TRI_THUC.docx)** | Word (.docx) | **Báo cáo chuẩn Đồ án Cao học** (có trang bìa trường, bảng biểu chuẩn mực, ma trận kiểm thử 10 test cases, phân tích truy vết suy diễn). |
| 📑 **[BAO_CAO_HE_CO_SO_TRI_THUC.md](BAO_CAO_HE_CO_SO_TRI_THUC.md)** | Markdown | Toàn văn báo cáo kỹ thuật phần mềm, tích hợp biểu đồ luồng Mermaid và bảng kiểm thử. |
| 🐍 **[demo_suy_dien_lui.py](demo_suy_dien_lui.py)** | Python Script | Động cơ suy diễn lùi (Backward Chaining Engine) với bài toán chẩn đoán y tế 5 luật. |
| 🐍 **[demo_tien_xu_ly_van_ban.py](demo_tien_xu_ly_van_ban.py)** | Python Script | Pipeline 4 công đoạn làm sạch và chuẩn hóa văn bản tiếng Việt. |
| 📓 **[demo_interactive.ipynb](demo_interactive.ipynb)** | Jupyter Notebook | Sổ tay thực nghiệm trực quan, chạy và quan sát kết quả theo từng ô mã lệnh. |
| ⚙️ **[requirements.txt](requirements.txt)** | Text | Danh mục các thư viện phụ thuộc của môi trường thực thi. |
| 🧪 **[test_env.py](test_env.py)** | Python Script | Script kiểm tra nhanh phiên bản các thư viện và môi trường máy tính. |
| 🛠️ **[generate_report.py](generate_report.py)** | Python Script | Bộ tạo tài liệu Word tự động dựa trên mẫu bìa chuẩn Cao học. |

---

## 🚀 Hướng dẫn cài đặt và thực thi

### 1. Cài đặt các thư viện cần thiết
```powershell
pip install -r requirements.txt
```

### 2. Chạy Demo Suy diễn lùi (Backward Chaining)
```powershell
python demo_suy_dien_lui.py
```

### 3. Chạy Demo Tiền xử lý & Chuẩn hóa văn bản
```powershell
python demo_tien_xu_ly_van_ban.py
```

### 4. Mở Sổ tay tương tác Jupyter Notebook
```powershell
jupyter notebook demo_interactive.ipynb
# Hoặc mở trực tiếp file demo_interactive.ipynb trên VS Code
```

### 5. Tạo lại Báo cáo Word chuẩn
```powershell
python generate_report.py
```

---

## 📊 Ma trận Kiểm thử Thực nghiệm (10 Test Cases - 100% PASS)

Hệ thống đã trải qua 10 kịch bản kiểm thử toàn diện từ đơn vị đến tích hợp:
- **TC-01 đến TC-05:** Kiểm thử Động cơ suy diễn lùi (đích có sẵn trong WM, suy diễn trực tiếp, suy diễn chuỗi bắc cầu đa tầng, mục tiêu không thỏa mãn, xuất cây truy vết).
- **TC-06 đến TC-09:** Kiểm thử Pipeline tiền xử lý văn bản (bóc tách HTML, tách câu không gãy `Tp. HCM`/`GS. TS`, chuẩn hóa Unicode NFC vs NFD `hòa` != `hoà`, bảo toàn thực thể viết hoa `FPT`/`AI`).
- **TC-10:** Kiểm thử thực thi tương tác toàn diện trên Jupyter Notebook.
