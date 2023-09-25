const form = document.getElementById('the_form')

const firstValue = document.getElementById('first');
const lastValue = document.getElementById('last');
const emailValue = document.getElementById('email');
const phoneValue = document.getElementById('phone');
const apartmentValue = document.getElementById('apartment');
const websiteValue = document.getElementById('website');
const additionalValue = document.getElementById('additional');

function sendUserData(e) {
    e.preventDefault()
    // submitted_form_data json object with the current values

    try {
        let submitted_form_data = {
            first: firstValue.value.toUpperCase(),
            last: lastValue.value.toUpperCase(),
            email: emailValue.value.toUpperCase(),
            phone: phoneValue.value,
            apartment: apartmentValue.value,
            website: websiteValue.value,
            region: document.querySelector('input[name="region"]:checked').value, // Check if regionValue exists
            description: document.querySelector('input[name="description"]:checked').value, // Check if descriptionValue exists
            how:  getCheckedCheckboxes('how'),
            additional: additionalValue.value,
        }
        if (checkFormInput(submitted_form_data) === true) {
            console.log(submitted_form_data);
            // toPythonAPI(submitted_form_data);
        } else {
            console.log('Form data is empty or invalid.');
            console.log(submitted_form_data);
        }

    } catch(error) {
        alert('Required areas cannot be empty')
        console.error(error)
    }
    

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

//checking information validity
function checkFormInput(submitted_form_data) {
    const keys = Object.keys(submitted_form_data)
    let isEmpty = false
    for(let i = 0; i < keys.length-1 && isEmpty === false; i++) {
        const key = keys[i]
        if(submitted_form_data[key] === '') {
            isEmpty = true
        }
    }
    if(isEmpty === true) {
    alert('One or more required fields may be empty')
    return isEmpty = false
    } else {
        console.log('All required fields are filled')
        return isEmpty = true
    }
}

form.addEventListener('submit', sendUserData) 