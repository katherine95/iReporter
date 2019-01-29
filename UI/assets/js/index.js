document.getElementById('login').addEventListener('submit', login);
function login(e) {
  e.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  fetch('https://floating-reaches-50695.herokuapp.com/api/v2/auth/login', {
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
        username,
        password,
      },
    ),
  })
    .then(response => response.json())
    .then((data) => {
      if (data.status === 200) {
        localStorage.setItem('user_id', data.data[0].user.user_id);
        localStorage.setItem('token', data.data[0].token);
        localStorage.setItem('role', data.data[0].user.isAdmin);
        localStorage.setItem('username', data.data[0].user.username);
        if (data.data[0].user.isAdmin === false) {
          window.location.replace('user-account.html');
        } else {
          window.location.replace('admin.html');
        }
      } else {
        document.getElementById('alert').style.color = 'red';
        document.getElementById('alert').innerHTML = data.message;
      }
    });
}
