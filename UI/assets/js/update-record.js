window.onload = function () {
  getRecord();

  function getRecord() {
    const token = localStorage.getItem('token');
    const message = localStorage.getItem('message');
    const url = new URL(window.location.href);
    const recordId = url.searchParams.get('recordId');
    const userId = localStorage.getItem('userId');

    const comment = document.getElementById('comment');
    const location = document.getElementById('location');

    fetch(`https://floating-reaches-50695.herokuapp.com/api/v2/incidents/${recordId}`, {
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
        console.log(data.data.location);
        if (data.status === 200) {
          comment.value = data.data.comment;
          location.value = data.data.location;
        }
        setTimeout(() => {
          window.location.replace('index.html');
        }, 300000);
});
  }
};
document.getElementById('updateIncident').addEventListener('submit', updateIncident);
function updateIncident(e) {
  e.preventDefault();
  const token = localStorage.getItem('token');
  const message = localStorage.getItem('message');
  const url = new URL(window.location.href);
  const recordId = url.searchParams.get('recordId');
  const comment = document.getElementById('comment').value;
  const location = document.getElementById('location').value;

  fetch(`https://floating-reaches-50695.herokuapp.com/api/v2/user/incidents/${recordId}`, {
    method: 'PATCH',
    headers: {
      Accept: 'application/json',
      'Content-type': 'application/json',
      mode: 'cors',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Request-Method': '*',
      Authorization: 'Bearer ' + token,
    },
    body: JSON.stringify(
      {
        comment,
        location,
      }
),
  })
    .then(response => response.json())
    .then((data) => {
      if (data.status === 200) {
        window.location.replace('user-account.html');
        setTimeout(() => {
          window.location.replace('index.html');
        }, 300000);
      } else {
        console.log(data.msg);
        localStorage.setItem('message', data.msg);
        document.getElementById('alert').style.color = 'red';
        document.getElementById('alert').innerHTML = data.message;
      }
    });
}
setTimeout(() => {
  window.location.replace('index.html');
}, 250000);
