#  3) შექმენით სია რომელშიც მოათავსებთ 1-დან 20მდე რიცხვებს შემდეგ კი ამ სიიდან დაბეჭდავთ მხოლოდ ლუწ რიცხვებს გამოიყენეთ for loop
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(len(list)):
    if list[i]%2==0:
        print('it is even')