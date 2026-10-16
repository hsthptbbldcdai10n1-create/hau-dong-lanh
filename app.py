import streamlit as st
import pandas as pd

st.set_page_config(page_title="Oyster HUB - Frozen Oyster Plant", page_icon="🦪", layout="wide")

from pathlib import Path

BASE = Path(__file__).parent
IMG = BASE / "images"

NAVY, BLUE, GOLD = "#0B3C5D", "#1E88C9", "#F5B82E"

# >>> EDIT YOUR CONTACT INFO HERE <<<
CONTACT = {
    "Company": "OYSTER HUB VIET NAM COMPANY LIMITED",
    "Address": "Gia Thuan 1 Industrial Cluster, Gia Thuan Commune, Dong Thap Province, Vietnam",
    "Email": "oystergiathuan1@gmail.com",
    "Phone": "0913 969 541",
}

st.markdown(
    f"""
<style>
.block-container {{padding-top: 1.5rem; max-width: 1200px;}}
h1, h2, h3 {{color: {NAVY};}}
div[data-testid="stMetric"] {{background: #EAF4FB; padding: 14px 16px; border-radius: 12px; border-left: 5px solid {GOLD};}}
section[data-testid="stSidebar"] {{border-right: 3px solid {GOLD};}}
.hero {{background: linear-gradient(135deg, {NAVY} 0%, {BLUE} 100%); border-radius: 18px; padding: 36px 40px 10px 40px;
        display: flex; align-items: center; justify-content: space-between; gap: 24px; overflow: hidden; margin-bottom: 18px;}}
.hero h1 {{color: #fff; font-size: 2.3rem; margin: 0 0 8px 0; line-height: 1.15;}}
.hero p {{color: #D6ECFA; font-size: 1.05rem; margin: 0 0 18px 0;}}
.hero .tag {{display: inline-block; background: {GOLD}; color: {NAVY}; font-weight: 700; padding: 6px 14px; border-radius: 999px; margin-right: 8px; font-size: .85rem;}}
.card {{background: #fff; border: 1px solid #D5E6F2; border-top: 5px solid {GOLD}; border-radius: 14px; padding: 18px 18px 8px 18px; height: 100%;}}
.card .ic {{font-size: 2rem;}}
.card h4 {{color: {NAVY}; margin: 6px 0;}}
.card p {{color: #335; font-size: .92rem;}}
</style>
""",
    unsafe_allow_html=True,
)

OYSTER_SVG = f"""
<svg viewBox="0 0 220 180" width="230" xmlns="http://www.w3.org/2000/svg">
<defs>
<linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE08A"/><stop offset="1" stop-color="{GOLD}"/></linearGradient>
<linearGradient id="g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#BFE3F7"/></linearGradient>
</defs>
<ellipse cx="110" cy="160" rx="85" ry="9" fill="#000" opacity=".18"/>
<path d="M20 100 Q15 150 110 158 Q205 150 200 100 Q110 120 20 100Z" fill="url(#g1)"/>
<path d="M30 104 Q110 124 190 104 Q185 140 110 148 Q35 140 30 104Z" fill="url(#g2)"/>
<path d="M18 98 Q10 30 110 18 Q210 30 202 98 Q110 76 18 98Z" fill="url(#g1)" stroke="#E0A010" stroke-width="2"/>
<path d="M60 90 Q64 50 110 36 M110 80 L110 30 M160 90 Q156 50 110 36" stroke="#E0A010" stroke-width="3" fill="none" opacity=".6"/>
<circle cx="110" cy="122" r="13" fill="#fff"/><circle cx="106" cy="118" r="4" fill="#fff" stroke="#CFE6F5"/>
<text x="168" y="56" font-size="22" fill="#fff" opacity=".9">❄</text><text x="30" y="46" font-size="16" fill="#fff" opacity=".8">❄</text>
</svg>
"""

WAVE_SVG = f"""
<svg viewBox="0 0 1200 60" preserveAspectRatio="none" width="100%" height="40" xmlns="http://www.w3.org/2000/svg">
<path d="M0 30 Q150 0 300 30 T600 30 T900 30 T1200 30 V60 H0Z" fill="{GOLD}" opacity=".9"/>
</svg>
"""


def hero(title, subtitle, tags):
    import base64
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    bg = f"linear-gradient(135deg, {NAVY} 0%, {BLUE} 100%)"
    p = find_img("hero")
    if p:
        mime = "png" if p.suffix.lower() == ".png" else ("webp" if p.suffix.lower() == ".webp" else "jpeg")
        b64 = base64.b64encode(p.read_bytes()).decode()
        bg = f"linear-gradient(135deg, rgba(11,60,93,.88), rgba(30,136,201,.55)), url(data:image/{mime};base64,{b64}) center/cover"
    st.markdown(
        f'<div class="hero" style="background:{bg}"><div><h1>{title}</h1><p>{subtitle}</p>{tag_html}</div><div>{OYSTER_SVG}</div></div>',
        unsafe_allow_html=True,
    )


