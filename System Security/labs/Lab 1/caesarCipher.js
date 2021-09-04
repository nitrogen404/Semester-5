const userInput = prompt("Enter the message: ");
// const shift = prompt("enter the number of Shift: ");

const Caesarcipher = function encrypt(text, shift) {
    let encryptedText = "";
    for (let i = 0; i < text.length; i++) {

        let asciiCode = text[i].charCodeAt();
        
        if (asciiCode >= 97 && asciiCode < 123) {
            asciiCode += shift % 26;
            if (asciiCode > 122) {
                asciiCode = (asciiCode - 122) + 96;
            }
            else if (asciiCode < 97) {
                asciiCode = (asciiCode - 97) + 123;
            }
        }
        if (asciiCode > 64 && asciiCode < 91) {
            asciiCode += shift % 26;
            if (asciiCode > 90) {
                asciiCode = (asciiCode - 90) + 64;
            }
            else if (asciiCode < 65) {
                asciiCode = (asciiCode - 65) + 91;

            }
        }
        encryptedText += String.fromCharCode(asciiCode);
    }
    
    return encryptedText;
}

// console.log(Caesarcipher(userInput, shift));



// console.log(mono(userInput));