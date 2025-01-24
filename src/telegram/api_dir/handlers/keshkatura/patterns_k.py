from re import IGNORECASE, compile, search

from src.telegram.api_dir.pattern import Pattern

from src.telegram.bot_dir.databases.requests import orm_add_product

from src.telegram.api_dir.categories import find_brand_and_category


title_ = r"([a-zA-Z -|][^\n]{5,60})"

size_ = r"Розмір\s?:?-? ?([-()| \d\w\\\.\,][^\n]*)"

condition_ = r"([\w\d\\\.\ -]*стан ?:?-? ?[\w\d\\\.\ -]*[^\n])"

price_ = r"Ціна\s?:?-? ?([\d ,\.\()-|][^\n]*)"


class KeshkaturaPattern(Pattern):

    def get_properties(self):

        find_brand_and_category(self)

        self.seller_contact = "@luxurybuyer_dasha\n@denyszinchenko"
        self.channel_name = "@casual_italy"
        self.url = f"https://t.me/casual_italy/{self.message_id}"

        title = search(title_, self.text, IGNORECASE)
        if title:
            self.title = title.group(1).strip()
        size = search(size_, self.text, IGNORECASE)
        if size:
            self.size = size.group(1).strip()
        condition = search(condition_, self.text, IGNORECASE)
        if condition:
            condition = condition.group(1).lower().replace('стан', "")
            self.condition = condition.strip()
        price = search(price_, self.text, IGNORECASE)
        if price:
            self.original_price = price.group(1).strip()
        if 'грн' or 'uah' or 'uan' in self.text.lower():
            self.currency = 'UAH'

        return


async def make_product(text, photo, message_id):
    prod = KeshkaturaPattern(text=text, image=photo, message_id=message_id)
    prod.get_properties()
    await prod.add_product()
    return 'Success'