def page_banner(title, subtitle):
    st.markdown(
        f'<div style="background:linear-gradient(90deg,{NAVY},{BLUE});border-radius:14px;padding:18px 26px;margin-bottom:6px">'
        f'<h2 style="color:#fff;margin:0">{title}</h2><p style="color:#D6ECFA;margin:4px 0 0 0">{subtitle}</p></div>'
        f'<div style="margin:0 0 14px 0">{WAVE_SVG}</div>',
        unsafe_allow_html=True,
    )


def find_img(name):
    """Find images/<name>.(jpg|jpeg|png|webp); name may include an extension."""
    stem = Path(name).stem
    for ext in ("jpg", "jpeg", "png", "webp", "JPG", "JPEG", "PNG"):
        p = IMG / f"{stem}.{ext}"
        if p.exists():
            return p
    return None


def photo(name, caption=""):
    """Show images/<name> if it exists. Returns True when shown."""
    p = find_img(name)
    if p:
        st.image(str(p), caption=caption, width="stretch")
        return True
    return False


# ------------------------------------------------------------------
# DATA (extracted from IPA_excel.xlsx and IPA_word.docx; VND billion)
# ------------------------------------------------------------------
YEARS = [2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034]

fin = pd.DataFrame(
    {
        "Net revenue": [43.76, 54.72, 83.18, 94.27, 135.66, 165.16, 182.36, 189.70],
        "COGS": [31.96, 37.75, 52.15, 57.19, 78.03, 91.53, 100.11, 103.36],
        "Gross profit": [11.80, 16.97, 31.02, 37.08, 57.63, 73.62, 82.25, 86.35],
        "EBITDA": [8.68, 12.81, 24.73, 29.54, 47.23, 60.43, 67.36, 70.70],
        "Net income": [7.27, 11.47, 20.86, 25.31, 40.32, 52.50, 53.49, 56.39],
    },
    index=YEARS,
)

rev_market = pd.DataFrame(
    {
        "Domestic": [11.63, 13.97, 19.28, 14.12, 19.09, 22.47, 24.59, 25.32],
        "Japan": [7.71, 12.47, 18.60, 24.05, 36.56, 40.09, 44.33, 46.18],
        "Taiwan": [12.85, 15.59, 16.74, 21.65, 27.42, 30.07, 33.25, 34.64],
        "Malaysia": [5.57, 5.41, 6.45, 8.34, 7.92, 8.69, 9.60, 10.01],
        "Hong Kong": [6.00, 7.28, 8.68, 11.22, 14.22, 15.59, 17.24, 17.96],
        "United States": [0, 0, 13.43, 14.89, 30.46, 48.26, 53.36, 55.59],
    },
    index=YEARS,
)

capacity = pd.DataFrame(
    {
        "Design capacity (kg/yr)": [800000, 800000, 1000000, 1000000, 1500000, 1500000, 1500000, 1500000],
        "Utilization": [0.60, 0.70, 0.75, 0.80, 0.70, 0.80, 0.85, 0.85],
        "Finished output (kg)": [480000, 560000, 750000, 800000, 1050000, 1200000, 1275000, 1275000],
    },
    index=YEARS,
)

cash_years = ["2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034"]
ncf_tipv = [-11.42, 2.04, 6.42, 18.66, 15.43, 37.46, 51.30, 53.91, 58.09]
cum_ncf = [-11.42, -9.38, -2.96, 15.70, 31.13, 68.59, 119.89, 173.79, 231.88]

staff = pd.DataFrame(
    {
        "Production workers": [18.7, 21.8, 29.3, 31.2, 41.0, 46.8, 49.7, 49.7],
        "QC / Warehouse": [4.0, 4.7, 6.3, 6.7, 8.8, 10.0, 10.6, 10.6],
        "Admin / Management": [3.0, 3.5, 4.7, 5.0, 6.6, 7.5, 8.0, 8.0],
        "Sales": [4.0, 4.7, 6.3, 6.7, 8.8, 10.0, 10.6, 10.6],
    },
    index=YEARS,
)

