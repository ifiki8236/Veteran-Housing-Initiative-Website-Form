const form = document.getElementById('the_form')

function sendUserData(e) {
    e.preventDefault()
    // submitted_form_data json object with the current values
    let submitted_form_data = {
        'landlords': {
            first: document.getElementById('first').value,
            last: document.getElementById('last').value,
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value,
            apartment: document.getElementById('apartment').value,
            website: document.getElementById('website').value,
            region: document.querySelector('input[name="region"]:checked').value,
            description: document.querySelector('input[name="description"]:checked').value,
            how: getCheckedCheckboxes('how'), // Define or replace this function
            // other_how: document.getElementById('other_how').value,
            additional: document.getElementById('additional').value
        }
    }
    toPythonAPI(submitted_form_data)
    console.log(submitted_form_data)
}

// the getCheckedCheckboxes function
function getCheckedCheckboxes(name) {
    const checkboxes = document.querySelectorAll('input[name="' + name + '"]:checked');
    const values = Array.from(checkboxes).map(checkbox => checkbox.value);
    return values;
}
function toPythonAPI(submitted_form_data){
    fetch('http://127.0.0.1:5000',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(submitted_form_data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message)
    })
    .catch(error => {
        console.error('ERROR:', error)
    })
}

form.addEventListener('submit', sendUserData)