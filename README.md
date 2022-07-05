#Helium HTTP Integration

A simple HTTP integration for helium console that saves packets to a json file.
Packets are saved into unique folders for each device, each containing folders for the date.
Each packet is saved to an individual json folder.

To run the container on port 8000 of the host and saving packets to ./packets:

`docker run -d --name helium-http-integration -p 8000:80 -v $(pwd)/packets:/workdir/packets goshawk22/helium-http-integration:latest`