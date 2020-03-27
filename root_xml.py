"""Шаблон под разные категории"""

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
