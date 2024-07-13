document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const groupFile = document.getElementById('groupFile').files[0];
    const hostelFile = document.getElementById('hostelFile').files[0];

    const formData = new FormData();
    formData.append('groupFile', groupFile);
    formData.append('hostelFile', hostelFile);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        document.getElementById('downloadLink').href = url;
        document.getElementById('downloadLink').click();
    })
    .catch(error => console.error('Error:', error));
});
