<div align="center">
    <img src="https://github.com/kw4rgs/fast-pokeberries-api/blob/816baf520755cc122e2305eb84e029c5e240918c/cover.png" alt="logo">
</div>

# FAST-POKEBERRIES-API
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Features 💪


## Information 📢


## Documentation 📚

**FastAPI doc**

All the necessary documentation will be available through the URL: 

> server ip:port/api/v1/docs

or 

> server ip:port/api/v1/redoc

**Endpoints**

1) Dashboard:

This is web view dashboard for the App.

>    - Endpoint: /
>    - HTTP Method: GET


2) Pokeberries statistics:

This endpoint retrieves the pokeberries statictics from the external API.

>    - Endpoint: /api/v1/allBerryStats
>    - HTTP Method: GET


## Instructions 🚀

> I will use "ubuntu" for practical purposes..

To deploy and install your project, you can follow these instructions:

1. Update your system:
   ```
   sudo apt update
   ```

2. Upgrade installed packages:
   ```
   sudo apt upgrade
   ```

3. Install Python 3 virtual environment package:
   ```
   sudo apt install python3-venv
   ```

4. Navigate to the `/opt` directory: (or the directory that you prefer)
   ```
   cd /opt
   ```

5. Clone the project repository from GitHub:
   ```
   git clone https://github.com/kw4rgs/fast-pokeberries-api.git
   ```

6. Change to the project directory:
   ```
   cd /opt/fast-pokeberries-api
   ```

7. Create a Python virtual environment:
   ```
   python3 -m venv env
   ```

8. Activate the virtual environment:
   ```
   source env/bin/activate
   ```

9. Install the project dependencies using the requirements.txt file:
    ```
    pip install -r requirements.txt
    ```
    
10. Copy env-example to .env
    ```
    cp env-example .env
    ```
    
11. Edit the .env with the current API URL (to this date 11/23 this is the url)
    ```
    nano .env

    POKEBERRIES_API_URL=https://pokeapi.co/api/v2/berry/

    ```

12. Test the project by running:
    ```
    python main.py
    ```

Tip: To deactivate the virtual environment, simply type `deactivate` in the terminal.



## Authors

- [@kw4rgs](https://www.github.com/kw4rgs)
