// 2) მომხმარებელს შემოატანინეთ ქულა თუ ქულა იქნება 90-დან 100ის ჩათვლით დაბეჭდეთ რომ ძალიან კარგი შედეგი, თუ ქულა იქნება 70-დან 90ის ჩათვლით დაწერეთ რომ კარგია მაგრამ გაუმჯობესება შეიძლება, თუ ქულა იქნება 50-დან 70ის ჩათვლით დაბეჭდეთ რომ ცუდია და აუცილებლად უნდა გამოასწოროს, ხოლო სხვაშემთხვევაში წასულია იმის საქმე



const score = Number(prompt("Enter your score: "))


if(score >= 90 && score <= 100){
    alert("sagol")
}else if(score >= 70 && score <= 90){
    alert("kaia mara meti shegilia")
}else if(score >= 50 && score <= 70){
    alert("kargi shedegi araa, aucileblad gamoaswore")
}else{
    alert("ooooo, shen shemtxvevit niko chochias xom ar icnob??")
}

