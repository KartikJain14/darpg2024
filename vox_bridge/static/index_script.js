document.addEventListener('DOMContentLoaded', (event) => {
    console.log('Document loaded');

    const uploadButton = document.getElementById('uploadButton');
    const fileInput = document.getElementById('fileInput');

    uploadButton.addEventListener('click', () => {
        console.log('Process button clicked');

        // Check if there is a file selected
        if (fileInput.files.length > 0) {
            const file = fileInput.files[0];
            console.log('File selected:', file.name);

            // Prepare the file to be uploaded
            const formData = new FormData();
            formData.append('audioFile', file); // Ensure the 'name' attribute in FormData matches the input's name
            alert('Your file is being processed. This may take upto 2 minutes.');
            uploadButton.disabled = true;
            uploadButton.innerText = 'Processing...';
            // Use fetch API to send the file to the server
            fetch('/api', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.text())
            .then(html => {
                // Replace the current document content with the received HTML
                document.write(html);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        } else {
            console.log('No file selected');
        }
    });
});
