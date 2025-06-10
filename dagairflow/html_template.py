html_templateTest = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DAG Information</title>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            .button-container {
                margin-bottom: 20px;
            }
            .button {
                padding: 8px 16px;
                margin-right: 10px;
                cursor: pointer;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
            }
            .button:hover {
                background-color: #45a049;
            }
            .button.failed {
                background-color: #f44336;
            }
            .button.failed:hover {
                background-color: #d32f2f;
            }
            .button.all {
                background-color: #2196F3;
            }
            .button.all:hover {
                background-color: #0b7dda;
            }
        </style>
    </head>
    <body>
        <h1>DAG Information</h1>
        <div class="button-container">
            <button class="button all" onclick="filterData('all')">ALL</button>
            <button class="button" onclick="filterData('success')">Success</button>
            <button class="button failed" onclick="filterData('failed')">Failed</button>
        </div>
        <table>
            <tr>
                <th>Название</th>
                <th>Время начала</th>
                <th>Время завершения</th>
                <th>Дата за которую был расчет</th>
                <th>Статус</th>
            </tr>
            {% for row in data %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
                <td>{{ row[3] }}</td>
                <td>{{ row[4] }}</td>
            </tr>
            {% endfor %}
        </table>

        <script>
            function filterData(filterType) {
                let url = '/getdag';
                if (filterType === 'success') {
                    url = '/getdag?filter=success';
                } else if (filterType === 'failed') {
                    url = '/getdag?filter=failed';
                }
                window.location.href = url;
            }
        </script>
    </body>
    </html>
"""




html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DAG Information</title>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
        </style>
    </head>
    <body>
        <h1>DAG Information</h1>
        <table>
            <tr>
                <th>Название</th>
                <th>Время начала</th>
                <th>Время завершения</th>
                <th>Дата за которую был расчет</th>
                <th>Статус</th>
            </tr>
            {% for row in data %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
                <td>{{ row[3] }}</td>
                <td>{{ row[4] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """