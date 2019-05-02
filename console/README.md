# Insurance Auto Auctions, Inc. (IAAI) Python console app

Using Azure Cognitive Services, this Python console application will serve as a **Proof of Concept** which demonstrates the deployment of the Speech SDK used in speech recognition activities conducted at Live Auctions.  **By using the Cognitive Services Speech SDK you acknowledge its license, see [Speech SDK license agreement](https://aka.ms/csspeech/license201809).**

## Prerequisites

* Python 3.5 or later needs to be installed. Downloads are available [here](https://www.python.org/downloads/).
* The Speech SDK Python package is available for Windows (x64 and x86)
* Installation required: [Microsoft Visual C++ Redistributable for Visual Studio 2017](https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads)

## Build the sample


* Install the Speech SDK Python package in your Python interpreter by executing this command
  ```sh
  pip install azure-cognitiveservices-speech
  ```
  in a terminal.

## Update the speech_key, service_region

Create your [Cognitive Services resources](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account)  .  Next, access the 'speech_sdk.py' file and update the Speech Key and Service Region.

## Run the sample console application

To run the app, navigate to the `speech-2-txt-console/console` directory in your local copy of the this repository.
Start the app with the command

```sh
python main.py
```

The Python executable should be called `python`.  The output from this console application will also create a text file in the `speech-2-txt-console/console/output` directory

The app displays a menu that you can navigate using your keyboard.
Choose the scenarios that you're interested in.  I've created outputs for samples in duration of 1 min, 2 min, 4 min and continuous stream using this configuration and the microphone on my laptop.
