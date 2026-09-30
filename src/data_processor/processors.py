from collections import Counter, defaultdict, deque

def get_unique_dishes(orders: list[dict]) -> set[str]:
    """Повертає множину унікальних страв (set comprehension)."""
    return {item["dish_name"] for item in orders}

def get_unique_categories(orders: list[dict]) -> set[str]:
    """Повертає множину унікальних категорій (set comprehension)."""
    return {item["category"] for item in orders}

def group_positions_by_order(orders: list[dict]) -> dict[int, list[dict]]:
    """Групує позиції за номером замовлення з використанням defaultdict."""
    grouped = defaultdict(list)
    for item in orders:
        grouped[item["order_id"]].append(item)
    return dict(grouped)

def count_dishes(orders: list[dict]) -> Counter:
    """Підраховує кількість кожної страви за допомогою Counter."""
    return Counter(item["dish_name"] for item in orders)

def create_order_index(orders: list[dict]) -> dict[int, list[dict]]:
    """Dict comprehension: швидкий індекс за order_id."""
    index = defaultdict(list)
    for item in orders:
        index[item["order_id"]].append(item)
    return dict(index)

def create_history_tracker(max_size: int = 5):
    """Використання deque з collections для відстеження історії операцій."""
    return deque(maxlen=max_size)