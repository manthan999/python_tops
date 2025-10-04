products = {
    "Laptop" :{
        "price":30000,
        "qty":10
    },
     "Mouse" :{
        "price":300,
        "qty":15
    },
     "Keyboard" :{
        "price":3000,
        "qty":11
    },
    "Monitor" :{
        "price":30000,
        "qty" :23
    },
    "Cpu" :{
        "price" :300000,
        "qty" :12
    },
    "phone" :{
        "price" :3000,
        "qty" :22
    },

}

for i,j in products.items():
    print(i)
    for x,y in j.items():
        print(x,y)