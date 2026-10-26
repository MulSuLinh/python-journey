# Week 14 — OOP đơn giản nhất

OOP là cách gom **dữ liệu** và **hành vi liên quan** vào một object. Không phải bài toán nào cũng cần class.

## 1. Class và object

- **Class**: bản mô tả để tạo object.
- **Object**: một giá trị cụ thể tạo ra từ class.
- **__init__**: khởi tạo dữ liệu ban đầu.
- **self**: object hiện tại.
- **Attribute**: dữ liệu của object.
- **Method**: hàm được định nghĩa trong class.
- **__str__**: cách hiển thị thân thiện khi dùng print(object).

~~~python
class Progress:
    def __init__(self, completed: int, total: int):
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"{self.completed}/{self.total}"
~~~

Dùng:

~~~python
progress = Progress(3, 4)
print(progress.percentage())  # 75.0
print(progress)               # 3/4
~~~

## 2. Composition — kết hợp object

Composition là khi object dùng một object hoặc hàm khác để làm công việc.

~~~python
class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)
~~~

Bot không cần biết cách strategy ra quyết định. Ta có thể thay strategy mà không viết lại class Bot.

## 3. Strategy

Một strategy là một quy tắc chọn hành động. Ví dụ, một strategy đi về phía mục tiêu:

~~~python
def move_toward_goal(state: dict[str, int]) -> str:
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"
~~~

Cần xét cả hai phía: mục tiêu lớn hơn thì đi right; mục tiêu nhỏ hơn thì đi left; đã tới mục tiêu thì wait.

## 4. Inheritance — kế thừa

Kế thừa dùng khi có quan hệ **“là một”** (is-a) tự nhiên.

~~~python
class Animal:
    def __init__(self, name: str):
        self.name = name

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"
~~~

Một Dog là một Animal, nên Dog dùng được thuộc tính name từ class cha.

## 5. Chọn cách nào?

- Dùng hàm khi chỉ cần thực hiện một việc.
- Dùng class khi dữ liệu và hành vi thuộc về cùng một đối tượng.
- Ưu tiên composition nếu muốn thay đổi hành vi dễ dàng.
- Dùng inheritance khi quan hệ “là một” thật rõ, không chỉ để giảm vài dòng code.

## Lệnh chạy và kiểm tra

~~~bash
python weeks/week-14-oop-essentials/examples/01_class_object.py
python weeks/week-14-oop-essentials/examples/02_composition.py
python weeks/week-14-oop-essentials/examples/03_basic_inheritance.py
python weeks/week-14-oop-essentials/checks/check_week.py
python -m pytest weeks/week-14-oop-essentials/checks/test_solutions.py
~~~

## Một câu tóm tắt

**Class là khuôn, object là thứ được tạo ra, composition là dùng object khác, inheritance là quan hệ “là một”.**
