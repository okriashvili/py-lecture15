# oop and class part 2
from abc import abstractmethod
from traceback import print_tb

print("oop and class part II Inheritance")
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    get_full_name = lambda self: f"{self.name} {self.age}"
    # def get_full_name (self):
    #     return f"{self.name} {self.age}"

student1 = Student("John", 22)
print(student1.get_full_name())


class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate (self, speed):
        self.speed += speed
        return f"{self.speed}"

    def slow_down (self, speed):
        self.speed -= speed
        return f"{self.speed}"

    def stop (self):
        self.speed = 0
        return self.speed

car1 = vehicle("BMW", "M5", 2019)

print(car1.accelerate(10))
print(car1.accelerate(20))
print(car1.slow_down(25))
print(car1.stop())

# შვილობილი კლასის შესამქნებად, ვქმნით ცალკეულ კლასს სადაც ფრჩხილებში ვუწერთ მშობელი კლასის დასახელებას
# ამ კლასს, ექნება მშობელი კლასის თვისებებიც
class BMW(vehicle):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def race(self, max_speed):
        max_speed = 240
        return max_speed

bmf_f30 = BMW("BMW", "f30", 2016)
print(f"f30's max-speed is {bmf_f30.accelerate(260)}")
print(f"f30 can race with max speed {bmf_f30.race(100)}")

# accelerate მეთოდი შევქმენით vehicle კლასში, მაგრამ მის შვილობის კლასსაც შეუძლია გამოიყენოს მშობლის თვისებები და მეთოდები


# შვილიშვილ კლასს შეუძლია გამოიყენოს როგორც მშობლის ისე მისი წინამორბედის მეთოდები
# კლასის შესამქნელად კლასის ფრჩხილებში ვუწერთ მშბელი კლასის სახელს, ეერთით წინამორბედი კლასის სახელს
class BMW_drift(BMW):
# არაა აუცილებელი __init__ კონსტრუქტორის შექმნა, შვილობილ კლასს, ავტომატურად ესეტება მშობელი init კონსტრუქტორის ატრობუტები


#super საკვანძო სიტყვა - როგორც ავღიშნეთ, არაა აუცილებელი კომსტრუქტორების დაწერა კასებში,
# მაგრამ იმ შემთხვევაში თუკი გვსურს რომ დავამატოთ კლასში ატრიბუტები შეგვიძლია გამოვიყენოთ super საკვანძო სიტყვას
    def __init__(self, brand, model, year, fee):
    # ვუქმნით ინიტ კონსტრუქტორს, და ცალცალკე რომ არ გავუწეროთ self.atrubute = atribute
    # super საკვანძო სიტყვაში ვუწერთ ატრიბუტებს შიგნიღ=თ, მაგრამ თუკი ატრობუტს ვამატებთ, ეს ხდება არა superის შიგნით
    # არამედ slef.atribute = atribute-მეთოდით
        super().__init__(brand, model, year)
        self.fee = fee
    # super საკვანძო სიტყვით ხდება მშობლის ელემენტების და მეთოდებისნ წამოღება

    def drift(self):
        return f"{self.brand} {self.model} can drift"


M = BMW_drift("BMW", "M5", 2019, "60,000$")
print(f"m5 can race with max speed {M.race(100)}")
print(M.drift())
print(M.slow_down(25))
print(M.fee)

# შეგვილია ერთი კალსი გავხადოპთ ორი კლასის შვილობილი, ამისათვის ცლასის შექმნისას, ფრჩხილებშ გადავცეთ ის ორი კლასის რომლის შვილობლიც გვინდა რომ გავხადოთ /
# მშობელი კლასები უნდა გამოვყოთ მძიმით














# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# პოლიმორფიზმი / polymorphizm - მრავალფეროვნება, მეთოდების გადატვირთვა
class shapes:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def cal_area(self):
        return self.width * self.height

class triangle(shapes):

