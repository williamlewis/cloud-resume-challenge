const api_url = 'https://gqzq4elpqa.execute-api.us-east-1.amazonaws.com/Production/count'

    fetch(api_url, {
        method: 'POST'
    })
        .then((response) => response.json())
        .then((data) => {document.getElementById('displayed-count').innerHTML = 'Total Page Views:  ' + data['total_views']});
                    