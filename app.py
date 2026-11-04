from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import re

import streamlit as st

ROOT = Path(__file__).resolve().parent
WEEKS_DIR = ROOT / "weeks"

WEEKS = [
    (1, "Môi trường & Hello Python", "week-01-hello-python", "Chạy chương trình đầu tiên, terminal và Git."),
    (2, "Biến, kiểu dữ liệu & input/output", "week-02-variables-types", "Lưu trữ, chuyển đổi và xử lý dữ liệu đầu vào."),
    (3, "Điều kiện & Boolean", "week-03-conditionals", "Ra quyết định và kiểm tra dữ liệu đầu vào."),
    (4, "Chuỗi & Regex", "week-04-strings", "Xử lý văn bản, f-string và biểu thức chính quy."),
    (5, "List & Tuple", "week-05-lists-tuples", "Lưu trữ dữ liệu tuần tự, slicing và unpacking."),
    (6, "Vòng lặp", "week-06-loops", "for, while, enumerate, zip và comprehensions."),
    (7, "Hàm", "week-07-functions", "Phân rã vấn đề, tham số, return và scope."),
    (8, "Dict & Set", "week-08-dicts-sets", "Dữ liệu dạng key-value, tập hợp và dữ liệu lồng nhau."),
    (9, "Midterm Project", "week-09-midterm-project", "Tổng hợp kiến thức tuần 01–08 thành một ứng dụng."),
    (10, "Files I/O", "week-10-files-io", "Đọc ghi tệp, pathlib, CSV và JSON."),
    (11, "Exceptions & Debugging", "week-11-exceptions", "Đọc traceback và xử lý lỗi an toàn."),
    (12, "Testing với pytest", "week-12-testing-pytest", "Kiểm thử normal case, edge case và input không hợp lệ."),
    (13, "Modules, CLI & API", "week-13-modules-cli-api", "Tổ chức module, dòng lệnh và HTTP/API."),
    (14, "OOP Essentials", "week-14-oop-essentials", "Class, composition và inheritance cơ bản."),
    (15, "Capstone Project", "week-15-capstone-project", "Xây dựng dự án cuối khóa có test và README."),
]


def safe_read(path: Path) -> str:
    """Read a repository text file without allowing paths outside the project."""
    try:
        resolved = path.resolve()
        resolved.relative_to(ROOT)
        return resolved.read_text(encoding="utf-8")
    except (OSError, ValueError):
        return ""


def collect_python_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return sorted(
        p for p in folder.rglob("*.py")
        if p.is_file() and not any(part.startswith(".") or part == "__pycache__" for part in p.parts)
    )


def render_home() -> None:
    st.title("🐍 Python Journey")
    st.subheader("Học Python bằng cách xây dựng — không chỉ học cú pháp.")
    st.write(
        "Một không gian thực hành tương tác cho lộ trình Python 15 tuần. "
        "Chọn bài học, đọc ghi chú, xem mã nguồn và thử thay đổi dữ liệu ngay trên web."
    )
    c1, c2, c3 = st.columns(3)
    c1.metric("Lộ trình", "15 tuần")
    c2.metric("Cấp độ", "Beginner")
    c3.metric("Cách học", "Learn → Build → Test")
    st.info("Chọn **Lộ trình & tài liệu** ở thanh bên để mở nội dung từng tuần, "
            "hoặc **Phòng thực hành** để tương tác với các ví dụ Python.")
    st.markdown("### Học theo vòng lặp")
    st.markdown("**Đọc khái niệm → xem ví dụ → thay đổi dữ liệu → quan sát kết quả → tự làm bài tập.**")
    st.markdown("### Bắt đầu nhanh")
    st.code("python -m pip install -r requirements.txt\nstreamlit run app.py", language="bash")


