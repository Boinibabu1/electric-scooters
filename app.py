from flask import Flask, render_template

app = Flask(__name__)

scooters = [
    {
        "name": "Volt X1",
        "price": "₹49,999",
        "range": "45 km",
        "speed": "45 km/h",
        "battery": "36V 15Ah",
        "image": "scooter1.jpg"
    },
    {
        "name": "Urban E2",
        "price": "₹59,999",
        "range": "55 km",
        "speed": "50 km/h",
        "battery": "48V 18Ah",
        "image": "scooter2.jpg"
    },
    {
        "name": "Thunder S",
        "price": "₹69,999",
        "range": "65 km",
        "speed": "55 km/h",
        "battery": "48V 20Ah",
        "image": "scooter3.jpg"
    }
]


@app.route("/")
def home():
    return render_template("index.html", scooters=scooters)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
