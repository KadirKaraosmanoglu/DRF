# DRF

Virtualenv kurulumu

    python -m venv env
    env\Scripts\activate

Daha sonra bağımlılıkların yüklenmesi için 

    pip install -r requirements.txt

Uygulamada manage.py nin bulunduğu dizinde aşağıdaki komut ile uygulama ayağa kaldırılabilir.

    python manage.py runserver localhost:3000

**Kullanıcı Adı:** admin

**Şifre:** admin123


yeni bir kullanıcı eklemek için 
    
    localhost:3000/users/register
    {
        "username":"test1",
        "password":"case1234",
        "password2":"case1234"
    }

login olup token almak için

    localhost:3000/users/login
    {
        "username":"test1",
        "password":"case1234"
    }

Örnek kullanım

    import requests

    url = 'http://127.0.0.1:8000/products/'
    headers = {'Authorization': 'Token 8d613af58157ee65235a40b4c261fe31d98a4a9f'}
    r = requests.get(url, headers=headers)

Projedeki tüm servislere Token eklenerek kullanılabilir.

Post istekleri için örnek objeler aşağıdaki gibidir.

    localhost:3000/categories
     {
      "name": "Shoes",
      "description": "Everybody needs shoes."
      }

    localhost:3000/products
     {
        "name": "Yellow Trousers",
        "description": "Flaming trousers.",
        "category": 2,
        "price": 50
     }

    localhost/sliders
    {
      "image": "test1.png",
      "productId": 2
    }

    localhost:3000/favorite
     {
       "productId": 4
     }




