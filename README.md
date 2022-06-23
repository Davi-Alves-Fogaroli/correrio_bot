# Bot to consume post office api

## Steps to run the project: " https://github.com/Davi-Alves-Fogaroli/correrio_bot/tree/main#readme "

#### To clone repositori 
- $ git init 
- $ git remote add origin https://github.com/Davi-Alves-Fogaroli/correrio_bot.git
- $ git pull origin main

### 1º step: 
-After opening the project in your code versioner, you will need to download the "pipenv" virtual environment
-Reference : " https://pipenv.pypa.io/en/latest/ "
- $ pip install pipenv
- $ pipenv shell
- $ pipenv install

### 2º step:
-After starting and configuring the virtual environment, you will need to download the crhomedriver in your browser's version
-Reference : " https://chromedriver.chromium.org/downloads "
-To find the version of your browser follow the step by step of the images below

![image](https://user-images.githubusercontent.com/61630258/170256891-c7cdcf28-6f35-4765-891c-64ef388c2182.png)

![image](https://user-images.githubusercontent.com/61630258/170257075-632d6097-9768-41e3-a35e-cc29492da081.png)

![image](https://user-images.githubusercontent.com/61630258/170257175-f8e02982-8de8-4e00-9294-6e04b4496000.png)

![image](https://user-images.githubusercontent.com/61630258/170257210-bcd4bfd1-5c0b-4378-9704-77dd3b7d6fb3.png)

-After downloading and unzipping, put your driver in the "driver" folder

### 3º step:
-Set webdriver environment variable
-In the root of the project create a file called ".env" use the file "example.env" as reference
-in ".env", create the variable "DRIVER_PATCH" and pass the relative or absolute path of your web driver (OBS: only one of the ways is enough)

### 4º step:
-With the previous steps done, open the terminal and run the following command:
- $ python main.py

### To run api_correios:
-With the previous steps done, open the terminal and run the following command:
- $ python api_correios.py
- - Before run code 
- ![image](https://user-images.githubusercontent.com/61630258/174611707-27dd7ccd-2186-4861-99d0-9bc4c68dcec6.png)
- After run code 
- ![image](https://user-images.githubusercontent.com/61630258/174611748-2d73ecc7-a209-46f1-b939-73962e0259d0.png)
- Logs 
![log_bot_correrios](https://user-images.githubusercontent.com/61630258/174612155-43d3045c-1d9c-4b4e-84b5-4603ea95e1b6.png)

### To run api_correios:
-With the previous steps done, open the terminal and run the following command:
- $ python main.py

- Before run code 
- ![image](https://user-images.githubusercontent.com/61630258/174611707-27dd7ccd-2186-4861-99d0-9bc4c68dcec6.png)
- After run code 
- ![image](https://user-images.githubusercontent.com/61630258/174611748-2d73ecc7-a209-46f1-b939-73962e0259d0.png)

- Logs 
![log_bot_correrios](https://user-images.githubusercontent.com/61630258/174612155-43d3045c-1d9c-4b4e-84b5-4603ea95e1b6.png)
