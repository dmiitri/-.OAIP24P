import json
products = [
    {
        "category": "Ноутбук",
        "name": " Lenovo IdeaPad 3",
        "price": 37999,
        "photo": "https://avatars.mds.yandex.net/get-marketpic/8791044/pic0023b3a6ee4ab9ac0547751e6290bda6/orig",
        "description": "Ноутбук Lenovo IdeaPad 3 15IAU7 представлен в сером пластиковом корпусе весом 1.63 кг. Аппаратная платформа с 6-ядерным процессором Intel Core i3-1215U и 8 ГБ оперативной памяти обеспечивает быстродействие при работе в программах, интернет-серфинге, запуске мультимедиа. Для хранения файлов предлагается твердотельный накопитель емкостью 256 ГБ."
    },
    {
        "category": "Смартфон",
        "name": "Apple iPhone 17 Pro",
        "price": 131999,
        "photo": "https://c.dns-shop.ru/thumb/st1/fit/0/0/25d8e5049f089e018d4d966dca7515df/3f07b1ffa9193a775d83d5a74fa818307037b9e0cf34e51a18ac31304fceefb9.jpg.webp",
        "description": "Представляем iPhone 17 Pro, разработанные чтобы стать самыми мощными моделями iPhone. В основе конструкции лежит цельнолитой алюминиевый корпус, обеспечивающий максимальную производительность, ёмкость аккумулятора и долговечность."
    },
    {
          "category": "Наушники",
        "name": "Sony WH-CH520",
        "price": 4599,
        "photo": "https://c.dns-shop.ru/thumb/st1/fit/wm/0/0/dcd6b47ff4af1f9bed6d16b440ca7694/c3c4822b572e7b00ef68af2e3d95cc96c52d4df588605861d6016ca5bc64131c.jpg.webp",
        "description": "Наслаждайтесь высоким качеством звука в течение всего дня. Наушники WH-CH520 с аккумулятором, обеспечивающим до 50 часов работы, стабильным подключением и улучшенными характеристиками при звонках, удовлетворят ваши потребности."
    },
]
with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=4)
with open("products.json", "r", encoding="utf-8") as file:
    data = json.load(file)
print (data)