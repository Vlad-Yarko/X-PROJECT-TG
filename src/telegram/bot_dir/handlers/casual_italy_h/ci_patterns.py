from re import IGNORECASE, compile

from src.telegram.bot_dir.databases.requests import orm_add_product


title_ = r"..?([\w ,()-][^\n]+)\s{2}"

size_ = r"[\w ,()-\\]+: ?([\w ,()-\\]*)\n"

add_size = r"([\w ,()-][^\n]*)\n"

price_ = r"[\w ,()-][^:]+..([\w ,()-][^\n]+)"

pattern1 = compile(r"\n?" + title_ + add_size + size_ + price_, IGNORECASE)
pattern2 = compile(r"\n?" + title_ + size_ + price_, IGNORECASE)
pattern3 = compile(r"\n?" + title_ + price_, IGNORECASE)


# patterns = tuple([pattern1, pattern2, pattern3, pattern4, pattern5, pattern6])


async def get_all_positions_c(text, photo, session):
    sold = "Is available"
    title = "No title"
    state = "Unknown"
    size = "No size"
    description = "No description"
    price = "No price"
    source = 'Casual Italy'

    while True:

        product = pattern1.match(text)

        if product:
            print(1)
            title = product.group(1)
            description = product.group(2)
            size = product.group(3)
            price = product.group(4)
            break

        product = pattern2.match(text)
        if product:
            print(2)
            title = product.group(1)
            size = product.group(2)
            price = product.group(3)
            break

        product = pattern3.match(text)
        if product:
            print(3)
            title = product.group(1)
            price = product.group(2)
            break

        else:
            print('JOJO')
            break
    await orm_add_product(session, photo, source, title, size, description, price, state, sold)
    return
