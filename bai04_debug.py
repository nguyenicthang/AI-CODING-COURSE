"""Chuong trinh tinh diem trung binh - bai04 da sua loi."""

from __future__ import annotations

import os
from typing import Iterable


def get_api_key() -> str:
  """Lay API key tu bien moi truong; khong hardcode trong source.

  Returns:
      API key string.

  Raises:
      RuntimeError: Neu bien API_KEY chua duoc cau hinh.
  """
  key = os.environ.get("API_KEY", "").strip()
  if not key:
    raise RuntimeError(
      "Chua cau hinh API_KEY. Dat bien moi truong hoac file .env (khong commit)."
    )
  return key


def calculate_average_grade(grades: Iterable[float]) -> float:
  """Tinh diem trung binh tu danh sach diem.

  Args:
      grades: Iterable cac diem so (khong duoc rong).

  Returns:
      Diem trung binh.

  Raises:
      ValueError: Neu danh sach rong hoac khong co diem hop le.
  """
  grade_list = list(grades)
  if not grade_list:
    raise ValueError("Danh sach diem rong — khong the tinh trung binh.")

  total = 0.0
  for grade in grade_list:
    total += float(grade)

  return total / len(grade_list)


def main() -> None:
  """Ham chinh: demo tinh diem va (tuy chon) doc API key."""
  student_grades = [8, 7, 9, 10, 6]
  result = calculate_average_grade(student_grades)
  print(f"Diem trung binh la: {result:.2f}")

  # Xu ly danh sach rong — khong de ZeroDivisionError
  empty_grades: list[float] = []
  try:
    calculate_average_grade(empty_grades)
  except ValueError as exc:
    print(f"Loi hop le: {exc}")

  # API key chi dung khi can goi API — doc tu moi truong
  try:
    api_key = get_api_key()
    # Vi du: headers = {"Authorization": f"Bearer {api_key}"}
    _ = api_key  # tranh warning "unused" neu chua goi API that
  except RuntimeError as exc:
    print(f"Canh bao cau hinh: {exc}")


if __name__ == "__main__":
  main()