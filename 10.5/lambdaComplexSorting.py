zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "cathegory" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "cathegory" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "cathegory" : (4, "Sluchátka")
    }
]


print(sorted(zbozi,key=lambda zbozi:zbozi["price"]))
print("================================================")
print(sorted(zbozi,key=lambda zbozi:zbozi["name"],reverse=True))
print("================================================")
print(sorted(zbozi,key=lambda zbozi:zbozi["cathegory"][0]))
print("================================================")