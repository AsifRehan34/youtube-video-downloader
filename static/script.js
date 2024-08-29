document.getElementById('downloadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var url = document.getElementById('url').value;

    if (!url) {
        document.getElementById('message').innerText = 'Please enter a URL!';
        return;
    }

    this.submit();
});
