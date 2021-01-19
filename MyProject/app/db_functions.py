def check_item_is_exist(item_name, table_name):
    return table_name.objects.filter(name=item_name).exists()

def insert_item_to_table(item_name, item_price, item_img_url, table_name, history_table_name):
    new_item = table_name(name=item_name, current_price=item_price,image_url=item_img_url)
    new_item.save()

    new_item_history = history_table_name(phone_id=new_item, price=item_price)
    new_item_history.save()

def update_item_price(item_name, item_price, table_name, history_table_name):
    item = table_name.objects.get(name=item_name)
    if item_price != item.current_price:
        item.current_price = item_price
        item.save()
        item_history = history_table_name(phone_id=item, price=item_price)
        item_history.save()
