# DRF

Virtualenv kurulumu

    python -m venv env
    env\Scripts\activate

Daha sonra bağımlılıkların yüklenmesi için 

    pip install -r requirements.txt

Uygulamada manage.py nin bulunduğu dizinde aşağıdaki komut ile uygulama ayağa kaldırılabilir.

    manage.py runserver localhost:3000

**Kullanıcı Adı:** admin

**Şifre:** admin123


yeni bir kullanıcı eklemek için 
    
    localhost:3000/users/register

login olup token almak için

    localhost:3000/users/login

Örnek kullanım

    import requests

    url = 'http://127.0.0.1:8000/products/'
    headers = {'Authorization': 'Token 8d613af58157ee65235a40b4c261fe31d98a4a9f'}
    r = requests.get(url, headers=headers)

Projedeki tüm servislere Token eklenerek kullanılabilir.




