# RblxRoll-rain-notifier

## Release v1.0:
- Release, more things to be added

**If you encounter an bug/error please open an issue!**

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Information:
- When there is a rain at [rblxroll](https://rblxroll.com) this program will notify you about the rain with some information about it
- If you want to use it check license so you know your limits
- Virustotal for exe: https://www.virustotal.com/gui/file/4e448bba52e160259eb2e2d1ae3c6236ce3fb60237b11a5a23bc454a064464ef
- If you dont trust it, its literally open source

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation:
1) First download the latest version of the program, either the exe or the python version.
2) Extract the files to a folder of your choice
3) If you are using the python version make sure you have installed the latest version!
4) Fill out the **config.json** file using the config guide below to help you!
5) Now run the installer.bat if you are using and it sdhould start running! If you are using the exe just double click on it!
- Any problems open up a new issue on this github respitory!

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Config guide:

Default config.json file:
```json
{
  "webhook_ping": "<@1234567890987654>",
  "webhook": "https://discord.com/api/webhooks/xxxxxxxx/xxxxxxxxxxxxxx",
  "roll_token": "eygdfgdfgdsf"
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

### rblxroll_token:
This is your rblxroll login token, this is used to connect to the websocket.

- To get this head to [rblxroll](https://rblxroll.com).
- Next press the "F12" key on your keyboard or "CTRL + SHIFT + I"
- Now make sure "console" is selected, if not just click on it (image attached)

![image](https://user-images.githubusercontent.com/79641603/178447705-533c36c2-d3c1-4019-ab0c-8cd7770e4350.png)

- Next paste in the code below and hit enter
```
copy(localStorage.getItem('token'))
```
- You should now have your rblxroll token copied to your clipboard, just open your config file and paste it inbetween the quotation marks.

## Current Issues:
- None