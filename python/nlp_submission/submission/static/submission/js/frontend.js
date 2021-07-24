function validateForm() {
    let sentence = document.forms["nlpForm"]["sent"].value;
    if (sentence ===  ""){
        alert("Please enter a sentence");
        return false
    }
}