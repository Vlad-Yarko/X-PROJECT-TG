from abc import ABC, abstractmethod
from src.telegram.api_dir.databases.requests import orm_add_product


class Pattern(ABC):
    def __init__(self, text, image, message_id):
        self.is_good = True
        self.text = text
        self.message_id = message_id
        self.photo = image
        self.brand = 'No brand'
        self.price_range = 'No price range'
        self.currency = 'UAH'
        self.channel_name = "No channel name"
        self.title = "No title"
        self.size = "One size"
        self.description = "No description"
        self.original_price = "No original_price"
        self.condition = "New"
        self.category = "Other"
        self.delivery_options = "No delivery options"
        self.url = "No url"
        self.payment_methods = "No payment methods"
        self.discounted_price = "No discounted price"
        self.discounted = False
        self.seller_contact = "No seller contact"


    @abstractmethod
    def get_properties(self):
        """
        Get properties from product
        """

        pass


    async def add_product(self):
        """
        Write all properties of product to Database
        """

        await orm_add_product(
            photo=self.photo,
            brand=self.brand,
            price_range=self.price_range,
            currency=self.currency,
            channel_name=self.channel_name,
            title=self.title,
            size=self.size,
            description=self.description,
            original_price=self.original_price,
            condition=self.condition,
            category=self.category,
            delivery_options=self.delivery_options,
            url=self.url,
            payments_methods=self.payment_methods,
            discounted_price=self.discounted_price,
            discounted=self.discounted,
            seller_contact=self.seller_contact)
