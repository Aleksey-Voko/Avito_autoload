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

        date_begin = etree.SubElement(ad, 'DateBegin')
        date_begin.text = advert_dict['DateBegin']

        listing_fee = etree.SubElement(ad, 'ListingFee')
        listing_fee.text = advert_dict['ListingFee']

        ad_status = etree.SubElement(ad, 'AdStatus')
        ad_status.text = advert_dict['AdStatus']

        manager_name = etree.SubElement(ad, 'ManagerName')
        manager_name.text = advert_dict['ManagerName']

        contact_phone = etree.SubElement(ad, 'ContactPhone')
        contact_phone.text = advert_dict['ContactPhone']

        address = etree.SubElement(ad, 'Address')
        address.text = advert_dict['Address']

        category = etree.SubElement(ad, 'Category')
        category.text = advert_dict['Category']

        goods_type = etree.SubElement(ad, 'GoodsType')
        goods_type.text = advert_dict['GoodsType']

        # Не в этой категории
        # ad_type = etree.SubElement(ad, 'AdType')
        # ad_type.text = advert_dict['AdType']

        title = etree.SubElement(ad, 'Title')
        title.text = advert_dict['Title']

        description = etree.SubElement(ad, 'Description')
        description.text = CDATA(advert_dict['Description'])

        price = etree.SubElement(ad, 'Price')
        price.text = advert_dict['Price']

        condition = etree.SubElement(ad, 'Condition')
        condition.text = advert_dict['Condition']

        images = etree.SubElement(ad, 'Images')
        for img_url in advert_dict['Images']:
            etree.SubElement(images, 'Image', url=img_url)

    etree.indent(root, space='    ')  # WTF: ???
    handle = etree.tostring(root, pretty_print=True, encoding='utf-8',
                            xml_declaration=True)
    Path(xml_file_path).parent.mkdir(exist_ok=True)
    with open(xml_file_path, 'bw') as f_out:
        f_out.write(handle)


if __name__ == '__main__':
    file_name = 'out_xml_file.xml'
    path = Path('out_xml') / file_name

    descr = '''\
<p>Microsoft Windows 12 учебная, 48-битная,<br>
☝☝☝☝☝☝☝☝☝☝<br>
<strong>OEM веб-версия без упаковки,</strong><br></p>
<ul>
<li>✅ Продажа от <strong>1 шт</strong>!</li>
<li>✅ Оплата <strong>при получении</strong> (наложенный платеж)!</li>
<li>✅ Доставка <strong>DPD</strong>, <strong>СДЭК</strong>,&nbsp;<strong>Почтой России</strong> или любой ТК - оплата товара при получении.</li>
<li>✅ <strong>Мы производитель</strong> - изготовим нестандартный размер <strong>на любой прибор</strong> (бытовой, торговый, промышленный)!</li>
<li>✅ <strong>Гарантия </strong>на все изделия (обмен или возврат без чека).</li>
</ul>
<p>⚡⚡⚡⚡ Wi-Fi в комплекте ⚡⚡⚡⚡,<br>
исходники прилагаются,<br>
часть исходников на паскале (EAP)</p>\
'''

    ad_dicts = [
        {
            'Id': '2020-03-001',
            'DateBegin': '2020-03-01T05:00:00+03:00',
            'ListingFee': 'Package',
            'AdStatus': 'Free',
            'ManagerName': 'Bill Gates',
            'ContactPhone': '8 800 200 80 01',
            'Address': 'Redmond, Washington, U.S.',
            'Category': 'Игры, приставки и программы',
            'GoodsType': 'Компьютерные игры',
            'AdType': 'Товар от производителя',
            'Title': 'Microsoft Windows 12 edu x48-bit with source code',
            'Description': descr,
            'Price': '880',
            'Condition': 'Новое',
            'Images': [
                'https://www.microsoft.com/картинки/виндовс-1.bmp',
                'https://www.microsoft.com/картинки/виндовс-2.bmp',
            ],
        },
        {
            'Id': '2020-03-002',
            'DateBegin': '2020-03-01T05:00:00+03:00',
            'ListingFee': 'Package',
            'AdStatus': 'Free',
            'ManagerName': 'Bill Gates',
            'ContactPhone': '8 800 200 80 01',
            'Address': 'Redmond, Washington, U.S.',
            'Category': 'Игры, приставки и программы',
            'GoodsType': 'Компьютерные игры',
            'AdType': 'Товар от производителя',
            'Title': 'Microsoft Windows 12 edu x48-bit with source code',
            'Description': descr,
            'Price': '440',
            'Condition': 'Б/у',
            'Images': [
                'https://www.microsoft.com/картинки/виндовс-1.bmp',
                'https://www.microsoft.com/картинки/виндовс-2.bmp',
            ],
        },
    ]

    save_root_xml(path, ad_dicts)
