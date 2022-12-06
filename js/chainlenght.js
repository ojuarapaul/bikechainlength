// calculador de tamanho de corrente

function main() {
    var chainstay = prompt('digite o tamanho do chainstain em polegadas, formato decimal - ex: 16.0, 17.5, 18.25 etc: ');
    var largercog = prompt('digite o numero de dentes da maior catraca - ex: 42: ');
    var chainring = prompt('digite o numero de dentes da sua maior - ou única - coroa - ex:30: ');
    a = (chainstay * 2)
    b = (largercog / 4)
    c = (chainring / 4)
    var chainLength = a + b + c + 4
    chainLength = Math.floor(chainLength);
alert('O tamanho da corrente é ' + chainLength + ' polegadas')
var linksNumber = chainLength * 2
alert ("That corresponds to " + linksNumber + " links")
alert("If you use a Missing Link it should be included in chain's size")
}
main()
