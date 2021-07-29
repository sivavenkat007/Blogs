
console.log("ss")
function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(username === '' && password === ''){
        alert('You must enter both')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/',{
        method : 'POST',
        headers : {
            'Content-Type': 'application/json',
            'charset': 'utf-8',
            'X-CSRFToken' : csrf,
        },
        body : JSON.stringify(data)
    }).then (result => result.json())
    .then(response => {
        console.log(response)
        })

}