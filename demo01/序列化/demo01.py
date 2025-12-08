import requests


response = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
if response.status_code == 200:
    result = response.json();
    print(result)