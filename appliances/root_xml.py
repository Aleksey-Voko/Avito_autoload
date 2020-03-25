from pathlib import Path

from lxml import etree
from lxml.etree import CDATA


def save_root_xml(xml_file_path, advert_dicts_list):
    """
    :param xml_file_path: path to xml file
    :param advert_dicts_list: list of dicts with ads
    """

    root = etree.Element('Ads', formatVersion='3', target='Avito.ru')

    for advert_dict in advert_dicts_list:
        ad = etree.SubElement(root, 'Ad')

        ad_id = etree.SubElement(ad, 'Id')
        ad_id.text = advert_dict['Id']

        if 'DateBegin' in advert_dict and advert_dict['DateBegin']:
            date_begin = etree.SubElement(ad, 'DateBegin')
            date_begin.text = advert_dict['DateBegin']

        if 'DateEnd' in advert_dict and advert_dict['DateEnd']:
            date_end = etree.SubElement(ad, 'DateEnd')
            date_end.text = advert_dict['DateEnd']

        if 'ListingFee' in advert_dict and advert_dict['ListingFee']:
            listing_fee = etree.SubElement(ad, 'ListingFee')
            listing_fee.text = advert_dict['ListingFee']

        if ('AdStatus' in advert_dict
                and advert_dict['AdStatus']
                and advert_dict['AdStatus'] != 'Free'):
            ad_status = etree.SubElement(ad, 'AdStatus')
            ad_status.text = advert_dict['AdStatus']

        if 'AvitoId' in advert_dict and advert_dict['AvitoId']:
            avito_id = etree.SubElement(ad, 'AvitoId')
            avito_id.text = advert_dict['AvitoId']

        if ('AllowEmail' in advert_dict
                and advert_dict['AllowEmail']
                and advert_dict['AllowEmail'] != 'Да'):
            allow_email = etree.SubElement(ad, 'AllowEmail')
            allow_email.text = advert_dict['AllowEmail']

        if 'ManagerName' in advert_dict and advert_dict['ManagerName']:
            manager_name = etree.SubElement(ad, 'ManagerName')
            manager_name.text = advert_dict['ManagerName']

        if 'ContactPhone' in advert_dict and advert_dict['ContactPhone']:
            contact_phone = etree.SubElement(ad, 'ContactPhone')
            contact_phone.text = advert_dict['ContactPhone']

        address = etree.SubElement(ad, 'Address')
        address.text = advert_dict['Address']

        if ('Latitude' in advert_dict
                and advert_dict['Latitude']
                and 'Longitude' in advert_dict
                and advert_dict['Longitude']):
            latitude = etree.SubElement(ad, 'Latitude')
            latitude.text = advert_dict['Latitude']
            longitude = etree.SubElement(ad, 'Longitude')
            longitude.text = advert_dict['Longitude']

        category = etree.SubElement(ad, 'Category')
        category.text = advert_dict['Category']

        if 'GoodsType' in advert_dict and advert_dict['GoodsType']:
            goods_type = etree.SubElement(ad, 'GoodsType')
            goods_type.text = advert_dict['GoodsType']

        if 'AdType' in advert_dict and advert_dict['AdType']:
            ad_type = etree.SubElement(ad, 'AdType')
            ad_type.text = advert_dict['AdType']

        title = etree.SubElement(ad, 'Title')
        title.text = advert_dict['Title']

        description = etree.SubElement(ad, 'Description')
        if advert_dict['Description'].startswith('<'):
            description.text = CDATA(advert_dict['Description'])
        else:
            description.text = advert_dict['Description']

        price = etree.SubElement(ad, 'Price')
        price.text = advert_dict['Price']

        if advert_dict['Category'] in (
            'Бытовая техника',
            'Мебель и интерьер',
            'Посуда и товары для кухни',
            'Ремонт и строительство',
        ):
            condition = etree.SubElement(ad, 'Condition')
            condition.text = advert_dict['Condition']

        images = etree.SubElement(ad, 'Images')
        if advert_dict['Images'][0].startswith('http'):
            for img_url in advert_dict['Images']:
                etree.SubElement(images, 'Image', url=img_url)
        else:
            for img_name in advert_dict['Images']:
                etree.SubElement(images, 'Image', name=img_name)

        if 'VideoURL' in advert_dict and advert_dict['VideoURL']:
            video_url = etree.SubElement(ad, 'VideoURL')
            video_url.text = advert_dict['VideoURL']

    etree.indent(root, space='    ')  # WTF: ???
    handle = etree.tostring(root, pretty_print=True, encoding='utf-8',
                            xml_declaration=True)
    Path(xml_file_path).parent.mkdir(exist_ok=True)
    with open(xml_file_path, 'bw') as f_out:
        f_out.write(handle)


