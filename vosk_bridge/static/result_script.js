function copyText(paragraphId) {
    const paragraphText = document.getElementById(paragraphId).innerText;
    navigator.clipboard.writeText(paragraphText).then(() => {
        console.log('Paragraph copied!');
    }, () => {
        alert('Failed to copy paragraph.');
    });
}

function saveText(paragraphId, filename) {
    const paragraphText = document.getElementById(paragraphId).innerText;
    const element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(paragraphText));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}