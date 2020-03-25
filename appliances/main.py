from datetime import datetime
from pathlib import Path

from pytils.translit import slugify

from appliances.data import (COMPANY_NAME, MANAGER_NAME, CONTACT_PHONE,
                             ADDRESS, CATEGORY, GOODS_TYPE, AD_TYPE,
                             get_description, CONDITION, PHOTO_STORAGE)
from appliances.root_xml import save_root_xml
from utils import get_list_of_dicts_from_csv_file


def main():
    ad_dict_list = []

    products = get_list_of_dicts_from_csv_file('Товары.csv')
    for products in products:
        if len(products['Заголовок']) < 20:
            title = f'Уплотнитель двери холодильника {products["Заголовок"]}'
        elif len(products['Заголовок']) < 26:
            title = f'Уплотнитель холодильника {products["Заголовок"]}'
        else:
            title = f'Уплотнитель для {products["Заголовок"]}'

        images = [''.join([PHOTO_STORAGE, x])
                  for x in products['Ссылки на картинки'].split(', ')]

        ad_dict_list.append(
            {
                'Id': f'{datetime.now().strftime("%Y-%m")}-{slugify(title)}',
                'DateBegin': '2020-03-01T05:00:00+03:00',  # TODO: generate
                'ListingFee': 'Package',
                'AdStatus': 'Free',
                'ManagerName': MANAGER_NAME,
                'ContactPhone': CONTACT_PHONE,
                'Address': ADDRESS,
                'Category': CATEGORY,
                'GoodsType': GOODS_TYPE,
                'AdType': AD_TYPE,
                'Title': title,
                'Description': get_description(products['Заголовок']),
                'Price': products['Цена'],
                'Condition': CONDITION,
                'Images': images,
            }
        )

    now = datetime.now().strftime('%d-%m-%Y')
    file_name = ''.join([slugify(COMPANY_NAME), '.', now, '.xml'])
    file_path = Path('out_xml') / file_name
    save_root_xml(file_path, ad_dict_list)


if __name__ == '__main__':
    main()
