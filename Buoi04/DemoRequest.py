import requests
import json

result = requests.get("https://dummyjson.com/products")
# print(result, result.status_code)
if result.status_code == 200:
    data = result.json()
    my_data = []
    for item in data["products"]:
        my_data.append(
            {
                "id": item["id"],
                "name": item["title"],
                "price": item["price"],
                "category": item["category"],
                "image": item["images"][0]
            }
        )

    with open("products.json", "w", encoding="UTF8") as file:
        json.dump(my_data, file, indent=4)
