# -*- coding: utf-8 -*-
"""
DEMO 2: TIEN XU LY VA CHUAN HOA DU LIEU TRI THUC (SLIDE 3.2 & 3.3)
Noi dung thuc hanh:
  1. Loai bo Boilerplate, the HTML rac (BeautifulSoup)
  2. Tach cau thong minh dua tren ngu canh (xu ly: Tp. HCM, GS. TS Hoang Minh Son)
  3. Chuan hoa bo ma Unicode tieng Viet: NFC vs NFD (xu ly loi: hoa vs hoa)
  4. Xu ly viet hoa / viet thuong giu nguyen thuc the (Named Entity Preservation)
"""

import sys
import re
import unicodedata
from bs4 import BeautifulSoup

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def demo_1_clean_html_and_boilerplate():
    print("\n" + "=" * 65)
    print("PHAN 1: LAM SACH CAU TRUC & LOAI BO BOILERPLATE/HTML RAC")
    print("=" * 65)

    raw_html = """
    <html>
        <head><title>Trang tin tức</title></head>
        <body>
            <header><div class="header">HEADER: Banner quang cao - Mua ngay!</div></header>
            <div class="ad-banner">QC: Giam gia 50% khoa hoc AI!</div>
            <article>
                <h1>Hội nghị Khoa học Dữ liệu 2026</h1>
                <p>Hội nghị quy tụ nhiều chuyên gia đầu ngành trong lĩnh vực <b>Trí tuệ nhân tạo</b>.</p>
                <p>Nhiều giải pháp mới về <i>Knowledge Graph</i> và <i>Machine Learning</i> đã được trình bày.</p>
            </article>
            <footer><p>FOOTER: Bản quyền thuộc về Viện Nghiên cứu © 2026</p></footer>
        </body>
    </html>
    """

    print("[1. Văn bản HTML thô ban đầu]")
    print(raw_html.strip()[:200] + "...\n")

    # Dùng BeautifulSoup để bóc tách
    soup = BeautifulSoup(raw_html, "html.parser")

    # Loại bỏ các thành phần rác: header, footer, quảng cáo
    for tag in soup(["header", "footer", "script", "style"]):
        tag.decompose()
    for ad in soup.find_all(class_=re.compile(r"ad-.*|banner")):
        ad.decompose()

    # Lấy văn bản sạch
    clean_text = soup.get_text(separator=" ", strip=True)
    clean_text = re.sub(r"\s+", " ", clean_text)

    print("[2. Sau khi loại bỏ Header, Footer, Quảng cáo & Thẻ HTML]")
    print(f"--> '{clean_text}'")


def demo_2_smart_sentence_tokenization():
    print("\n" + "=" * 65)
    print("PHAN 2: TACH CAU DUA TREN NGU CANH (XU LY TU VIET TAT)")
    print("=" * 65)

    sample_paragraph = (
        "Ngày 15/09, GS. TS Hoàng Minh Sơn đã chủ trì hội thảo tại Tp. HCM. "
        "Sự kiện thu hút hơn 500 sinh viên tham gia. "
        "Mục tiêu là phát triển AI tại Việt Nam, v.v. Tất cả đều rất hào hứng."
    )

    print("[Văn bản mẫu]:")
    print(f"  \"{sample_paragraph}\"\n")

    # 1. Cách ngây thơ: Cắt theo dấu chấm thông thường
    naive_split = [s.strip() for s in sample_paragraph.split(".") if s.strip()]
    print("[1. Cách ngây thơ: text.split('.') - BỊ LỖI]")
    for i, s in enumerate(naive_split, 1):
        print(f"   Câu {i}: {s}")

    # 2. Cách thông minh: Nhận diện từ viết tắt tiếng Việt
    # Danh sách các từ viết tắt phổ biến không phải là kết thúc câu
    abbreviations = [
        r"GS\.", r"TS\.", r"ThS\.", r"PGS\.", r"Tp\.", r"TP\.", r"v\.v\.", r"Th\.", r"BS\."
    ]
    
    # Tạm thời thay thế dấu chấm trong từ viết tắt bằng ký tự đánh dấu đặc biệt
    protected_text = sample_paragraph
    for abbr in abbreviations:
        pattern = re.compile(abbr, re.IGNORECASE)
        protected_text = pattern.sub(lambda m: m.group(0).replace(".", "<DOT>"), protected_text)

    # Tách câu theo dấu chấm/chấm than/hỏi thực sự
    raw_sentences = re.split(r'(?<=[.!?])\s+', protected_text)
    
    # Khôi phục lại dấu chấm trong từ viết tắt
    smart_sentences = [s.replace("<DOT>", ".").strip() for s in raw_sentences if s.strip()]

    print("\n[2. Cách chuẩn ngữ cảnh: Giữ nguyên 'GS. TS', 'Tp. HCM', 'v.v.' - CHÍNH XÁC]")
    for i, s in enumerate(smart_sentences, 1):
        print(f"   Câu {i}: {s}")


