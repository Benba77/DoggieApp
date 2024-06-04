
console.log(`Ich bin in JS: ${baseUrl}`)


var buttonKöpek = document.getElementById('buttonKöpek')
var imgKöpek = document.getElementById('imgKöpek')
var pKöpek = document.getElementById('pKöpek')



function strTitle(breed) {
    let breedNew = ''
    for (var i=0; i<breed.length; i++) {
        if (i==0 || (i>0 && breed[i-1]=='-')) {
            breedNew = breedNew + breed[i].toUpperCase()
        } else {
            breedNew = breedNew + breed[i]
        }
    }
    console.log(breedNew)
    return breedNew
}

buttonKöpek.addEventListener('click', async function() {
    
    response = await fetch('https://dog.ceo/api/breeds/image/random')
    json = await response.json()
    console.log(json)

    imgUrl = json['message']
    console.log(imgUrl)
    imgKöpek.src = imgUrl
    breed =  imgUrl.split('/')[4]
    pKöpek.innerText = 'Rasse: ' + strTitle(breed)


    fetch(baseUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'breed': strTitle(breed) , 'url':imgUrl})
    })
})

