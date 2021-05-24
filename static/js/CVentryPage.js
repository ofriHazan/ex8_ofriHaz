let text = "Hi everyone, My name is Ofri Hazan, Welcome to me CV webpage :)";
let i = 0;
let speed=50;

function loadEntryPage(){
    if(i<text.length){
        document.getElementById("Hi").innerHTML+=text.charAt(i);
        i++;
        setTimeout(loadEntryPage,speed);
    }
}
console.log(text);