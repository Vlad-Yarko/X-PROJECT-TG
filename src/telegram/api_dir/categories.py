from src.telegram.api_dir.pattern import Pattern

pants = ('pants', 'JEANS', 'PANTS', )
coats = ('coats', 'VEST', 'BOMBER', 'JACKET', 'OVERSHIRT', 'TRENCH', 'COAT')
sweaters = ('sweaters', 'HOODED', 'TURTLENECK', 'SWEATER', 'SHIRT', 'SWEATSHIRT', 'SLEEVE', 'ZIP', 'FLEECE', 'LONGSLEEVE', 'GOLF', 'SWEAT', 'HOODIE')
shoes = ('shoes', 'CONVERSE', )
summer = ('summer clothes', 'TEE', 'TOP')
underwear = ('underwear clothed', 'underpants')
bags = ('bags', 'BAG')

categories = (
    pants,
    coats,
    sweaters,
    shoes,
    summer,
    underwear,
    bags
)

brands = ('adidas',
          'CP COMPANY',
          'nike',
          'stone island',
          'CALVIN KLEIN',
          'MA.STRUM',
          'ALPHA INDUSTRIES',
          'PATAGONIA',
          'MA STRUM',
          'Carhartt',
          'New Balance',
          "Fred Perry",
          "Palm Angels",
          "C.P. Company",
          "C.P.Company",
          "POLO",
          "THE NORTH FACE",
          "ALPHA INDASTRIES PUFFER VEST ")


def find_brand_and_category(obj: Pattern):

    text = obj.text.lower()

    for brand in brands:
        if brand.lower() in text:
            obj.brand = brand
            break

    a = False
    for category in categories:
        for i in category[1:]:
            if i.lower() in text:
                obj.category = category[0]
                a = True
                break
        if a:
            break