def render_curriculum() -> None:
    st.title("📚 Lộ trình & tài liệu")
    week_labels = [f"Tuần {n:02d} · {title}" for n, title, _, _ in WEEKS]
    selected = st.selectbox("Chọn tuần học", week_labels)
    index = week_labels.index(selected)
    number, title, slug, description = WEEKS[index]
    week_dir = WEEKS_DIR / slug

    st.header(f"Tuần {number:02d}: {title}")
    st.write(description)
    st.caption(f"Thư mục: weeks/{slug}/")

    readme = safe_read(week_dir / "README.md")
    notes = safe_read(week_dir / "notes.md")
    tab_overview, tab_notes, tab_files = st.tabs(["Tổng quan", "Ghi chú bài học", "Mã nguồn & bài tập"])

    with tab_overview:
        if readme:
            st.markdown(readme)
        else:
            st.warning("Tuần này chưa có README.md.")
    with tab_notes:
        if notes:
            st.markdown(notes)
        else:
            st.info("Tuần này chưa có notes.md.")
        lesson_files = sorted(week_dir.glob("lesson-*.md")) if week_dir.exists() else []
        for lesson in lesson_files:
            with st.expander(lesson.stem.replace("-", " ").title()):
                st.markdown(safe_read(lesson))

    with tab_files:
        folders = ["examples", "exercises", "solutions", "mini-project", "checks", "tests"]
        found = []
        for folder_name in folders:
            files = collect_python_files(week_dir / folder_name)
            if files:
                found.extend(files)
                with st.expander(f"{folder_name} · {len(files)} file", expanded=folder_name == "examples"):
                    for file_path in files:
                        relative = file_path.relative_to(ROOT).as_posix()
                        st.markdown(f"**{relative}**")
                        st.code(safe_read(file_path), language="python")
        if not found:
            st.info("Chưa tìm thấy file Python trong các thư mục examples/exercises/solutions.")

    st.divider()
    st.markdown("**Mở thư mục tuần trên GitHub:**")
    st.link_button("Xem trên GitHub", f"https://github.com/MulSuLinh/python-journey/tree/upgrade/python-journey-v2/weeks/{slug}")


