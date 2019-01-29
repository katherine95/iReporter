// Initialize Firebase
document.getElementById('custom-button').addEventListener('change', handleFileUploadChange);
document.getElementById('createIncident').addEventListener('submit', handleFileUploadSubmit);
const config = {
  apiKey: 'AIzaSyCrpgN6i3GyddMRhYgS7arjWcSNE5nDZRw',
  authDomain: 'ireporter-27f48.firebaseapp.com',
  databaseURL: 'https://ireporter-27f48.firebaseio.com',
  projectId: 'ireporter-27f48',
  storageBucket: 'ireporter-27f48.appspot.com',
  messagingSenderId: '186862939691',
};
firebase.initializeApp(config);
const storageService = firebase.storage();
const storageRef = storageService.ref();

let selectedFile;
handleFileUploadChange(e) {
  selectedFile = e.target.files[0];
}

function handleFileUploadSubmit(e) {
  const uploadTask = storageRef.child(`images/${selectedFile.name}`).put(selectedFile); // create a child directory called images, and place the file inside this directory
  uploadTask.on('state_changed', (snapshot) => {
    // Observe state change events such as progress, pause, and resume
  }, (error) => {
    // Handle unsuccessful uploads
    console.log(error);
  }, () => {
    // Do something once upload is complete
    console.log('success');
  });
}