if __name__ == '__main__':
    file_name = 'out_xml_file.xml'
    path = Path('out_xml') / file_name

    ad_dicts = [
        {
            'Id': '723681273',
            'DateBegin': '2020-04-01T05:00:00+03:00',
            'DateEnd': '2020-05-01T05:00:00+03:00',
            'AdStatus': 'TurboSale',
            'AllowEmail': 'Да',
            'ManagerName': 'Иван Петров-Водкин',
            'ContactPhone': '8 800 200 80 01',
            'Address': 'Владимирская область, г. Владимир, ул. Гагарина, 1',
            'Category': 'Бытовая техника',
            'GoodsType': 'Стиральные машины',
            'AdType': 'Товар приобретен на продажу',
            'Title': 'Стиральная машина Candy GC4 1051 D',
            'Description': '''\
<p>Характеристики:</p>
<ul>
<li>отдельно стоящая стиральная машина
<li>60x40x85 см
<li>фронтальная загрузка
<li>стирка до 5 кг
<li>класс энергопотребления: A+
<li>электронное управление
<li>отжим при 1000 об/мин
<li>защита от протечек
</ul>\
''',
            'Price': '15000',
            'Condition': 'Новый',
            'Images': [
                'http://img.test.ru/8F7B-4A4F3A0F2BA1.jpg',
                'http://img.test.ru/8F7B-4A4F3A0F2XA3.jpg',
            ],
            'VideoURL': 'http://www.youtube.com/watch?v=YKmDXNrDdBI',
        },
        {
            'Id': 'remont_i_stroitelstvo001',
            'AdStatus': 'Free',
            'AllowEmail': 'Нет',
            'Address': 'Санкт-Петербург, Лиговский проспект, 1',
            'ContactPhone': '8 800 200 80 01',
            'Category': 'Ремонт и строительство',
            'GoodsType': 'Инструменты',
            'AdType': 'Товар приобретен на продажу',
            'Title': 'Перфоратор Makita HR3200C',
            'Description': '''\
Перфоратор имеет три режима работы: сверление, сверление с ударом, долбление.
 
Мощность, Вт 850 
Max диаметр сверления коронкой (бетон), мм: 90 
Max диаметр сверления\
''',
            'Price': '250000',
            'Condition': 'Новый',
            'Images': [
                '8F7B-4A4F3A0F2BA1.jpg',
                '8F7B-4A4F3A0F2XA3.jpg',
            ],
        },
        {
            'Id': 'mebel_i_interer002',
            'AdStatus': 'Free',
            'AllowEmail': 'Нет',
            'Address': 'Москва, улица Лесная, 9',
            'ContactPhone': '8 800 200 80 01',
            'Category': 'Мебель и интерьер',
            'GoodsType': 'Кровати, диваны и кресла',
            'AdType': 'Товар от производителя',
            'Title': 'Кровать детская Легенда 24',
            'Description': 'Спальное место: 80х160 см, габариты: 1642×882×500 мм, материал: ЛДСП, цвет корпуса: венге светлый',
            'Price': '25000',
            'Condition': 'Новый',
            'Images': [
                '8F7B-4A4F3A0F2BA1.jpg',
                '8F7B-4A4F3A0F2XA3.jpg',
            ],
        },
    ]

    save_root_xml(path, ad_dicts)
