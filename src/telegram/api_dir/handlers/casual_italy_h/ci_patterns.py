from re import IGNORECASE, compile, search

from src.telegram.api_dir.pattern import Pattern

from src.telegram.api_dir.categories import find_brand_and_category

title_ = r"..?([\w ,()-\\|][^\n]+)\s\s?(?:❌?\w{0,7}❌?)?\s\s?"

size_ = r"[\w ,()-\\|]+: ?([\w ,()-\\]*)\n\n?"

add_size = r"([\w ,()-\\|][^\n]*)\n\n?"

price_ = r"[\w ,()-\\|][^:]+..([\d ,\.\()-]+)"

delivery_ = r"(📦🇺🇦Доставка в Україну БЕЗКОШТОВНА \(5-7 робочих днів\)\n?📦🇪🇺Доставка по Європі 1-5 днів)"
pay_ = r"💶? ?Варіанти оплати:\s?\s?([\w ,\\|][^\n]*)"

pattern1 = compile(r"\n?" + title_ + add_size + size_ + price_, IGNORECASE)
pattern2 = compile(r"\n?" + title_ + size_ + price_, IGNORECASE)
pattern3 = compile(r"\n?" + title_ + price_, IGNORECASE)


class CasualItalyPattern(Pattern):

    def get_properties(self):

        find_brand_and_category(self)

        if delivery := search(delivery_, self.text, IGNORECASE):
            self.delivery_options = delivery.group(1)

        if pay := search(pay_, self.text, IGNORECASE):
            self.payment_methods = pay.group(1)

        self.seller_contact = "@luxurybuyer_dasha\n@denyszinchenko"
        self.channel_name = "@casual_italy"
        self.url = f"https://t.me/casual_italy/{self.message_id}"

        while True:

            product = pattern1.match(self.text)

            if product:
                print(1)
                self.title = product.group(1)
                self.description = product.group(2)
                self.size = product.group(3)
                self.original_price = product.group(4)
                break

            product = pattern2.match(self.text)
            if product:
                print(2)
                self.title = product.group(1)
                self.size = product.group(2)
                self.original_price = product.group(3)
                break

            product = pattern3.match(self.text)
            if product:
                print(3)
                self.title = product.group(1)
                self.original_price = product.group(2)
                break

            else:
                print('JOJO')
                self.is_good = False
                return
        return


async def make_product(text, photo, message_id):
    if "📦🇺🇦Доставка в Україну БЕЗКОШТОВНА (5-7 робочих днів)\n📦🇪🇺Доставка по Європі 1-5 днів" in text:
        prod = CasualItalyPattern(text=text, image=photo, message_id=message_id)
        prod.get_properties()
        if prod.is_good:
            await prod.add_product()
            return 'Success'
    return "Error"
