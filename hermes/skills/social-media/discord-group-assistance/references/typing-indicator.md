# Discord typing-indicator diagnosis

Use this when someone sees the bot typing after its answer has been sent. Hermes may legitimately refresh typing while a turn is running; a response-ready log alone cannot prove that its adapter stopped sending typing requests. Discord's typing indicator expires after roughly 10 seconds unless refreshed.

1. **Establish timing and identity.** Record the message's response-ready and sent times from gateway logs, the affected channel ID, and the bot's user ID. A report made during an active turn is not evidence of a loop. Avoid a gateway restart until the observation is complete.
2. **Observe the gateway event stream read-only.** Open a temporary second `discord.py` client using the active profile's exact `DISCORD_BOT_TOKEN` key (`hermes config env-path`), without printing or passing the token as a command argument. Subscribe to `guilds` and `typing` intents. Filter `on_raw_typing` by the channel ID and bot user ID; log timestamps only. For example, in a temporary Python probe run with an interpreter that has `discord.py`:

```python
import asyncio
import datetime
import os
from pathlib import Path
import discord

channel_id = int(os.environ['TARGET_CHANNEL_ID'])
env_path = Path(os.environ['HERMES_ENV_PATH'])
token = next(line.partition('=')[2].strip().strip('"') for line in env_path.read_text().splitlines() if line.startswith('DISCORD_BOT_TOKEN='))
intents = discord.Intents.none()
intents.guilds = True
intents.typing = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('observer ready; bot user:', client.user.id, flush=True)

@client.event
async def on_raw_typing(payload):
    if payload.channel_id == channel_id and payload.user_id == client.user.id:
        print(datetime.datetime.now(datetime.timezone.utc).isoformat(), 'TYPING_START', flush=True)

async def main():
    try:
        async with client:
            await asyncio.wait_for(client.start(token), timeout=45)
    except asyncio.TimeoutError:
        pass

asyncio.run(main())
```

Set `HERMES_ENV_PATH` from `hermes config env-path` and `TARGET_CHANNEL_ID` to the affected channel. Run the observer while the bot is actively answering once to verify that its own events are visible to this client; a silent unvalidated observer is inconclusive.
3. **Measure an idle window.** Leave the observer connected for at least 20 seconds after the reply is delivered, preferably 30 seconds, without sending another message in that channel. Events recurring in that window indicate continuing refreshes, not a single stale Discord indicator. No events beyond expiry while a client still displays typing point toward a client-side visual state, a different bot identity, or an unvalidated observer; check the identity and validation before choosing.
4. **Trace only after classification.** If events recur, inspect the adapter's `send_typing` / `stop_typing` task lifecycle and the gateway's cleanup path; test a minimal reproducible race before changing code. If no events recur, ask for a second Discord client or reload the original client to distinguish local display caching. Report observed timestamps and the remaining uncertainty; do not claim a root cause from source code or logs alone.
