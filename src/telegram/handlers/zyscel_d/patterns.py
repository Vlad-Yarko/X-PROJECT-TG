from re import IGNORECASE, compile

from src.telegram.databases.requests import orm_add_product


prodano = r"..?(ПРОДАНо)..?\s\s?"

title_ = r"([\w ,()-][^\n]+)\s{2}"

state_ = r".. ?([\w ,()-][^\n]+)\n{2}"

size_ = r"[\w ,()-\\]+: ?([\w ,()-\\]*)"

add_size = r"([\w ,()-][^\n]*)"

five_add_size = r"([\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)"

four_add_size = r"([\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)"

double_add_size = r"([\w ,()-][^\n]*(?:\n[\w ,()-][^\n]*)?)"

double_add_size_price = r"\n{2}([\w ,()-]+(?:\n[\w+,()-]+)?)"

price_ = r"\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)"


pattern1 = compile(r"\n?" + title_ + state_ + size_ + r"\n" + double_add_size + r"\n{2}" + four_add_size + price_, IGNORECASE)

pattern2 = compile(r"\n?" + title_ + state_ + size_ + r"\n" + double_add_size + r"\n{2}" + five_add_size + r"\n{2}" + five_add_size + price_, IGNORECASE)

pattern3 = compile(r"\n?" + title_ + state_ + size_ + r"\n" + double_add_size + price_, IGNORECASE)

pattern4 = compile(r"\n?" + title_ + state_ + size_ + r"\n" + double_add_size + r"\n{2}" + five_add_size + price_, IGNORECASE)

pattern5 = compile(r"\n?" + title_ + state_ + size_ + price_ + double_add_size_price, IGNORECASE)

pattern6 = compile(r"\n?" + title_ + state_ + price_[5:], IGNORECASE)

is_not_available_pattern = compile(r"\n?" + prodano, IGNORECASE)


patterns = tuple([pattern1, pattern2, pattern3, pattern4, pattern5, pattern6])


async def get_all_positions_z(text, photo, session):
    prod = is_not_available_pattern.match(text)
    if prod:
        sold = prod.group(1)
    else:
        sold = "Is available"
    title = "No title"
    state = "Unknown"
    size = "No size"
    description = "No description"
    price = "No price"
    source = 'Zyscel'

    while True:

        product = pattern1.search(text)

        if product:
            print(1)
            title = product.group(1)
            state = product.group(2)
            size = product.group(3)
            description = '\n'.join((product.group(4), product.group(5)))
            price = product.group(6)

            break

        product = pattern2.search(text)
        if product:
            print(2)
            title = product.group(1)
            state = product.group(2)
            size = product.group(3)
            description = '\n'.join((product.group(4), product.group(5), product.group(6)))
            price = product.group(7)

            break

        product = pattern3.search(text)
        if product:
            print(3)
            title = product.group(1)
            state = product.group(2)
            size = product.group(3)
            description = product.group(4)
            price = product.group(5)

            break

        product = pattern4.search(text)

        if product:
            print(4)
            title = product.group(1)
            state = product.group(2)
            size = product.group(3)
            description = '\n'.join((product.group(4), product.group(5)))
            price = product.group(6)

            break

        product = pattern5.search(text)

        if product:
            print(5)
            title = product.group(1)
            state = product.group(2)
            size = product.group(3)
            price = product.group(4)
            description = product.group(5)

            break

        product = pattern6.search(text)

        if product:
            print(6)
            title = product.group(1)
            state = product.group(2)
            price = product.group(3)

        else:
            print('JOJO')
            break
    await orm_add_product(session, photo, source, title, size, description, price, state, sold)
    return
