import base64
from collections import OrderedDict

import requests
import json

PLAYABLE_CHARACTERS_DATA_URL\
    = "https://api.github.com/repos/genshin-impact-api/wiki-data/contents/playable-characters.json"

if __name__ == "__main__":
    data: dict = OrderedDict()

    playable_characters: list[dict] = json.loads(
        base64.b64decode(json.loads(requests.get(PLAYABLE_CHARACTERS_DATA_URL).text)["content"]).decode('utf-8')
    )
    data["playableCharacters"] = []
    for idx in range(len(playable_characters)):
        playable_characters[idx]["id"] = idx + 1
        data["playableCharacters"].append(
            playable_characters[idx]
        )

    with open("db.json", "w") as data_file:
        data_file.write(json.dumps(data, indent=4, ensure_ascii=False))
