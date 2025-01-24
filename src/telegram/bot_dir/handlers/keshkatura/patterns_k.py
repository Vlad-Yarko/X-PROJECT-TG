from re import IGNORECASE, compile

from src.telegram.bot_dir.databases.requests import orm_add_product

prodano = r".*?(продано).*?"

title_ = r"^(.*?(?=\n•|\nРозмір|\nСтан|\nЦіна|\n))"

size_ = r"(Розмір)\s*[:\-–—]?\s*([^\n]+)"
state_ = r"(Стан|Ідеальний стан|Чудовий стан|Відмінний стан|Новий|Б/У)\s*[:\-–—]?\s*([^\n]+)"
price_ = r"(Ціна\s?:?\s?)[^\n]+"

title_pattern = compile(title_, IGNORECASE)
size_pattern = compile(size_, IGNORECASE)
state_pattern = compile(state_, IGNORECASE)
price_pattern = compile(price_, IGNORECASE)
is_not_available_pattern = compile(prodano, IGNORECASE)


async def get_all_positions_k(text, photo, session):
    prod = is_not_available_pattern.match(text)
    if prod:
        sold = prod.group(1)
    else:
        sold = 'Is available'

    title = "No title"
    state = "Unknown"
    size = "No size"
    description = "No description"
    price = "No price"

    title_match = title_pattern.search(text)
    if title_match:
        title = title_match.group(1).strip()

    size_match = size_pattern.search(text)
    if size_match:
        size = size_match.group(2).strip()

    state_match = state_pattern.search(text)
    if state_match:
        state = state_match.group(2).strip()

    price_match = price_pattern.search(text)
    if price_match:
        price = price_match.group(0).strip()

    if title and price:
        await orm_add_product(session, photo, source="keshkatura", title=title, size=size,
                              description=None, price=price, state=state,
                              available=sold)
        print(f"Назва: {title}, Розмір: {size}, Стан: {state}, Ціна: {price}")
    else:
        print("JOJO")
