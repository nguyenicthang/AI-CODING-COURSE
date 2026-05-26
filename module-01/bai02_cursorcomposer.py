# Chương trình máy tính đơn giản

VALID_OPERATORS = ("+", "-", "*", "/")


def read_number(prompt: str) -> float:
    """
    Đọc một số từ người dùng.
    Lặp lại cho đến khi nhập hợp lệ.
    """
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ (ví dụ: 10 hoặc 3.5).")


def read_operator() -> str:
    """
    Đọc phép tính từ người dùng.
    Chỉ chấp nhận +, -, *, /
    """
    while True:
        op = input("Nhập phép tính (+, -, *, /): ").strip()
        if op in VALID_OPERATORS:
            return op
        print("Lỗi: Phép tính không hợp lệ. Chỉ dùng +, -, *, /")


def calculate(a: float, b: float, operator: str) -> float | None:
    """
    Thực hiện phép tính giữa a và b.
    Trả về None nếu chia cho 0.
    """
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            print("Lỗi: Không thể chia cho 0.")
            return None
        return a / b
    return None


def ask_continue() -> bool:
    """Hỏi người dùng có muốn tính tiếp không."""
    while True:
        answer = input("Bạn có muốn tính tiếp không? (y/n): ").strip().lower()
        if answer in ("y", "yes", "c", "co"):
            return True
        if answer in ("n", "no", "k", "khong", "không"):
            return False
        print("Lỗi: Vui lòng nhập y (có) hoặc n (không).")


def run_calculator_once() -> None:
    """Chạy một lần tính toán."""
    print("\n--- Máy tính đơn giản ---")
    first_number = read_number("Nhập số thứ nhất: ")
    second_number = read_number("Nhập số thứ hai: ")
    operator = read_operator()

    result = calculate(first_number, second_number, operator)
    if result is not None:
        print(f"Kết quả: {first_number} {operator} {second_number} = {result}")


def main() -> None:
    """Hàm chính của chương trình."""
    print("Chào mừng bạn đến với máy tính đơn giản!")
    while True:
        run_calculator_once()
        if not ask_continue():
            print("Cảm ơn bạn đã sử dụng. Tạm biệt!")
            break


if __name__ == "__main__":
    main()