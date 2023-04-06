import websockets, asyncio, json, time
from discord_webhook import DiscordWebhook, DiscordEmbed

with open("config.json", "r") as config:
  config = json.load(config)

webhookurl = config['webhook']
ping = config['webhook_ping']
token = config['roll_token']

webhook = DiscordWebhook(url=webhookurl, content=f"{ping}")

async def handler(ws):
    async for message in ws:
        if message == "2":
            await ws.send("3")
        try:
            msg = json.loads(message.replace("42/general,", ""))
            print(msg)
            if msg[0] == "rain" and msg[1]['rain']['state'] == "running":
                amount = msg[1]['rain']['amount']
                rain_type = msg[1]['rain']['type']
                prize = (format(int(amount),","))
                re_prize = prize[:-4]
                print(f"{re_prize} | {rain_type} | 2 min")
                timestamp = int(time.time()) + 120
                embed = DiscordEmbed(title=f"RBLXROLL Rain!", url="https://rblxroll.com", color=0x01E2A4)
                embed.add_embed_field(name="Rain Amount", value=f"{re_prize} R$")
                embed.add_embed_field(name="Rain Type", value=f"{rain_type}")
                embed.add_embed_field(name="Expiration", value=f"<t:{timestamp}:R>")
                embed.set_timestamp()
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/977857118189289512/1093472503713767454/logo.1381439b.png")
                webhook.add_embed(embed)
                webhook.execute()
                webhook.remove_embed(0)
                time.sleep(125)
                await start_client()
        except:
            pass

async def start_client():
    while True:
        try:
            async with websockets.connect("wss://api.rblxroll.com/socket.io/?EIO=4&transport=websocket") as ws:
                await ws.send("40/general,{}")
                await handler(ws)
        except websockets.exceptions.ConnectionClosed as e:
            print(f"Connection closed with code {e.code}.")
        except websockets.exceptions.WebSocketException as e:
            print(f"WebSocket exception: {e}")
        await asyncio.sleep(5)

asyncio.run(start_client())
