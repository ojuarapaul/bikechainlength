// chain length calculator

function main() {
    let chainstay = document.getElementById("chainStaySize").value;
    if (chainstay == "") {
        main();
    } else {
        chainstay = chainstay * 1;
    }
    let largercog = document.getElementById("cog").value;
    if (largercog == "") {
        main();
    } else {
    largercog = largercog * 1;
    }
    let chainring = document.getElementById("chainring").value;
    if (chainring == "") {
        main();
    } else {
    chainring = chainring * 1;
    }
    a = (chainstay * 2)
    b = (largercog / 4)
    c = (chainring / 4)
    let chainLength = a + (b + c + 4)
    chainLength = Math.floor(chainLength);
    const linksNumber = chainLength * 2
    alert("The chain size should be " + chainLength + " inches, which corresponds to " + linksNumber + " links.")
    
    alert("If you use a Missing Link it should be included in the chain's size!")
}

