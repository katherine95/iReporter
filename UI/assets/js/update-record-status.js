window.onload = function () {
  getRecord();

  function getRecord() {
    const token = localStorage.getItem('token');
    const message = localStorage.getItem('message');
    const url = new URL(window.location.href);
    const recordId = url.searchParams.get('recordId');
    const user_id = localStorage.getItem('user_id');

    const status = document.getElementById('status');

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
        if (data.status === 200) {
          status.value = data.data.status;
        } else if (data.status === 404) {
          window.alert('Record with that ID does not exist.');
          window.location.replace('user-account.html');
        } else if (data.message) {
          document.getElementById('alert').style.color = 'red';
          document.getElementById('alert').innerHTML = data.message;
        }
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
  const status = document.getElementById('status').value;

  fetch(`https://floating-reaches-50695.herokuapp.com/api/v2/incidents/${recordId}`, {
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
        status,
      }
),
  })
    .then(response => response.json())
    .then((data) => {
      console.log(data.status);
      if (data.status === 200) {
        window.alert('Status changed Successfully');
        window.location.replace('admin.html');
      } else if (data.status === 400) {
        window.alert('Status can only be updated to resolved, inDraft or rejected');
        window.location.href;
      } else if (message === 'Token has expired') {
        window.alert('Please log in');
        window.location.replace('index.html');
      } else{
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
