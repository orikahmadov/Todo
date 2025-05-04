from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid 




app = Flask(__name__) 
# Enable CORS for all routes it will allow all origins to access the API
# In production, you should restrict origins to your frontend's domain
CORS(app, resources={r"/*": {"origins": "*"}})

products = [
    # Laptops
    {"id": 1, "name": "HP Laptop", "category": "laptop", "origin": "USA", "price": 1000, "description": "HP Laptop with 16GB RAM and 512GB SSD"},
    {"id": 2, "name": "Dell Inspiron", "category": "laptop", "origin": "USA", "price": 950, "description": "Dell Inspiron with 8GB RAM and 256GB SSD"},
    {"id": 3, "name": "Lenovo ThinkPad", "category": "laptop", "origin": "China", "price": 1100, "description": "Lenovo ThinkPad with 16GB RAM and 1TB SSD"},
    {"id": 4, "name": "Apple MacBook Air", "category": "laptop", "origin": "USA", "price": 1200, "description": "Apple MacBook Air M1 with 8GB RAM and 256GB SSD"},
    {"id": 5, "name": "Acer Aspire", "category": "laptop", "origin": "Taiwan", "price": 800, "description": "Acer Aspire with 8GB RAM and 512GB SSD"},
    {"id": 6, "name": "Asus ZenBook", "category": "laptop", "origin": "Taiwan", "price": 1050, "description": "Asus ZenBook with 16GB RAM and 512GB SSD"},
    {"id": 7, "name": "MSI Modern", "category": "laptop", "origin": "Taiwan", "price": 1150, "description": "MSI Modern with 16GB RAM and 1TB SSD"},
    {"id": 8, "name": "Samsung Galaxy Book", "category": "laptop", "origin": "South Korea", "price": 980, "description": "Samsung Galaxy Book with 8GB RAM and 512GB SSD"},
    {"id": 9, "name": "Microsoft Surface Laptop", "category": "laptop", "origin": "USA", "price": 1300, "description": "Microsoft Surface Laptop with 16GB RAM and 512GB SSD"},
    {"id": 10, "name": "Razer Blade Stealth", "category": "laptop", "origin": "USA", "price": 1500, "description": "Razer Blade Stealth with 16GB RAM and 512GB SSD"},
    {"id": 11, "name": "LG Gram", "category": "laptop", "origin": "South Korea", "price": 1250, "description": "LG Gram with 16GB RAM and 1TB SSD"},
    {"id": 12, "name": "Huawei MateBook", "category": "laptop", "origin": "China", "price": 900, "description": "Huawei MateBook with 8GB RAM and 512GB SSD"},
    {"id": 13, "name": "Toshiba Dynabook", "category": "laptop", "origin": "Japan", "price": 850, "description": "Toshiba Dynabook with 8GB RAM and 256GB SSD"},
    {"id": 14, "name": "Google Pixelbook", "category": "laptop", "origin": "USA", "price": 1000, "description": "Google Pixelbook with 8GB RAM and 128GB SSD"},
    {"id": 15, "name": "Alienware m15", "category": "laptop", "origin": "USA", "price": 1800, "description": "Alienware m15 with 32GB RAM and 1TB SSD"},
    {"id": 16, "name": "Gigabyte Aero", "category": "laptop", "origin": "Taiwan", "price": 1400, "description": "Gigabyte Aero with 16GB RAM and 1TB SSD"},
    {"id": 17, "name": "Fujitsu Lifebook", "category": "laptop", "origin": "Japan", "price": 950, "description": "Fujitsu Lifebook with 8GB RAM and 512GB SSD"},
    {"id": 18, "name": "Chuwi HeroBook", "category": "laptop", "origin": "China", "price": 400, "description": "Chuwi HeroBook with 4GB RAM and 128GB SSD"},
    {"id": 19, "name": "Vaio SX14", "category": "laptop", "origin": "Japan", "price": 1350, "description": "Vaio SX14 with 16GB RAM and 512GB SSD"},
    {"id": 20, "name": "Xiaomi Mi Notebook", "category": "laptop", "origin": "China", "price": 850, "description": "Xiaomi Mi Notebook with 8GB RAM and 512GB SSD"},
    {"id": 21, "name": "Panasonic Let's Note", "category": "laptop", "origin": "Japan", "price": 1400, "description": "Panasonic Let's Note with 16GB RAM and 512GB SSD"},
    {"id": 22, "name": "Sharp Dynabook", "category": "laptop", "origin": "Japan", "price": 900, "description": "Sharp Dynabook with 8GB RAM and 256GB SSD"},
    {"id": 23, "name": "NEC Lavie", "category": "laptop", "origin": "Japan", "price": 1100, "description": "NEC Lavie with 16GB RAM and 512GB SSD"},
    {"id": 24, "name": "Honor MagicBook", "category": "laptop", "origin": "China", "price": 750, "description": "Honor MagicBook with 8GB RAM and 512GB SSD"},
    {"id": 25, "name": "Realme Book", "category": "laptop", "origin": "China", "price": 700, "description": "Realme Book with 8GB RAM and 256GB SSD"},
    {"id": 26, "name": "Dynabook Satellite Pro", "category": "laptop", "origin": "Japan", "price": 950, "description": "Dynabook Satellite Pro with 8GB RAM and 512GB SSD"},
    {"id": 27, "name": "Avita Liber", "category": "laptop", "origin": "Hong Kong", "price": 600, "description": "Avita Liber with 8GB RAM and 256GB SSD"},
    {"id": 28, "name": "Eurocom Sky X4C", "category": "laptop", "origin": "Canada", "price": 2000, "description": "Eurocom Sky X4C with 32GB RAM and 2TB SSD"},
    {"id": 29, "name": "Clevo N141ZU", "category": "laptop", "origin": "Taiwan", "price": 850, "description": "Clevo N141ZU with 8GB RAM and 512GB SSD"},
    {"id": 30, "name": "System76 Lemur Pro", "category": "laptop", "origin": "USA", "price": 1200, "description": "System76 Lemur Pro with 16GB RAM and 512GB SSD"},
    {"id": 31, "name": "Purism Librem 14", "category": "laptop", "origin": "USA", "price": 1600, "description": "Purism Librem 14 with 16GB RAM and 1TB SSD"},
    {"id": 32, "name": "TUXEDO Pulse 15", "category": "laptop", "origin": "Germany", "price": 1300, "description": "TUXEDO Pulse 15 with 16GB RAM and 1TB SSD"},
    {"id": 33, "name": "Medion Akoya", "category": "laptop", "origin": "Germany", "price": 700, "description": "Medion Akoya with 8GB RAM and 256GB SSD"},
    {"id": 34, "name": "Schneider SCL141CTP", "category": "laptop", "origin": "Germany", "price": 400, "description": "Schneider SCL141CTP with 4GB RAM and 128GB SSD"},
    {"id": 35, "name": "Positivo Motion", "category": "laptop", "origin": "Brazil", "price": 500, "description": "Positivo Motion with 4GB RAM and 128GB SSD"},
    {"id": 36, "name": "Itautec Infoway", "category": "laptop", "origin": "Brazil", "price": 600, "description": "Itautec Infoway with 8GB RAM and 256GB SSD"},
    {"id": 37, "name": "Samsung Notebook 9", "category": "laptop", "origin": "South Korea", "price": 1100, "description": "Samsung Notebook 9 with 16GB RAM and 512GB SSD"},
    {"id": 38, "name": "Haier Y11C", "category": "laptop", "origin": "China", "price": 350, "description": "Haier Y11C with 4GB RAM and 128GB SSD"},
    {"id": 39, "name": "Jumper EZbook X3", "category": "laptop", "origin": "China", "price": 300, "description": "Jumper EZbook X3 with 6GB RAM and 128GB SSD"},
    {"id": 40, "name": "Teclast F7 Plus", "category": "laptop", "origin": "China", "price": 400, "description": "Teclast F7 Plus with 8GB RAM and 256GB SSD"},
    {"id": 41, "name": "BMAX Y13", "category": "laptop", "origin": "China", "price": 350, "description": "BMAX Y13 with 8GB RAM and 256GB SSD"},
    {"id": 42, "name": "VivoBook S14", "category": "laptop", "origin": "Taiwan", "price": 900, "description": "VivoBook S14 with 8GB RAM and 512GB SSD"},
    {"id": 43, "name": "Prestigio SmartBook", "category": "laptop", "origin": "Cyprus", "price": 320, "description": "Prestigio SmartBook with 4GB RAM and 128GB SSD"},
    {"id": 44, "name": "Chuwi LapBook Pro", "category": "laptop", "origin": "China", "price": 350, "description": "Chuwi LapBook Pro with 8GB RAM and 256GB SSD"},
    {"id": 45, "name": "Microsoft Surface Go", "category": "laptop", "origin": "USA", "price": 650, "description": "Microsoft Surface Go with 8GB RAM and 128GB SSD"},
    # Phones
    {"id": 46, "name": "Apple iPhone 14", "category": "phone", "origin": "USA", "price": 999, "description": "Apple iPhone 14 with 128GB storage"},
    {"id": 47, "name": "Samsung Galaxy S23", "category": "phone", "origin": "South Korea", "price": 899, "description": "Samsung Galaxy S23 with 256GB storage"},
    {"id": 48, "name": "Google Pixel 7", "category": "phone", "origin": "USA", "price": 799, "description": "Google Pixel 7 with 128GB storage"},
    {"id": 49, "name": "OnePlus 11", "category": "phone", "origin": "China", "price": 749, "description": "OnePlus 11 with 256GB storage"},
    {"id": 50, "name": "Xiaomi Mi 13", "category": "phone", "origin": "China", "price": 699, "description": "Xiaomi Mi 13 with 128GB storage"},
    # Cameras
    {"id": 51, "name": "Canon EOS R6", "category": "camera", "origin": "Japan", "price": 2500, "description": "Canon EOS R6 Mirrorless Camera"},
    {"id": 52, "name": "Nikon Z6 II", "category": "camera", "origin": "Japan", "price": 2000, "description": "Nikon Z6 II Mirrorless Camera"},
    {"id": 53, "name": "Sony Alpha a7 IV", "category": "camera", "origin": "Japan", "price": 2500, "description": "Sony Alpha a7 IV Full-Frame Camera"},
    {"id": 54, "name": "Fujifilm X-T4", "category": "camera", "origin": "Japan", "price": 1700, "description": "Fujifilm X-T4 Mirrorless Camera"},
    {"id": 55, "name": "Panasonic Lumix S5", "category": "camera", "origin": "Japan", "price": 1800, "description": "Panasonic Lumix S5 Mirrorless Camera"},
    # Sensors
    {"id": 56, "name": "Bosch BME280", "category": "sensor", "origin": "Germany", "price": 15, "description": "Bosch BME280 Temperature, Humidity, Pressure Sensor"},
    {"id": 57, "name": "Honeywell HIH6130", "category": "sensor", "origin": "USA", "price": 20, "description": "Honeywell HIH6130 Humidity and Temperature Sensor"},
    {"id": 58, "name": "Texas Instruments HDC1080", "category": "sensor", "origin": "USA", "price": 10, "description": "TI HDC1080 Digital Humidity Sensor"},
    {"id": 59, "name": "STMicroelectronics VL53L0X", "category": "sensor", "origin": "Switzerland", "price": 8, "description": "ST VL53L0X Time-of-Flight Distance Sensor"},
    {"id": 60, "name": "AMS AS7262", "category": "sensor", "origin": "Austria", "price": 25, "description": "AMS AS7262 6-Channel Visible Light Sensor"}
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API IS working"}), 200


@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products), 200

    

@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
