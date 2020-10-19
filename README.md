# OlympiadaBot
Telegram Bot which provides an information about the results of All-Russian Olympiad for schoolchildren ([ВОШ](https://vos.olimpiada.ru/2020/school)). This bot has low-functionality, nevertheless implements the main task
This bot **requires** these packages:
* Requests - for backend part of our bot
* [Telebot](https://github.com/eternnoir/pyTelegramBotAPI) - for creating a bot

## How it works
We can see the results on [this](https://online.olimpiada.ru) website. So if we open an web-inspector and view the network tab, we will see that we are being redirected to another web-page with our credentials. Therefore, we can make a *get* request of this page and then *post* request our credentials and get json-format file. In this file we can see the information about contestant. Import and send them to the requestor.

## Proper key
The key must lool like this: **sec10/sch771258/11/172wl3** where
> s - just a letter
> ec - Economy
> 10 - Economy code
> sch771273 (sch - school, 77 - region, 1258 - school number)
> 11 - your grade
> 172wl3 - your unique code

In 2019 and earlier* it looked almost the same, but started with the school information: **sch771258/10/g254q8hr9**

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or improve. 