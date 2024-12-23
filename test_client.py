from whisper_live.client import TranscriptionClient

# sample client that connects to the default whisper live local server
# if one would like to change the port or the server address the client connects to, one would also have to
# change the respective parameters of the run_server.py script that is running the server

if __name__ == "__main__":
  client = TranscriptionClient(
    "localhost",
    9090,
    lang="en",
    translate=False,
    model="small",  # supports the Systran/faster-whisper-small huggingface model as well
    use_vad=False,  # if False and there is no voice activity detected, sends no audio to the server
    save_output_recording=False,  # if True, will save the audio processed by the model to an audio file
  )

  client()