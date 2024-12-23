## Loading the Extension
- Open the Mozilla Firefox browser.
- Type ```about:debugging#/runtime/this-firefox``` in the address bar and press Enter.
- Clone this repository
- Click the Load temporary Add-on.
- Browse to the location where you cloned the repository files and select the ```Audio Transcription Fox``` folder.
- The extension should now be loaded and visible on the extensions page.


## Real time transcription with OpenAI-whisper
This Firefox extension allows you to send audio from your browser to a server for transcribing the audio in real time. 

## Implementation Details

### Options
When using the Audio Transcription extension, you have the following options:
 - **Language**: Select the target language for transcription or translation. You can choose from a variety of languages supported by OpenAI-whisper.
 - **Task:** Choose the specific task to perform on the audio. You can select either "transcribe" for transcription or "translate" to translate the audio to English.
  - **Model Size**: Select the whisper model size to run the server with.

### Getting Started
- Make sure the transcription server is running properly. To know more about how to start the server, see the [documentation here](https://github.com/dataforest-ai/live_transcription/blob/main/README.md).
- Just click on the Firefox Extension which should show 2 options
  - **Start Capture** : Starts capturing the audio in the current tab and sends the captured audio to the server for transcription. This also creates an element to show the transcriptions recieved from the server on the current tab.
  - **Stop Capture** - Stops capturing the audio.


## Limitations
This extension requires an internet connection to stream audio and receive transcriptions. The accuracy of the transcriptions may vary depending on the audio quality and the performance of the server-side transcription service. The extension may consume additional system resources while running, especially when streaming audio.

## Note
The extension relies on a properly running transcription server with multilingual support. Please follow the server documentation for setup and configuration.