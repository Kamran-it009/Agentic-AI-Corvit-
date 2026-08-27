# 1. NUMERICAL TYPES
# ==========================================
age: int = 25
price: float = 99.99
complex_num: complex = 3 + 4j


# 1.  Boolean Type
# ==========================================
is_active: bool = True


# 2. STRING TYPE
# ==========================================
name: str = "Mohammed"


# 4. SEQUENCE TYPES
# ==========================================
numbers: list[int] = [1, 2, 3, 4]
coordinates: tuple[float, float] = (31.5204, 74.3587)  # Fixed length/types
flexible_tuple: tuple[str, ...] = ("a", "b", "c")       # Arbitrary length of strings


# 5. MAPPING TYPES
# ==========================================
user_scores: dict[str, int] = {"Alice": 95, "Bob": 88}



# 7. FUNCTIONS
# ==========================================
def add_numbers(x: int, y: int) -> int:
    return x + y


# 6. CLASSES
# ==========================================
class User:
    def __init__(self, name: str, user_id: int) -> None:
        self.name: str = name
        self.user_id: int = user_id

    def get_info(self) -> str:
        return f"User {self.name} (ID: {self.user_id})"

# Using a custom class as a type hint
current_user: User = User("Kamran", 1001)

# ==========================================
from typing import Optional, Union
# Optional Type (Value can be int or None)
def find_user(user_id: int) -> Optional[User]:
    if user_id == 1001:
        return current_user
    return None

# Union Type (Can accept int OR float)
def process_value(val: Union[int, float]) -> float:
    return float(val) * 2.5

