// გააკეთეთ კალკულატორი. მომხმარებელს შემოატანინეთ ოპერაციაც და 2 რიცხვიც. შემდეგ შეასრულეთ შესაბამისი მოქმედება და გამოიტანეთ კონსოლში.


let num1 = Number(prompt("Enter the First number: "))
let num2 = Number(prompt("Enter the Second number: "))
let op = prompt("Enter Operator: ")

if(op == "+"){
    console.log(num1 + num2)
}else if(op == "-"){
    console.log(num1 - num2)
}else if(op == "*"){
    console.log(num1 * num2)
}else if(op == "/"){
    console.log(num1 / num2)
}

