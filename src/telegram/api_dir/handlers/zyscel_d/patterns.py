from re import IGNORECASE, compile, search

b = r"([\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*(?:\n{2}([\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)?(?:\n{2}([\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)?(?:\n{2}([\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)?)"


from src.telegram.api_dir.pattern import Pattern
from src.telegram.api_dir.categories import find_brand_and_category

from src.telegram.bot_dir.databases.requests import orm_add_product

a = r"(?:\n{2}([\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)?(?:\n{2}([\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)?"

prodano = r"..?(ПРОДАНо)..?\s\s?"

title_ = r"([\w ,()-|][^\n]+)\s{2}"

state_ = r".. ?([\w ,()-|][^\n]+)\n{2}"

size_ = r"[\w ,()-\\|]+: ?([\w ,()-\\|]*)"

add_size = r"([\w ,()-|][^\n]*)"

five_add_size = r"([\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*(?:\n{2}[\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)?(?:\n{2}[\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)?(?:\n{2}[\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)?)"

four_add_size = r"([\w ,()-|][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*\n[\w ,()-][^\n]*)"

double_add_size = r"([\w ,()-|][^\n]*(?:\n[\w ,()-][^\n]*)?)"

double_add_size_price = r"\n{2}([\w ,()-|]+(?:\n[\w+,()-]+)?)"

price_ = r"\n{2}[\w ,()-][^:]+..([\d ,\.\()-|]+)\s?(\w[^\n]+)"

discount_price_ = r"\n?Акційна ціна\s?:\s?([\d\.\-()|]*)\w*\n?"

add_description_ = r"\s?(Без патчу[\w \d|,\.\][^\n]*)"

new_size = r"\w+[^\n]([\w ()\.\|,]+\n(?:[\w ()\.\|,]+)?)"


pattern1 = compile(r"\n?" + title_ + state_ + size_ + r"\n" + double_add_size + r"\n{2}" + four_add_size + price_ , IGNORECASE)

# pattern2 = compile(r"\n?" + title_ + state_ + size_ + r"\n" + double_add_size + r"\n{2}" + five_add_size + r"\n{2}" + five_add_size + price_, IGNORECASE)

pattern2 = compile(r"\n?" + title_ + state_ + size_ + r"\n" + double_add_size + r"\n{2}" + five_add_size + price_, IGNORECASE)


pattern3 = compile(r"\n?" + title_ + state_ + size_ + price_ + double_add_size_price, IGNORECASE)

pattern4 = compile(r"\n?" + title_ + state_ + new_size + price_, IGNORECASE)

pattern5 = compile(r"\n?" + title_ + state_ + size_ + r"\n\n?" + double_add_size + price_, IGNORECASE)

pattern6 = compile(r"\n?" + title_ + state_ + size_ + price_, IGNORECASE)

pattern7 = compile(r"\n?" + title_ + state_ + price_[5:], IGNORECASE)

pattern8 = compile(r"\n?" + title_ + state_ + size_ + r"\n" + double_add_size + price_, IGNORECASE)


is_not_available_pattern = compile(r"\n?" + prodano, IGNORECASE)


class ZyscelPattern(Pattern):
    def get_properties(self):

        self.channel_name = "@zyscel_store"
        self.seller_contact = '@zyscel'
        self.url = f"https://t.me/zyscel_store/{self.message_id}"

        find_brand_and_category(self)

        while True:

            product = pattern1.search(self.text)

            if product:
                print(1)
                self.title = product.group(1)
                self.condition = product.group(2)
                self.size = product.group(3)
                self.description = '\n'.join((product.group(4), product.group(5)))
                self.original_price = product.group(6)
                self.currency = product.group(7)

                break

            product = pattern2.search(self.text)

            if product:
                print(2)
                self.title = product.group(1)
                self.condition = product.group(2)
                self.size = product.group(3)
                self.description = product.group(5)
                self.original_price = product.group(6)
                self.currency = product.group(7)

                break

            product = pattern3.search(self.text)

            if product:
                print(3)
                self.title = product.group(1)
                self.condition = product.group(2)
                self.size = product.group(3)
                self.original_price = product.group(4)
                self.currency = product.group(5)
                self.description = product.group(6)

                break

            product = pattern4.search(self.text)

            if product:
                print(4)

                self.title = product.group(1)
                self.condition = product.group(2)
                self.size = product.group(3).lstrip()
                self.original_price = product.group(4)
                self.currency = product.group(5)

                break

            product = pattern5.search(self.text)

            if product:
                print(5)

                self.title = product.group(1)
                self.condition = product.group(2)
                self.size = product.group(3)
                self.description = product.group(4)
                self.original_price = product.group(5)

                break

            product = pattern6.search(self.text)
            if product:
                print(6)
                self.title = product.group(1)
                self.condition = product.group(2)
                self.size = product.group(3)
                self.original_price = product.group(4)
                self.currency = product.group(5)

                break

            product = pattern7.search(self.text)

            if product:
                print(7)
                self.title = product.group(1)
                self.condition = product.group(2)
                self.original_price = product.group(3)
                self.currency = product.group(4)

                break

            product = pattern8.search(self.text)
            if product:
                print(8)
                self.title = product.group(1)
                self.condition = product.group(2)
                self.size = product.group(3)
                self.description = product.group(4)
                self.original_price = product.group(5)
                self.currency = product.group(6)

                break

            else:
                print('JOJO')
                self.is_good = False
                return
        if d := search(discount_price_, self.text):
            self.discounted_price = d.group(1)
            self.discounted = True
        if add_desc := search(add_description_, self.text):
            self.description += '\n' + add_desc.group(1)
        if self.currency.lower() == 'грн':
            self.currency = "UAH"
        if self.condition.lower() == 'вживана річ':
            self.condition = "Used"
        if self.condition.lower() == "нова річ":
            self.condition = "New"
        return


async def make_product(text, photo, message_id):
    if not "Купити: @zycsel".lower() in text.lower():
        return
    prod = ZyscelPattern(text=text, image=photo, message_id=message_id)
    prod.get_properties()
    if prod.is_good:
        await prod.add_product()
        return 'Success'
    return "Error"
