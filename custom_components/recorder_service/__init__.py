import requests

DOMAIN = "recorder_service"

WAV_ATTR_NAME = "wav"
URL_ATTR_NAME = "target"

def setup(hass, config):
    def handle_recorder(call):
        wav = call.data.get(WAV_ATTR_NAME, '')
        target = call.data.get(URL_ATTR_NAME, '')

        # send wav to file
        f = open("/config/tts/audiorec/rec.wav", "w")
        f.write(wav)
        f.close()

    hass.services.register(DOMAIN, "process", handle_recorder)

    return True
