from typing import Callable
from data_processor.decorators import measure_time

@measure_time
def calculate_order_totals(orders: list[dict]) -> dict[int, float]:
    """Обчислює суму кожного замовлення."""
    totals = defaultdict_sum(orders)
    return totals

def defaultdict_sum(orders: list[dict]) -> dict[int, float]:
    totals = {}
    for item in orders:
        o_id = item["order_id"]
        totals[o_id] = totals.get(o_id, 0.0) + item["price"]
    return totals

def calculate_average_order_value(*order_totals: float) -> float:
    """Приймає суми замовлень через *args та повертає середнє значення."""
    if not order_totals:
        return 0.0
    return sum(order_totals) / len(order_totals)

def find_most_expensive_item(orders: list[dict]) -> dict | None:
    """Пошук найдорожчої позиції за допомогою max() та lambda."""
    if not orders:
        return None
    return max(orders, key=lambda item: item["price"])

def find_most_popular_dish(orders: list[dict]) -> tuple[str, int] | None:
    """Пошук найпопулярнішої страви."""
    if not orders:
        return None
    counts = Counter_dishes(orders)
    return counts.most_common(1)[0]

def Counter_dishes(orders: list[dict]):
    from collections import Counter
    return Counter(item["dish_name"] for item in orders)

def create_price_filter(min_price: float) -> Callable[[dict], bool]:
    """Closure (Замикання): створює функцію-фільтр за ціною."""
    def predicate(item: dict) -> bool:
        return item["price"] >= min_price
    return predicate

def register_new_order_item(**fields) -> dict:
    """Приймає довільні параметри страви через **kwargs і повертає dict."""
    return dict(fields)