SHIFTS = [-20, -10, 0, 10, 20]
sens_epv = {
    "Selling price": [41.46, 80.19, 118.98, 157.76, 196.54],
    "Exchange rate (VND/USD)": [56.74, 87.86, 118.98, 150.10, 181.21],
    "Production capacity": [87.14, 103.06, 118.98, 134.89, 150.81],
    "Raw material price": [154.23, 136.60, 118.98, 101.35, 83.72],
    "Total investment": [122.47, 120.72, 118.98, 117.23, 115.48],
}
sens_tipv = {
    "Selling price": [52.75, 98.14, 143.53, 188.92, 234.31],
    "Exchange rate (VND/USD)": [70.29, 106.91, 143.53, 180.16, 216.78],
    "Production capacity": [105.69, 124.61, 143.53, 162.46, 181.38],
    "Raw material price": [184.37, 163.95, 143.53, 123.12, 102.70],
    "Total investment": [147.10, 145.32, 143.53, 141.75, 139.96],
}


# ------------------------------------------------------------------
# PUBLIC PAGES (Vietnamese)
# ------------------------------------------------------------------
def page_home():
    hero(
        "HÀU ĐÔNG LẠNH OYSTER HUB",
        "TƯƠI NGON TỪ BIỂN - AN TOÀN TRÊN BÀN ĂN",
        ["❄ Cấp đông IQF", "🦪 Hàu nửa vỏ", "🌏 Xuất khẩu"],
    )

    st.markdown("## Vì sao chọn chúng tôi")
    st.write(
        "Chúng tôi chế biến hàu nuôi của Việt Nam thành sản phẩm hàu nửa vỏ đông lạnh IQF: giữ trọn vị tươi, "
        "bảo quản ổn định đến 30 ngày và đóng gói hút chân không tiện lợi cho siêu thị, nhà hàng, khách sạn "
        "và xuất khẩu. Nguyên liệu có truy xuất nguồn gốc, quy trình kiểm soát theo HACCP, "
        "chuỗi lạnh liên tục từ nhà máy đến tay khách hàng."
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Nhà máy", "1.500 m²")
    c2.metric("Công suất mỗi năm", "800–1.500 tấn")
    c3.metric("Bảo quản", "≤ -18 °C")
    c4.metric("Phục vụ", "6 thị trường")

    st.markdown("## Sản phẩm nổi bật")
    if find_img("product"):
        a, b = st.columns([2, 3])
        with a:
            photo("product.jpg", "Hàu nửa vỏ đông lạnh IQF")
        with b:
            st.markdown("### Hàu nửa vỏ đông lạnh IQF")
            st.write("Cấp đông nhanh từng con, phủ một lớp băng mỏng bảo vệ thịt hàu, đóng khay hút chân không 1–1,5 kg.")
    f1, f2, f3 = st.columns(3)
    f1.markdown('<div class="card"><div class="ic">🦪</div><h4>Hàu nửa vỏ cao cấp</h4><p>Phân loại kích cỡ đồng đều, thịt dày, xử lý ozone trước cấp đông, đóng khay hút chân không.</p></div>', unsafe_allow_html=True)
    f2.markdown('<div class="card"><div class="ic">❄️</div><h4>Chuỗi lạnh liên tục</h4><p>Hầm cấp đông IQF, kho lạnh và xe lạnh giữ sản phẩm từ -18 °C trở xuống đến tay khách.</p></div>', unsafe_allow_html=True)
    f3.markdown('<div class="card"><div class="ic">📱</div><h4>Truy xuất nguồn gốc</h4><p>Quét mã QR trên bao bì để xem vùng nuôi, ngày thu hoạch, mã nhà máy và kết quả kiểm nghiệm.</p></div>', unsafe_allow_html=True)
    st.write("")
    st.info("Cần báo giá hoặc mẫu thử? Vào mục **Liên hệ** để gửi yêu cầu cho chúng tôi.")


def page_about():
    page_banner("Giới thiệu", "Công ty TNHH OYSTER HUB VIỆT NAM")

    a, b = st.columns([3, 2])
    with a:
        st.markdown("### Chúng tôi là ai")
        st.write(
            "Hiện nay hàu ở Việt Nam chủ yếu bán tươi, nên khó bảo quản lâu, khó vận chuyển xa và khó mở rộng thị trường. "
            "OYSTER HUB xây dựng nhà máy chế biến và đóng gói hàu đông lạnh để nâng giá trị cho hàu nuôi trong nước, "
            "cung cấp sản phẩm hàu nửa vỏ đông lạnh an toàn, chất lượng cho thị trường trong nước và xuất khẩu "
            "(Nhật Bản, Đài Loan, Malaysia, Hồng Kông, Hoa Kỳ)."
        )
    with b:
        if not photo("factory.jpg", "Nhà máy chế biến hàu đông lạnh"):
            st.markdown('<div class="card"><div class="ic">🏭</div><h4>Nhà máy 1.500 m²</h4><p>Dây chuyền bán tự động, chia khu một chiều từ khu bẩn sang khu sạch, mở rộng theo 3 giai đoạn.</p></div>', unsafe_allow_html=True)

    st.markdown("### Mục tiêu của chúng tôi")
    k1, k2, k3 = st.columns(3)
    k1.markdown('<div class="card"><div class="ic">📈</div><h4>Kinh tế</h4><p>Mở rộng 3 giai đoạn: 800 → 1.000 → 1.500 tấn/năm, tận dụng máy móc để giảm giá thành.</p></div>', unsafe_allow_html=True)
    k2.markdown('<div class="card"><div class="ic">🤝</div><h4>Xã hội</h4><p>Tạo việc làm tại địa phương (khoảng 30 đến 79 lao động) và đầu ra ổn định cho hộ nuôi hàu.</p></div>', unsafe_allow_html=True)
    k3.markdown('<div class="card"><div class="ic">🌱</div><h4>Môi trường</h4><p>Xử lý nước thải, tái chế vỏ hàu, dùng điện mặt trời và môi chất lạnh NH3.</p></div>', unsafe_allow_html=True)

    st.markdown("### Quy trình sản xuất")
    steps = ["1. Tiếp nhận & kiểm tra", "2. Rửa & làm mát sơ bộ", "3. Tách vỏ & phân loại", "4. Xử lý ozone & xếp khay",
             "5. Cấp đông IQF & mạ băng", "6. Đóng gói hút chân không", "7. Bảo quản kho lạnh (≤ -18 °C)", "8. Phân phối chuỗi lạnh"]
    cols = st.columns(4)
    for i, s_ in enumerate(steps):
        cols[i % 4].info(s_)

    st.markdown("### Chất lượng & an toàn thực phẩm")
    st.markdown(
        """
        - Chương trình **HACCP**, điều kiện cơ sở theo **QCVN 02-01 / 02-02**
        - Tham chiếu tiêu chuẩn **Codex STAN 292-2008** về E. coli trong hàu
        - Sản phẩm bảo quản **-18 °C trở xuống**; hàu nguyên liệu xử lý ngay hoặc giữ tối đa 5 ngày
        - Truy xuất nguồn gốc theo lô, mã QR trên bao bì
        """
    )

    st.markdown("### Vị trí nhà máy")
    st.write(
        "Cụm công nghiệp Gia Thuận 1, xã Gia Thuận, tỉnh Đồng Tháp (khu vực Gò Công), cách TP.HCM khoảng 40 km, "
        "cách cảng Hiệp Phước khoảng 30 km và gần vùng nuôi hàu Cần Giờ bên kia sông Soài Rạp. "
        "Cụm có sẵn điện, nước và hệ thống xử lý nước thải tập trung."
    )

    st.markdown("### Phát triển bền vững")
    s1, s2, s3 = st.columns(3)
    s1.metric("Tái chế vỏ hàu", "100%")
    s2.metric("Điện mặt trời", "500 kWp")
    s3.metric("Tiêu chuẩn nuôi", "ASC / VietGAP")


def page_product():
    page_banner("Sản phẩm", "Hàu nửa vỏ đông lạnh IQF")

    a, b = st.columns([2, 3])
    with a:
        if not photo("product.jpg", "Hàu nửa vỏ đông lạnh IQF"):
            st.markdown(f'<div style="background:linear-gradient(135deg,{NAVY},{BLUE});border-radius:16px;padding:20px;text-align:center">{OYSTER_SVG}</div>', unsafe_allow_html=True)
    with b:
        st.markdown("### Hàu nửa vỏ đông lạnh IQF")
        st.write(
            "Hàu giữ lại một nửa vỏ, được cấp đông nhanh từng con (IQF), phủ lớp băng mỏng bảo vệ thịt hàu khỏi cháy lạnh "
            "và giữ màu tự nhiên. Đóng khay hút chân không, in ngày/lô, sẵn sàng cho bếp nhà hàng, siêu thị và xuất khẩu."
        )
        st.markdown(
            """
            - ✅ Tiết kiệm công tách vỏ và giảm rác bếp
            - ✅ Bảo quản ổn định đến 30 ngày
            - ✅ Xử lý ozone giảm vi sinh trước cấp đông
            - ✅ Có mã QR truy xuất nguồn gốc
            """
        )
        st.metric("Giá tham khảo thị trường Việt Nam", "từ 85.000 VNĐ/kg")

    gallery = [find_img(f"product{i}") for i in range(2, 8)]
    gallery = [g for g in gallery if g]
    if gallery:
        st.markdown("### Hình ảnh sản phẩm")
        gcols = st.columns(min(3, len(gallery)))
        for i, g in enumerate(gallery):
            with gcols[i % len(gcols)]:
                st.image(str(g), width="stretch")

    st.markdown("### Thông số sản phẩm")
    spec = pd.DataFrame(
        {
            "Tiêu chí": ["Dạng sản phẩm", "Khối lượng mỗi khay", "Nhiệt độ bảo quản", "Bao bì", "Phân loại", "Tỷ lệ thu hồi so với hàu nguyên liệu"],
            "Thông số": ["Hàu nửa vỏ, cấp đông IQF, mạ băng", "1 – 1,5 kg", "-18 °C hoặc thấp hơn", "Khay hút chân không, in ngày/lô, đóng thùng carton", "Phân cỡ trên băng tải", "70%"],
        }
    )
    st.dataframe(spec, hide_index=True, width="stretch")

    st.markdown("### Giá dự kiến theo thị trường (năm 2027)")
    price = pd.DataFrame(
        {
            "Thị trường": ["Việt Nam", "Nhật Bản", "Đài Loan", "Malaysia", "Hồng Kông", "Hoa Kỳ (từ 2029)"],
            "Giá": ["85.000 VNĐ/kg", "6,00 USD/kg", "3,00 USD/kg", "2,60 USD/kg", "7,00 USD/kg", "6,83 USD/kg"],
        }
    )
    st.dataframe(price, hide_index=True, width="stretch")
    st.caption("Giá lấy từ mô hình tài chính của dự án. Giá thực tế thỏa thuận theo số lượng và đơn hàng.")

    st.markdown("### Kênh phân phối")
    c = st.columns(5)
    items = [("🛒", "Siêu thị", "Aeon, WinMart, Co.op Mart"), ("🍽️", "Nhà hàng & khách sạn", "Buffet hải sản, khách sạn, tiệc cưới"),
             ("📦", "Thương mại điện tử", "Cửa hàng tươi sống online, ứng dụng giao nhanh"), ("🚚", "Nhà phân phối", "Đại lý hải sản đông lạnh các tỉnh"),
             ("🚢", "Xuất khẩu", "Container lạnh đến Nhật, Đài Loan, Malaysia, Hồng Kông, Mỹ")]
    for col, (ic, t, d) in zip(c, items):
        col.markdown(f'<div class="card"><div class="ic">{ic}</div><h4>{t}</h4><p>{d}</p></div>', unsafe_allow_html=True)


def page_contact():
    page_banner("Liên hệ", "Gửi yêu cầu báo giá, mẫu thử hoặc hợp tác")

    left, right = st.columns([3, 2])
    with left:
        st.markdown("### Vị trí")
        # Vị trí ước chừng; chỉnh lat/lon theo đúng lô đất nếu cần.
        st.map(pd.DataFrame({"lat": [10.30], "lon": [106.76]}), zoom=9, color=GOLD, size=400)
        st.caption("Ghim bản đồ chỉ là vị trí ước chừng.")
    with right:
        st.markdown("### Thông tin liên hệ")
        st.markdown(f"🏭 **{CONTACT['Company']}**")
        st.markdown(f"📍 {CONTACT['Address']}")
        st.markdown(f"☎️ {CONTACT['Phone']}")
        st.markdown(f"📧 {CONTACT['Email']}")

    st.markdown("### Gửi tin nhắn")
    with st.form("contact"):
        name = st.text_input("Họ tên")
        email = st.text_input("Email hoặc số điện thoại")
        msg = st.text_area("Nội dung")
        if st.form_submit_button("Gửi"):
            st.success(f"Cảm ơn{' ' + name if name else ''}! Chúng tôi sẽ liên hệ lại sớm.")


# ------------------------------------------------------------------
# INVESTOR SECTION (English, from the feasibility report)
# ------------------------------------------------------------------
def inv_market():
    st.write(
        "Exports drive growth (70–80% of sales volume); the domestic market provides a stable base (20–30%). "
        "Both the domestic and global addressable markets are assumed to grow 4% per year."
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("Global SAM 2026", "27.1 M kg", "→ 37.1 M kg in 2034")
    c2.metric("Vietnam SAM 2026", "3.0 M kg", "→ 4.1 M kg in 2034")
    c3.metric("Largest export market", "Taiwan", "45–50% of export volume")

    st.markdown("### Revenue by market (VND billion)")
    st.bar_chart(rev_market, color=["#F5B82E", "#0B3C5D", "#1E88C9", "#6EC1EA", "#FFD97A", "#9AA9B5"])

    st.markdown("### Selling prices")
    prices = pd.DataFrame(
        {
            "Market": ["Vietnam (VND/kg)", "Japan (USD/kg)", "Taiwan (USD/kg)", "Malaysia (USD/kg)", "Hong Kong (USD/kg)", "United States (USD/kg)"],
            "Price 2027": ["85,000", "6.00", "3.00", "2.60", "7.00", "6.50 (from 2029)"],
            "Price 2034": ["104,539", "7.13", "3.57", "3.09", "8.32", "7.73"],
            "Annual growth": ["3.0%", "2.5%", "2.5%", "2.5%", "2.5%", "2.5%"],
        }
    )
    st.dataframe(prices, hide_index=True, width="stretch")

    st.markdown("### Production plan")
    cap_view = capacity.copy()
    cap_view["Utilization"] = (cap_view["Utilization"] * 100).round(0).astype(int).astype(str) + "%"
    st.dataframe(cap_view.style.format({"Design capacity (kg/yr)": "{:,.0f}", "Finished output (kg)": "{:,.0f}"}), width="stretch")
    st.caption("Utilization dips in 2031 because design capacity jumps from 1.0 to 1.5 million kg/year; actual output still rises.")

    with st.expander("Porter's Five Forces summary"):
        st.markdown(
            """
            - **New entrants: medium to high.** Large capital and strict microbiological standards act as barriers.
            - **Supplier power: medium, rising.** Supply depends on weather and farm stability; raw material price grows 3.5%/year.
            - **Buyer power:** low to medium domestically; strong in export markets (strict standards, 30-day payment terms).
            - **Substitutes: medium.** Fresh oysters, clams and mussels; IQF half-shell offers safety, convenience and 30-day storage.
            - **Rivalry: very strong.** Competition for raw materials and export customers.
            """
        )


def inv_tech():
    st.write(
        "The plant follows a one-way flow from the dirty area to the clean area to avoid cross-contamination. "
        "IQF freezing and cold storage together account for roughly half of equipment spending, so the cold chain determines both quality and cost."
    )

    st.markdown("### Production process")
    steps = [
        "1. Receiving & inspection",
        "2. Washing & pre-cooling",
        "3. Shucking & sorting",
        "4. Ozone treatment & tray loading",
        "5. IQF freezing & glazing",
        "6. Vacuum packaging",
        "7. Cold storage (≤ -18 °C)",
        "8. Cold-chain distribution",
    ]
    cols = st.columns(4)
    for i, s in enumerate(steps):
        cols[i % 4].info(s)

    st.markdown("### Investment by phase (VND billion)")
    capex = pd.DataFrame(
        {
            "Leasehold improvements": [2.0, 0, 0],
            "Machinery & equipment": [6.59, 4.31, 9.02],
            "Office equipment": [0.5, 0, 0.2],
            "Contingency (10%)": [0.909, 0.431, 0.922],
        },
        index=["Phase 1", "Phase 2", "Phase 3"],
    )
    st.bar_chart(capex, color=["#0B3C5D", "#1E88C9", "#6EC1EA", "#F5B82E"])
    capex_t = capex.copy()
    capex_t["Total"] = capex_t.sum(axis=1)
    st.dataframe(capex_t.style.format("{:.3f}"), width="stretch")
    st.caption("Total CAPEX: VND 24.882 bn. Machinery depreciated over 10 years; renovation, office equipment and contingency over 8 years.")

    st.markdown("### Machinery by functional group (VND million)")
    equip = pd.DataFrame(
        {
            "Equipment group": [
                "Receiving and inspection", "Washing and preliminary cooling", "Shucking and sorting",
                "Ozone, draining, tray loading", "IQF freezing", "Glazing", "Vacuum packing",
                "Carton sealing and palletizing", "Cold storage", "Electricity, utilities, wastewater, installation, other",
            ],
            "Phase 1": [205, 900, 780, 560, 1980, 260, 480, 225, 1200, 0],
            "Phase 2": [0, 325, 275, 100, 1280, 140, 325, 0, 850, 1015],
            "Phase 3": [0, 500, 510, 210, 2650, 300, 550, 0, 2000, 2300],
        }
    )
    st.dataframe(equip, hide_index=True, width="stretch")

    st.markdown("### Quality & food safety")
    st.markdown(
        """
        - HACCP program under QCVN 02-02 and facility conditions under QCVN 02-01
        - E. coli three-class plan (Codex STAN 292-2008): n = 5, c = 1, m = 230, M = 700 MPN/100 g
        - Finished product stored at -18 °C or lower; raw oysters processed immediately or held at most 5 days
        - Wastewater meets the cluster connection requirements and QCVN 40:2025/BTNMT
        """
    )


def inv_fin():
    st.caption("Base-case results from the financial model. WACC about 9.6%–10.4%.")

    view = st.radio("Perspective", ["TIPV (total investment)", "EPV (equity)"], horizontal=True)
    if view.startswith("TIPV"):
        m = [("NPV", "VND 143.53 bn"), ("IRR", "85.47%"), ("MIRR", "47.90%"), ("Payback (PP)", "2.16 yrs"), ("Discounted payback", "2.31 yrs"), ("Profitability index", "13.57x")]
    else:
        m = [("NPV", "VND 118.98 bn"), ("IRR", "111.85%"), ("MIRR", "48.73%"), ("Payback (PP)", "1.71 yrs"), ("Discounted payback", "1.94 yrs"), ("Profitability index", "18.21x")]
    cols = st.columns(6)
    for c, (k, v) in zip(cols, m):
        c.metric(k, v)

    st.markdown("### Revenue and profit (VND billion)")
    st.bar_chart(fin[["Net revenue", "Gross profit", "EBITDA", "Net income"]], stack=False, color=["#0B3C5D", "#1E88C9", "#6EC1EA", "#F5B82E"])

    st.markdown("### Cumulative net cash flow, TIPV (VND billion)")
    cf = pd.DataFrame({"Net cash flow": ncf_tipv, "Cumulative": cum_ncf}, index=cash_years)
    st.line_chart(cf, color=["#1E88C9", "#F5B82E"])
    st.caption("2026 is the investment year. Cumulative cash flow turns positive in 2029.")

    st.markdown("### Income statement summary (VND billion)")
    st.dataframe(fin.T.style.format("{:.2f}"), width="stretch")

    st.markdown("### Funding structure")
    c1, c2 = st.columns(2)
    c1.markdown(
        """
        - Total CAPEX: **VND 24.882 bn** (9.999 + 4.741 + 10.142)
        - Initial working capital: **VND 1.416 bn**
        - Loans: VND 4.5 bn (2026), 2.5 bn (2028), 5.0 bn (2030)
        """
    )
    c2.markdown(
        """
        - Corporate income tax: 0% in 2027–2028, 8.5% in 2029–2032, 17% from 2033
        - Total CIT 2027–2034: about VND 35.4 bn
        - Fixed asset liquidation value: VND 4.56 bn
        """
    )


def inv_risk():
    st.write("The model shows strong base-case returns, but results are sensitive to selling price, exchange rate and raw material cost.")

    st.markdown("### Sensitivity of NPV")
    persp = st.radio("NPV perspective", ["EPV (equity)", "TIPV (total investment)"], horizontal=True)
    data = sens_epv if persp.startswith("EPV") else sens_tipv
    chosen = st.multiselect("Variables", list(data.keys()), default=["Selling price", "Raw material price", "Production capacity"])
    if chosen:
        sdf = pd.DataFrame({k: data[k] for k in chosen}, index=SHIFTS)
        sdf.index.name = "Change in variable (%)"
        st.line_chart(sdf)
        st.caption("NPV in VND billion. Selling price is the most sensitive variable; total investment is the least.")
    else:
        st.info("Select at least one variable.")

    st.markdown("### Scenario analysis (EPV)")
    scen = pd.DataFrame(
        {
            "Scenario": ["Worst case", "Base case", "Optimistic"],
            "Probability": ["25%", "50%", "25%"],
            "NPV (VND bn)": [-13.59, 118.98, 380.22],
            "IRR": ["-4.06%", "111.85%", "489.84%"],
            "Payback": ["Not recovered", "1.71 yrs", "0.24 yrs"],
            "Avg DSCR": [-1.89, 14.18, 48.64],
        }
    )
    st.dataframe(scen, hide_index=True, width="stretch")
    c1, c2, c3 = st.columns(3)
    c1.metric("Expected NPV", "VND 151.14 bn")
    c2.metric("Standard deviation", "VND 142.90 bn")
    c3.metric("Coefficient of variation", "0.945")
    st.warning("In the worst case (all adverse changes of 20% at once) the project loses value. Cash flow and debt must be managed closely.")

    st.markdown("### Key risks and mitigation")
    risks = pd.DataFrame(
        {
            "Risk": [
                "Raw material supply and price", "Selling price and market demand", "Food safety and quality",
                "Cold chain and refrigeration", "Environment and waste", "Exchange rate and interest rate",
            ],
            "Mitigation": [
                "Long-term offtake contracts with cooperatives and farms; support ASC/VietGAP farming",
                "Diversify across Japan, Taiwan, Malaysia, Hong Kong, US and domestic channels; build brand",
                "HACCP, batch traceability, ozone pre-treatment, strict microbiological testing",
                "Preventive maintenance, backup generator, refrigerant leak monitoring",
                "Wastewater treatment meeting QCVN 40:2025/BTNMT; recycle oyster shells",
                "Hedging for large export contracts; close cash-flow and debt monitoring",
            ],
        }
    )
    st.dataframe(risks, hide_index=True, width="stretch")


def inv_people():

    st.markdown("### Workforce plan (headcount)")
    st.bar_chart(staff, color=["#0B3C5D", "#1E88C9", "#6EC1EA", "#F5B82E"])
    total = staff.sum(axis=1)
    c1, c2, c3 = st.columns(3)
    c1.metric("Staff in 2027", f"{total[2027]:.0f}")
    c2.metric("Staff in 2034", f"{total[2034]:.0f}")
    c3.metric("Avg production wage 2027", "VND 8.0 M/month", "+3%/year")
    st.caption("Headcount is derived from a labor norm of 0.08 h/kg, 7 hours/day and 293 operating days/year.")

    st.markdown("### Economic and social impact")
    c1, c2 = st.columns(2)
    c1.markdown(
        """
        **Economic**
        - Raw oyster offtake from farmers: about 10,626 tonnes over 2027–2034 (about VND 369 bn)
        - Corporate income tax contribution: about VND 35.4 bn
        - Export earnings from Japan, Taiwan, Malaysia, Hong Kong and the US
        """
    )
    c2.markdown(
        """
        **Social**
        - Direct jobs growing from about 30 to about 79
        - 100% of workers trained in food safety (HACCP, ISO 22000)
        - Cut-resistant gloves, cold-resistant uniforms and health check-ups twice a year
        """
    )

    st.markdown("### Environmental commitments")
    st.markdown(
        """
        - **Shell recycling:** oyster shells (about 30% of input) are dried and ground into agricultural lime, feed calcium and farming substrate
        - **Clean energy:** 500 kWp rooftop solar covering about 25% of daytime electricity demand
        - **Refrigerant:** NH3 (R717), with zero ozone depletion potential
        - **Wastewater:** MBR treatment before connection to the industrial cluster's system
        - **Traceability:** QR codes from farm to package; ASC and VietGAP supply chain
        """
    )

    st.markdown("### UN SDG commitments")
    sdg = pd.DataFrame(
        {
            "SDG": ["SDG 8: Decent work & growth", "SDG 12: Responsible consumption", "SDG 14: Life below water"],
            "Commitment": [
                "Create jobs, pay above general wage level, buy oysters from local fishermen",
                "Recycle 100% of oyster shell by-products; energy-saving IQF technology",
                "Treat wastewater to discharge standards; promote raft/hanging-rope farming",
            ],
        }
    )
    st.dataframe(sdg, hide_index=True, width="stretch")


def page_investor():
    page_banner("Nhà đầu tư / Investor", "Key figures from the feasibility study (base case)")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total CAPEX", "VND 24.88 bn")
    c2.metric("NPV (TIPV)", "VND 143.5 bn")
    c3.metric("IRR (TIPV)", "85.47%")
    c4.metric("Payback", "2.16 yrs")
    t = st.tabs(["Market & Revenue", "Technology & CAPEX", "Financial", "Risk", "People & ESG"])
    for tab, fn in zip(t, [inv_market, inv_tech, inv_fin, inv_risk, inv_people]):
        with tab:
            fn()


# ------------------------------------------------------------------
# NAVIGATION (top menu) + FOOTER
# ------------------------------------------------------------------
nav = st.navigation(
    [
        st.Page(page_home, title="Trang chủ", icon="🏠", url_path="home", default=True),
        st.Page(page_about, title="Giới thiệu", icon="🏭", url_path="about"),
        st.Page(page_product, title="Sản phẩm", icon="🦪", url_path="product"),
        st.Page(page_contact, title="Liên hệ", icon="📞", url_path="contact"),
        st.Page(page_investor, title="Nhà đầu tư", icon="📊", url_path="investor"),
    ],
    position="top",
)
nav.run()

st.markdown("---")
st.markdown(
    f"🏭 {CONTACT['Address']}  \\n☎️ {CONTACT['Phone']}  \\n📧 {CONTACT['Email']}"
)
st.caption("© OYSTER HUB VIỆT NAM | Số liệu lấy từ mô hình tài chính và báo cáo khả thi của dự án (kịch bản cơ sở).")
