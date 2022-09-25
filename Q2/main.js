let stringCont = document.getElementById("str-var");
let intCont = document.getElementById("int-var");
let sumFuncAns = document.getElementById("sum-func-answer");
let if_elseAns = document.getElementById("if-else-header-answer");


let stringVar = "Hemansi";
stringCont.innerHTML = stringVar;
let integerVar = 20;
intCont.innerHTML = integerVar;

let sumFunc = (num1, num2) => {
  return num1 + num2;
};


sumFuncAns.innerHTML = sumFunc(11, 9);


let age = 20;
if (age >= 19) {
  if_elseAns.innerHTML = "Yes";
} else {
  if_elseAns.innerHTML = "No";
}


for (let x = 1; x < 11; x++) {
  document.write(x * 15 + "<br>");
}