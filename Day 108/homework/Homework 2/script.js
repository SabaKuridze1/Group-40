// შექმენით 10 ელემენტიანი სია, ჩაამატეთ მომხმარებლის შემოტანილი სიტყვა. დააკონსოლში გამოიტანეთ მთლიანი სია და მე-5 ინდექსზე მყოფი ელემენტისა და მე-8 ინდექსზე მყოფი ელემენტების კონკატენაცია.


let arr = ["a", "b", "g", "d", "e", "v", "z", "t", "i", "k"]


let userStr = prompt("Enter a word: ")


arr.push(userStr)

console.log(arr)

console.log(arr[5] + arr[8])