def render_playground() -> None:
    st.title("🧪 Phòng thực hành Python")
    st.write("Các ví dụ nhỏ chạy bằng Python thật trong ứng dụng. Thay đổi dữ liệu rồi quan sát kết quả.")
    demo = st.selectbox(
        "Chọn chủ đề thực hành",
        [
            "Biến & phép tính",
            "Điều kiện",
            "Chuỗi & tần suất từ",
            "List & thống kê",
            "Vòng lặp",
            "Dict tra cứu",
            "Hàm",
            "JSON",
        ],
    )

    if demo == "Biến & phép tính":
        st.subheader("Máy tính cơ bản")
        a, b = st.columns(2)
        left = a.number_input("Số thứ nhất", value=12.0)
        right = b.number_input("Số thứ hai", value=3.0)
        operation = st.selectbox("Phép tính", ["Cộng", "Trừ", "Nhân", "Chia"])
        if operation == "Cộng":
            result = left + right
            expression = f"{left} + {right}"
        elif operation == "Trừ":
            result = left - right
            expression = f"{left} - {right}"
        elif operation == "Nhân":
            result = left * right
            expression = f"{left} * {right}"
        else:
            result = None if right == 0 else left / right
            expression = f"{left} / {right}"
        st.code(f"result = {expression}", language="python")
        if result is None:
            st.error("Không thể chia cho 0.")
        else:
            st.metric("Kết quả", f"{result:g}")

    elif demo == "Điều kiện":
        st.subheader("Xếp loại theo điểm")
        score = st.slider("Điểm số", 0, 100, 78)
        if score >= 90:
            grade = "Xuất sắc"
        elif score >= 80:
            grade = "Giỏi"
        elif score >= 65:
            grade = "Khá"
        elif score >= 50:
            grade = "Trung bình"
        else:
            grade = "Cần cố gắng"
        st.code(
            "if score >= 90:\n    grade = 'Xuất sắc'\nelif score >= 80:\n    grade = 'Giỏi'\n"
            "elif score >= 65:\n    grade = 'Khá'\nelse:\n    grade = 'Cần cố gắng'",
            language="python",
        )
        st.success(f"Điểm {score}: {grade}")

    elif demo == "Chuỗi & tần suất từ":
        st.subheader("Word Counter")
        sentence = st.text_area("Nhập một đoạn văn", "Python rất thú vị. Học Python bằng cách thực hành!")
        words = re.findall(r"\w+", sentence.lower(), flags=re.UNICODE)
        counts = Counter(words)
        st.code("words = re.findall(r'\\w+', text.lower())\ncounts = Counter(words)", language="python")
        c1, c2 = st.columns(2)
        c1.metric("Số từ", len(words))
        c2.metric("Số từ khác nhau", len(counts))
        if counts:
            st.bar_chart(dict(counts.most_common(10)))
            st.dataframe([{"Từ": word, "Số lần": count} for word, count in counts.most_common()], use_container_width=True)

    elif demo == "List & thống kê":
        st.subheader("Phân tích danh sách số")
        raw = st.text_input("Nhập các số, cách nhau bằng dấu phẩy", "12, 8, 15, 20, 5")
        try:
            values = [float(item.strip()) for item in raw.split(",") if item.strip()]
            if not values:
                raise ValueError("Danh sách đang trống")
            st.code("numbers = [12, 8, 15, 20, 5]\nmaximum = max(numbers)\naverage = sum(numbers) / len(numbers)", language="python")
            a, b, c = st.columns(3)
            a.metric("Số phần tử", len(values))
            b.metric("Lớn nhất", f"{max(values):g}")
            c.metric("Trung bình", f"{sum(values) / len(values):.2f}")
            st.write("Danh sách đã sắp xếp:", sorted(values))
        except ValueError:
            st.error("Hãy nhập danh sách số hợp lệ, ví dụ: 1, 2, 3.")

    elif demo == "Vòng lặp":
        st.subheader("Mô phỏng vòng lặp for")
        limit = st.slider("Giới hạn", 1, 20, 5)
        numbers = list(range(1, limit + 1))
        st.code(f"for number in range(1, {limit + 1}):\n    print(number)", language="python")
        st.write("Các giá trị được tạo:", numbers)
        st.metric("Tổng các số", sum(numbers))
        st.dataframe([{"Lần lặp": i, "Giá trị": value, "Tổng tích lũy": sum(numbers[:i])} for i, value in enumerate(numbers, 1)])

    elif demo == "Dict tra cứu":
        st.subheader("Từ điển thông tin học viên")
        records = {
            "An": {"Python": 8.5, "Git": 7.0},
            "Bình": {"Python": 9.0, "Git": 8.0},
            "Chi": {"Python": 7.5, "Git": 9.5},
        }
        person = st.selectbox("Chọn học viên", list(records))
        st.code("scores = {'An': {'Python': 8.5, 'Git': 7.0}}\npython_score = scores[name]['Python']", language="python")
        st.json(records[person])
        st.metric("Điểm Python", records[person]["Python"])

    elif demo == "Hàm":
        st.subheader("Hàm tính tiền sau giảm giá")
        price = st.number_input("Giá gốc (đồng)", min_value=0, value=200000, step=10000)
        percent = st.slider("Giảm giá (%)", 0, 90, 10)
        def final_price(amount: float, discount: int) -> float:
            return amount * (1 - discount / 100)
        result = final_price(price, percent)
        st.code("def final_price(amount, discount):\n    return amount * (1 - discount / 100)", language="python")
        st.metric("Giá sau giảm", f"{result:,.0f} đ")

    else:
        st.subheader("Chuyển đổi dữ liệu JSON")
        name = st.text_input("Tên", "Lan")
        age = st.number_input("Tuổi", 1, 120, 20)
        skills = st.multiselect("Kỹ năng", ["Python", "Git", "SQL", "HTML", "Data"], ["Python", "Git"])
        payload = {"name": name, "age": age, "skills": skills}
        st.code("json_text = json.dumps(data, ensure_ascii=False, indent=2)", language="python")
        st.json(payload)
        st.download_button("Tải JSON", json.dumps(payload, ensure_ascii=False, indent=2), "student.json", "application/json")


def main() -> None:
    st.set_page_config(page_title="Python Journey · Interactive", page_icon="🐍", layout="wide")
    st.sidebar.title("🐍 Python Journey")
    section = st.sidebar.radio("Điều hướng", ["Tổng quan", "Lộ trình & tài liệu", "Phòng thực hành"])
    st.sidebar.divider()
    st.sidebar.caption("Python 3.12+ · 15 tuần · Beginner")
    if section == "Tổng quan":
        render_home()
    elif section == "Lộ trình & tài liệu":
        render_curriculum()
    else:
        render_playground()
    st.sidebar.markdown("---")
    st.sidebar.caption("Learn → Build → Test → Debug → Improve")


if __name__ == "__main__":
    main()
