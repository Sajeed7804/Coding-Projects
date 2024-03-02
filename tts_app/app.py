import requests

url = "https://text-to-speech-neural-google.p.rapidapi.com/generateAudioFiles"

payload = {
	"audioFormat": "ogg",
	"paragraphChunks": ["A detailed analysis of my experience using Open AI’s ChatGPT tool to create code. Intro. ChapGPT sounds too good to be true, so let’s ask it to write some JS code for us. I want to see if it can tackle tasks I do on a daily basis as a front-end dev. Let’s get straight into it and try to break this thing. :). Building a Modal in React. Although it is possible, let’s not start this experiment by adding some code to begin with"],
	"voiceParams": {
		"name": "Wavenet-B",
		"engine": "google",
		"languageCode": "en-IN"
	}
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "bfca210001msh943cbacbdd53f48p1b750fjsndb92cc402198",
	"X-RapidAPI-Host": "text-to-speech-neural-google.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())