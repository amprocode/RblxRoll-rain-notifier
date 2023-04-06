# RblxRoll-rain-notifier

## Release v1.1:
- Minor bug fix

**If you encounter a bug/error please open an issue!**

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Information:
- When there is a rain at [rblxroll](https://rblxroll.com) this program will notify you about the rain with some information about it
- If you want to use it check license so you know your limits
- If you dont trust it, its literally open source

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation:
1) First download the latest version of the program.
2) Extract the files to a folder of your choice.
3) Make sure you have installed the latest version!
4) Fill out the **config.json** file using the config guide below to help you!
5) Now run the installer.bat if you are using and it sdhould start running!
- Any problems open up a new issue on this github respitory!

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Config guide:

Default config.json file:
```json
{
  "webhook_ping": "<@1234567890987654>",
  "webhook": "https://discord.com/api/webhooks/xxxxxxxx/xxxxxxxxxxxxxx"
}
```

### webhook_ping:
You can now ping a role or user instead of @everyone. If you need help getting an ID im sure this will help:

https://youtu.be/KVLdpboY7bg

Setting up ping:

If you want to ping **@everyone** or **@here** make sure your webhook_ping setting looks something like this:
```
"webhook_ping": "@everyone",
```
If you want to ping a **user** make sure your webhook_ping setting looks something like this:
```
"webhook_ping": "<@747719812054253568>",
```
If you want to ping a **role** just put a **&** symbol infront of the numbers. It should look something like this:
```
"webhook_ping": "<@&690632567663575090>",
```

**Obviously these are examples, replace the numbers with your own**

### webhook:
Insert you discord webhook inbetween the quotes so the notification can be sent to your server

Example of webhook:

![image](https://user-images.githubusercontent.com/79641603/230377393-ee33031f-6728-4b77-8e34-44fd290f99ec.png)

## Current Issues:
- None