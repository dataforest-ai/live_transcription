# live_transcription
A tool for real-time audio transcription built with OpenAI Whisper. 

# Usage

In order to use the live audio transcription tool, one has to execute the below steps:

1. Install PyAudio and ffmpeg:
   ```bash
   bash scripts/setup.sh
   ```
   
3. Install the whisper-live library:
   ```bash
   pip install whisper-live
   ```

## Faster Whisper backend server setup 

The command to run the server with the Faster Whisper backend:
``` bash
python3 run_server.py --port 9090 --backend faster_whisper
```

Additionally, one can run the server using a custom model:
```bash 
python3 run_server.py --port 9090 \
                      --backend faster_whisper \
                      -fw "/path/to/custom/faster/whisper/model"
```

## Running the client 

An example client setup can be found in the **test_client.py** script:
```python
from whisper_live.client import TranscriptionClient


if __name__ == "__main__":
  client = TranscriptionClient(
    "localhost",
    9090,
    lang="en",
    translate=False,
    model="small",  
    use_vad=False,  
    save_output_recording=False,  
  )

  client() 
```

- The above setup is for transcribing from microphone.

- Using the client to transcribe an audio file:
```python
client("tests/jfk.wav")
```

- Using the client to transcribe from an RTSP stream:
```python
client(rtsp_url="rtsp://admin:admin@192.168.0.1/rtsp")
```

- Using the client to transcribe from an HLS stream:

```python
client(hls_url="http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_1xtra/bbc_1xtra.isml/bbc_1xtra-audio%3d96000.norewind.m3u8")
```

## Docker server setup

- CPU:
```bash
docker run -it -p 9090:9090 ghcr.io/collabora/whisperlive-cpu:latest
```

- GPU:
```bash
docker run -it --gpus all -p 9090:9090 ghcr.io/collabora/whisperlive-gpu:latest
```

## Browser extensions
In case of setting up the tool as a browser extension, please refer to the respective documentation:
- [Chrome extension documentation](https://github.com/dataforest-ai/live_transcription/blob/main/Audio-Transcription-Chrome/README.md)
- [Mozilla Firefox extension documentation](https://github.com/dataforest-ai/live_transcription/blob/main/Audio-Transcription-Firefox/README.md)
