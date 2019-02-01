window.onload = function () {
  getUsers();

  function getUsers() {
    const token = localStorage.getItem('token');
    const message = localStorage.getItem('message');
    const username = localStorage.getItem('username');
    document.getElementById('username').innerHTML = username;

    fetch('https://floating-reaches-50695.herokuapp.com/api/v2/auth/signup', {
      headers: {
        Accept: 'application/json',
        'Content-type': 'application/json',
        mode: 'cors',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Request-Method': '*',
        Authorization: 'Bearer ' + token,
      },
    })
      .then(response => response.json())
      .then((data) => {
        console.log(data.data);
        if (data.status === 200) {
          const table = document.getElementById('users');
          const users = data.data;
          users.map((user) => {
            const new_row = table.insertRow();

            const id = new_row.insertCell(0);
            const email = new_row.insertCell(1);
            const firstname = new_row.insertCell(2);
            const lastname = new_row.insertCell(3);
            const othernames = new_row.insertCell(4);
            const phonenumber = new_row.insertCell(5);
            const createdOn = new_row.insertCell(6);
            const username = new_row.insertCell(7);
            const isAdmin = new_row.insertCell(8);
            const viewUser = new_row.insertCell(9);

            id.innerHTML = users.indexOf(user) + 1;
            email.innerHTML = user.email;
            firstname.innerHTML = user.firstname;
            lastname.innerHTML = user.lastname;
            othernames.innerHTML = user.othernames;
            phonenumber.innerHTML = user.phonenumber;
            createdOn.innerHTML = user.createdOn;
            username.innerHTML = user.username;
            isAdmin.innerHTML = user.isAdmin;
            viewUser.innerHTML = `<a href='create-admin.html?userName=${ user.username }' id='makeAdmin'>Make Admin</a>`;
          });
        } else if (message === 'Token has expired') {
          window.alert('Please log in');
          window.location.replace('index.html');
        } else{
          document.getElementById('alert').style.color = 'red';
          document.getElementById('alert').innerHTML = data.message;
        }
      });
  }
};

setTimeout(() => {
  window.location.replace('index.html');
}, 250000);
