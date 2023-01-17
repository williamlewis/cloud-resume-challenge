const api_url = 'https://sm82gzbtzk.execute-api.us-east-1.amazonaws.com/prod/count'

    fetch(api_url, {
        method: 'POST'
    })
        .then((response) => response.json())
        .then((data) => {document.getElementById('displayed-count').innerHTML = 'Total Page Views:  ' + data['total_views']});
                    