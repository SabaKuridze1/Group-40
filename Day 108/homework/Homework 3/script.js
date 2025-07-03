// მომხმარებელს შემოატანინეთ ასაკი. თუ 5-ზე ნაკლები შემოიტანა გამოიტანეთ კონსოლში 'ბაღის მოსწავლე ხარ'. 6-დან 18-მდე თუ შემოიტანა გამოიტანეთ 'სკოლის მოსწავლე ხარ'. 18-დან 19-მდე       -      '  აბიტურიენტი'; 20-დან 25-მდე სტუდენტი. დანარჩენ სხვა შემთხვევაში შეეკითხეთ თუ მუშაობს პროგრამისტად. თუ შემოიტანა მომხმარებელმა 'კი' მაშინ გამოიტანეთ 'შენ ნამდვილი ჩადი ხარ'. სხვა შემთხვევაში 'კარგია'

let age = Number(prompt("ramdeni wlis xar?: "))

let programisti = 0
if(age <= 5){
    console.log("shen bagis moswavle xar")
}else if(age >= 6 && age <= 18){
    console.log("shen skolis moswavle xar")
}else if(age >= 18 && age <= 19){
    console.log("shen abiturienti xar")
}else if(age >= 20 && age <= 25){
    console.log("shen studenti xar")
}
else{
    programisti = prompt("pragramisti xar??")
}if(programisti == "ki"){
    console.log("namdvili chad xar")
}else{
    console.log("kargia")
}