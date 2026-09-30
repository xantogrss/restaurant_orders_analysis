import time
import random
from data_processor.data import orders
from data_processor.processors import (
    get_unique_dishes,
    get_unique_categories,
    group_positions_by_order,
    count_dishes,
    create_order_index,
)
from data_processor.analytics import (
    calculate_order_totals,
    calculate_average_order_value,
    find_most_expensive_item,
    find_most_popular_dish,
    create_price_filter,
    register_new_order_item,
)

def run_benchmark():
    """Експериментальна частина: порівняння швидкості пошуку List vs Dict."""
    print("\n--- ЕКСПЕРИМЕНТАЛЬНА ЧАСТИНА (BENCHMARK) ---")
    sizes = [1_000, 10_000, 100_000]
    
    print(f"{'Кількість записів':<20} | {'List Search (сек)':<20} | {'Dict Search (сек)':<20}")
    print("-" * 65)
    
    for size in sizes:
        # Генерація синтетичних даних
        dataset = [
            {"order_id": i, "dish_name": f"Dish_{i}", "price": random.uniform(10, 500)}
            for i in range(size)
        ]
        target_id = size - 1 # Шукаємо найостанніший елемент (найгірший випадок для list)
        
        # 1. Пошук у List O(N)
        start = time.perf_counter()
        _ = next((item for item in dataset if item["order_id"] == target_id), None)
        list_time = time.perf_counter() - start
        
        # 2. Пошук у Dict O(1)
        index_dict = {item["order_id"]: item for item in dataset}
        start = time.perf_counter()
        _ = index_dict.get(target_id)
        dict_time = time.perf_counter() - start
        
        print(f"{size:<20} | {list_time:<20.8f} | {dict_time:<20.8f}")

def main():
    print("=== ЛАБОРАТОРНА РОБОТА №2: ВАРІАНТ 11 (Ресторан) ===")
    
    # 1. Унікальні страви та категорії
    print("\n1. Унікальні страви:", get_unique_dishes(orders))
    print("2. Унікальні категорії:", get_unique_categories(orders))
    
    # 2. Агрегація: Суми замовлень
    order_totals = calculate_order_totals(orders)
    print("\n3. Сума кожного замовлення:")
    for order_id, total in order_totals.items():
        print(f"   Замовлення #{order_id}: {total:.2f} грн")
        
    # 3. Середня вартість замовлення (*args)
    avg_price = calculate_average_order_value(*order_totals.values())
    print(f"\n4. Середня вартість замовлення: {avg_price:.2f} грн")
    
    # 4. Найдорожча позиція & Найпопулярніша страва
    expensive = find_most_expensive_item(orders)
    popular = find_most_popular_dish(orders)
    print(f"\n5. Найдорожча позиція: {expensive['dish_name']} ({expensive['price']} грн)")
    print(f"6. Найпопулярніша страва: {popular[0]} (замовлено {popular[1]} раз(и))")
    
    # 5. Counter та Групування
    print("\n7. Статистика підрахунку страв (Counter):")
    for dish, count in count_dishes(orders).items():
        print(f"   {dish}: {count}")
        
    # 6. Фільтрація через Closure (Замикання)
    min_price_150 = create_price_filter(150.0)
    expensive_items = [item for item in orders if min_price_150(item)]
    print("\n8. Страви дорожчі за 150 грн (через Closure):")
    for item in expensive_items:
        print(f"   - {item['dish_name']} ({item['price']} грн)")
        
    # 7. Створення нового запису (**kwargs)
    new_item = register_new_order_item(order_id=106, dish_name="Борщ", category="Перші страви", price=160.0)
    print("\n9. Нова позиція створена через **kwargs:", new_item)
    
    # 8. Запуск замірiв часу
    run_benchmark()

if __name__ == "__main__":
    main()