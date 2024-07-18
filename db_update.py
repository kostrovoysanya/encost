import sqlite3

def add_machines_to_db():
    # Подключение к базе данных
    conn = sqlite3.connect('client.sqlite')
    cursor = conn.cursor()

    # Добавление станков
    machines = [
        ("Сварочный аппарат №1", 'true'),
        ("Пильный аппарат №2", 'true'),
        ("Фрезер №3", 'true')
    ]
    cursor.executemany("INSERT INTO endpoints (name, active) VALUES (?, ?)", machines)

    # Получение причин простоев для существующих станков
    reasons_query = """
    SELECT reason_name, reason_hierarchy
    FROM endpoint_reasons
    WHERE endpoint_id IN (
        SELECT id FROM endpoints WHERE name IN ('Фрезерный станок', 'Старый, ЧПУ', 'Сварка')
    )
    """
    reasons = cursor.execute(reasons_query).fetchall()

    # Получение id новых станков
    new_machines_query = """
    SELECT id
    FROM endpoints
    WHERE name IN ('Сварочный аппарат №1', 'Пильный аппарат №2', 'Фрезер №3')
    """
    new_machines_ids = cursor.execute(new_machines_query).fetchall()

    # Копирование причин простоев на новые станки
    for machine_id in new_machines_ids:
        for reason in reasons:
            cursor.execute("INSERT INTO endpoint_reasons (endpoint_id, reason_name, reason_hierarchy) VALUES (?, ?, ?)", (machine_id[0], reason[0], reason[1]))

    # Определение группы "Цех №2" для новых станков
    new_group_name = 'Цех №2'
    machines_to_group = new_machines_ids + cursor.execute("""
        SELECT id
        FROM endpoints
        WHERE name IN ('Пильный станок', 'Старый ЧПУ')
    """).fetchall()

    for machine_id in machines_to_group:
        cursor.execute("INSERT INTO endpoint_groups (endpoint_id, name) VALUES (?, ?)", (machine_id[0], new_group_name))

    # Сохранение изменений и закрытие подключения
    conn.commit()
    conn.close()

# Запуск функции
add_machines_to_db()