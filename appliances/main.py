from datetime import datetime, timedelta
from pathlib import Path

from pytils.translit import slugify

from appliances.data import (COMPANY_NAME, MANAGER_NAME, CONTACT_PHONE,
                             ADDRESS, CATEGORY, GOODS_TYPE, AD_TYPE,
                             get_description, CONDITION, PHOTO_STORAGE,
                             START_TIME)
from appliances.root_xml import save_root_xml
from utils import (get_list_of_dicts_from_csv_file, get_datetime,
                   get_repr_world_time)


def main():
    ad_dict_list = []

    products = get_list_of_dicts_from_csv_file('Товары.csv')
    current_date = get_datetime(START_TIME)

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
                'DateBegin': get_repr_world_time(current_date),
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

        current_date += timedelta(minutes=45)
        if current_date.hour >= 20 and current_date.minute > 0:
            day = current_date.day + 1
            current_date = current_date.replace(day=day, hour=8, minute=0)

    now = datetime.now().strftime('%d-%m-%Y')
    file_name = ''.join([slugify(COMPANY_NAME), '.', now, '.xml'])
    file_path = Path('out_xml') / file_name
    save_root_xml(file_path, ad_dict_list)


if __name__ == '__main__':
    main()
