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

-   **FastAPI App:** Utilizes FastAPI, a high-performance web framework for building APIs in Python, ensuring fast development and efficient handling of requests.
-   **Production-Ready:** Configured and optimized for production environments, incorporating best practices for stability and performance.
-   **Dockerized:** Offers a containerized version using Docker, ensuring consistent deployment across different environments and simplifying setup.
-   **Easy Deployment:** Streamlines deployment using Docker Compose or Dockerfiles, making it hassle-free for various environments.
-   **Documentation:** Automatically generates API documentation for clear and accessible endpoints, simplifying usage for developers and users.

## Information 📢

The API provide this information:

 - **"berries_names":** An alphabetically sorted list of all the unique
   names of the berries.
 - **"min_growth_time":** Represents the shortest growth time among all the
   berries.
 - **"median_growth_time":** The middle value of the growth times representing the median growth time of the
   berries.
 - **"max_growth_time":** Indicates the longest growth time among the berries.
 - **"variance_growth_time":** Represents the variance in the growth times across all berries, showing how much they differ from the mean.
 - **"mean_growth_time":** The average growth time calculated across all the berries.
 - **"frequency_growth_time":** Provides a breakdown of the frequency of different growth times among the berries.

## Documentation 📚

**FastAPI doc**

All the necessary documentation will be available through the URL: 

> server ip:port/docs

or 

> server ip:port/redoc

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

1) Cloning the repository to local
2) Cloning the reposirtory to a web server
3) Using the dockerized version

### 1) Cloning the repository to local

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
   cd fast-pokeberries-api
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
    
11. Edit the .env.prod with the current API URL (to this date 11/23 this is the url)
    ```
    nano .env

    ENVIRONMENT="Production"
    POKEBERRIES_API_URL="https://pokeapi.co/api/v2/berry/"

    ```

12. Test the project by running:
    ```
    python main.py
    ```

Tip: To deactivate the virtual environment, simply type `deactivate` in the terminal.


### 2) Cloning the reposirtory to a web server

To deploy as a web service, follow these additional steps:

1. Open the systemd service configuration file in a text editor:
   ```
   sudo nano /etc/systemd/system/fast-pokeberries-api.service
   ```

2. Paste the following content into the file:
   ```
   [Unit]
   Description=Pokeberries FastAPI Application
   After=network.target

   [Service]
   User=<your_username>
   Group=<your_groupname>
   WorkingDirectory=/opt/fast-pokeberries-api #Or the directory where you put the app
   ExecStart=/opt/fast-pokeberries-api/env/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 #same in here
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Replace `<your_username>` and `<your_groupname>` with your actual username and group name.

3. Save the file and exit the text editor.

4. Enable the service to start on boot:
   ```
   sudo systemctl enable fast-pokeberries-api.service
   ```

5. Start the service:
   ```
   sudo systemctl start fast-pokeberries-api.service
   ```

Now, your application has been deployed and should run as a systemd service. It will automatically start on boot and restart if it crashes.

### 3) Using the dockerized version

## Authors

- [@kw4rgs](https://www.github.com/kw4rgs)