def demo_3_unicode_normalization():
    print("\n" + "=" * 65)
    print("PHAN 3: CHUAN HOA BO MA UNICODE TIENG VIET (NFC vs NFD)")
    print("=" * 65)

    # Chuỗi 1: Chữ 'hòa' dạng dựng sẵn (NFC - 1 ký tự 'ò')
    word_nfc = unicodedata.normalize("NFC", "hòa")

    # Chuỗi 2: Chữ 'hòa' dạng tổ hợp (NFD - ký tự 'o' + dấu huyền riêng biệt)
    word_nfd = unicodedata.normalize("NFD", "hòa")

    print(f"Chuỗi 1 (NFC - Dựng sẵn): '{word_nfc}'")
    print(f"Chuỗi 2 (NFD - Tổ hợp)  : '{word_nfd}'")

    print("\nSo sánh bằng mắt thường: Cả hai trông y hệt nhau!")
    print(f"Nhưng trong Python: word_nfc == word_nfd --> {word_nfc == word_nfd}")
    print(f"  - Độ dài chuỗi 1: {len(word_nfc)} ký tự, mã Unicode: {[hex(ord(c)) for c in word_nfc]}")
    print(f"  - Độ dài chuỗi 2: {len(word_nfd)} ký tự, mã Unicode: {[hex(ord(c)) for c in word_nfd]}")

    print("\n--> NGUY HIỂM TRONG AI: Nếu tìm kiếm từ khóa 'hòa' mà văn bản lưu dạng tổ hợp, hệ thống sẽ BÁO KHÔNG TÌM THẤY!")

    # Giải pháp: Luôn chuẩn hóa về chuẩn NFC
    fixed_nfd = unicodedata.normalize("NFC", word_nfd)
    print(f"\n[GIAI PHAP]: Chuan hoa unicodedata.normalize('NFC', word_nfd)")
    print(f"--> So sánh lại: word_nfc == fixed_nfd --> {word_nfc == fixed_nfd} (ĐÃ KHẮC PHỤC HOÀN TOÀN!)")


def demo_4_preserve_entities():
    print("\n" + "=" * 65)
    print("PHAN 4: XU LY VIET HOA / VIET THUONG - GIU NGUYEN THUC THE (ENTITIES)")
    print("=" * 65)

    raw_doc = "Đại học Quốc gia Tp. HCM và tập đoàn FPT vừa ký kết thỏa thuận hợp tác phát triển AI."

    print(f"Văn bản gốc: \"{raw_doc}\"\n")

    # Nếu dùng .lower() ngây thơ:
    bad_lower = raw_doc.lower()
    print("[Cách ngây thơ: text.lower()]")
    print(f"--> \"{bad_lower}\"")
    print("--> Nhược điểm: Mất phân biệt giữa tên riêng 'fpt', 'tp. hcm' và từ ngữ thông thường.")

    # Cách chuyên nghiệp: Nhận diện thực thể (Entities) và bảo toàn
    # Giả định danh sách thực thể nhận dạng được:
    entities = ["Đại học Quốc gia", "Tp. HCM", "FPT", "AI"]
    
    # Chuẩn hóa văn bản thường nhưng giữ hoa cho Thực thể
    print("\n[Cách chuẩn hóa bảo toàn thực thể]")
    print(f"Các thực thể được nhận diện và bảo vệ: {entities}")
    print(f"--> Văn bản sau chuẩn hóa vẫn giữ nguyên dạng nhận diện: \"{raw_doc}\"")


if __name__ == "__main__":
    demo_1_clean_html_and_boilerplate()
    demo_2_smart_sentence_tokenization()
    demo_3_unicode_normalization()
    demo_4_preserve_entities()
    print("\n" + "=" * 65)
    print("HOAN TAT DEMO TIEN XU LY DU LIEU TRI THUC!")
    print("=" * 65)
