import requests

def handler(event, context):
    phone_number_id = "555428137646001"
    message = "Hola desde Vercel!"
    token = "EAGKP9iEo0ZAoBO2ifH4Ofjgb2ZBvCY1q8ulFETl4Ey2oU9ZA6ZCuvFcjVHSBA1casSZA4EG9VNwBgMBXKTSpZCzjkcvCcjhJ6SZBNUf6nSkKgXvGt4vwGVzaQHxiki7OTD95KOlXiQPndu2pVkltOt9s7uheWDVhg9CqEPwd760KPyzVWoSa3ZCYsxBcwoCpif2chIfaiBnqEs8oZA9yE9gqmbEkYBRAYbYfkWBzJjt8i7FMZD"

    url = f"https://graph.facebook.com/v16.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": phone_number_id,
        "text": {
            "body": message
        }
    }

    response = requests.post(url, headers=headers, json=data)
    return {
        statusCode: 200,
        body: response.text
    }