# პოლიმორფიზმი გვაძლევს საშუალებას რომ მშობლის მეთოდები შევცვალოთ და მოვარგოთ შვილობილ კლასებს
#     def cal_area(self):
#         return f"triangle area is {self.width * self.height * 2}"
# cal_area მეთოდი შევცვალეთ და მოვარგეთ tringle კლასს / ფორმულა შევცვალეთ

# მეთოდების მოკლედ ჩასაწერად შეგვიძლია გამოვიძახოთ super() საკვანძო სიტყვა .მშობლის მეთოდის დასახელება
    def cal_area2(self):
        return f"triangle area is {super().cal_area()}"


class square(shapes):

    def __init__(self, side):
        self.side = side

    def cal_area3(self):
        return f"square area is {self.side * self.side}"


triangle1 = triangle(10, 5)
square1 = square(10)

print(triangle1.cal_area())
print(triangle1.cal_area2())
print(square1.cal_area3())
# პოლიმორფიზმი განიხილავს, მრავალფეროვნებას, კლასებში მეთოდების გადატვირთვას და შემდგომ შვილობილ კალსებზე მორგებას / მაგრამ ჩვენი ნებაა გადავტვირთავთ მას თუ არა





# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# abstraction - პოლიმორფიზმის მსგავსი რამააა აბსტრაქციზმიც, შესაძლებლობას გვაძლევს რომ გადავტვირთოთ შვილობილ კლასებში მეთოდები
# მაგრამ განსხვავებით პოლიმორფიზმისა, აბსტრაქციზმის შემმთხვევაში აუცილებლად უნდა გადავტტვირთოთ მშობეილი კლასის მეთოდი

# პირველ რიგში ვაიმპორტებთ abstractmethodს
from abc import ABC, abstractmethod
# შემდგომ იმ მშობელ კლასს, რომლიც კლასებიც გადატვირთვაც გვინდა მოვახდინოთ ფრჩხილებში ვუწერთ ABC საკვანძო სიტყვას, ABC-ს შვილობლის ვხდით
class shape(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height
# აბსტრაქციზმის სიტანქი არის შემდეგი: იმ მეთოდებს რომლის გადატვირთვაც აუცილებლად უნდა მოხდეს, თავზე უნდა დავაწეროთ @abstractmethod
# მოკლედ, მშობელი კლასის მეთოდი აუცილებლად უნდა იყოს გადაწერილი შვილობილ კლასში

    @abstractmethod
    def cal_perimeter(self):
        return f"perimeter is{(self.width + self.height) * 2}"

class rectangles(shape):
# აბსტრაქტ მეთოდის გამოიყენება იმისათვის რომ სტრუქტურა იყოს დაცული, მაგალითად შესაძლოა გვქონდეს კლასი რომელშიც დაგვავიწყდა მეთოდის გადატვრიტა
# ამიტომ გამოიყენება აბსტრაქტნეთოდი, რომელიც არ მოგვცემს იმის საშუალებას რომ მეთოდი აუცილებლად გადავუტვრთოთ / წინააღმდეგ შემთვევაში გავა ერორზე
    def cal_perimeter(self):
        return f"rectangle perimeter is {(self.width + self.height) * 0.5}"


    def get_square(self):
        return f"rectangles square area is {self.width * self.height}"

triangle = rectangles(10, 10)
print(triangle.cal_perimeter())
print(triangle.get_square())





# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# str კონსტრუქტორი
class Students:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def get_full_name(self):
        return f"{self.name} {self.lastname}"

    def __str__(self):
        return f"{self.name} {self.lastname}"



student1 = Students("makho", "okriashvili", 22)

# ინსტანსის დაპრინტვისას, გვიპრინტავს ობიექტის მისამართს
print(student1)
# ამაგრამ თუკი გვინდა რომ ინსტანსის დაპრინტვისას, გამოიტანოს არა ობიექტის მისამართი არამედ მაგ:სახელი და გვარი ვიყენებთ __str__ კონსტრუქტორს
# რომელსაც ვაბრუნებინებთ იმას რასაც გავუწერთ
# __Str__ კონსტრუწტორი ავტომატურად ამოქმედდება მაშინ როდესაც გამოვიძახებთ კლასის ინსტანსებს
print(student1.get_full_name())


