document.getElementById('signup').addEventListener('submit', signup);
function signup(e) {
  e.preventDefault();
  const firstname = document.getElementById('firstname').value;
  const lastname = document.getElementById('lastname').value;
  const othernames = document.getElementById('othernames').value;
  const phonenumber = document.getElementById('phonenumber').value;
  const email = document.getElementById('email').value;
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  fetch('https://floating-reaches-50695.herokuapp.com/api/v2/auth/signup', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-type': 'application/json',
      mode: 'cors',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Request-Method': '*',
    },
    body: JSON.stringify(
      {
        firstname,
        lastname,
        othernames,
        phonenumber,
        email,
        username,
        password,
      }
),
  })
    .then(response => response.json())
    .then((data) => {
      if (data.status === 201) {
        console.log(data);
        console.log(data.data[0].token);
        window.location.replace('index.html');
      }else {
        console.log(data);
        document.getElementById('alert').style.color = 'red';
        document.getElementById('alert').innerHTML = data.message;
      }
    });
}
