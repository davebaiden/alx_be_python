weather = input("What's the weather like today? (sunny/rainy/cold)): ").strip().lower()
if weather == "sunny":
    recommend = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    recommend = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    recommend = "Make sure to wear a warm coat and a scarf."
else:
    recommend = "Sorry, I don't have recommendation for this weather."
print(recommend)