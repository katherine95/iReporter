window.onload = function () {
  getRecord();

  function getRecord() {
    const token = localStorage.getItem('token');
    const message = localStorage.getItem('message');
    const url = new URL(window.location.href);
    const recordId = url.searchParams.get('recordId');
    const role = localStorage.getItem('role');

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
        if (data.status === 200 && role == 'true') {
          const incidentType = document.getElementById('type');
          const comment = document.getElementById('comment');
          const location = document.getElementById('location');
          const createdOn = document.getElementById('createdOn');
          const image = document.getElementById('image');
          const status = document.getElementById('status');
          const editRecord = document.getElementById('edit');

          incidentType.innerHTML = data.data.incidentType;
          comment.innerHTML = data.data.comment;
          location.innerHTML = data.data.location;
          createdOn.innerHTML = data.data.createdOn;
          image.innerHTML = data.data.image[0];
          status.innerHTML = data.data.status;
          editRecord.innerHTML = `<a href='update-record-status.html?recordId=${ data.data.id }'>Edit</a>`;
        } else if (data.status === 200) {
          const incidentType = document.getElementById('type');
          const comment = document.getElementById('comment');
          const location = document.getElementById('location');
          const createdOn = document.getElementById('createdOn');
          const image = document.getElementById('image');
          const status = document.getElementById('status');
          const editRecord = document.getElementById('edit');

          incidentType.innerHTML = data.data.incidentType;
          comment.innerHTML = data.data.comment;
          location.innerHTML = data.data.location;
          createdOn.innerHTML = data.data.createdOn;
          image.innerHTML = data.data.image[0];
          status.innerHTML = data.data.status;
          editRecord.innerHTML = `<a href='update-record.html?recordId=${ data.data.id }'>Edit</a>`;
        } else if (message === 'Token has expired') {
          window.alert('Please log in');
          window.location.replace('index.html');
        }else {
          document.getElementById('alert').style.color = 'red';
          document.getElementById('alert').innerHTML = data.message;
        }
      });
  }
};
document.getElementById('delete').addEventListener('click', deleteRecord);
function deleteRecord() {
  const token = localStorage.getItem('token');
  const message = localStorage.getItem('message');
  const url = new URL(window.location.href);
  const recordId = url.searchParams.get('recordId');

  fetch(`https://floating-reaches-50695.herokuapp.com/api/v2/incidents/${recordId}`, {
    method: 'DELETE',
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
      console.log(data.message);
      if (data.status === 200) {
        window.alert('Deleted successfully');
        window.location.replace('user-account.html');
      } else if (data.status === 404) {
        window.alert('Record with that ID does not exist.');
        window.location.replace('user-account.html');
      } else if (data.message) {
        document.getElementById('alert').style.color = 'red';
        document.getElementById('alert').innerHTML = data.message;
 }
    });
}
