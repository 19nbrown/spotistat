# Spotistat

Spotistat is a self-hosted FastAPI web app that provides personalized Spotify stats and playlist analytics. It runs in a Docker container and offers a simple web interface to authenticate with Spotify and explore your listening data.

## Features

-  OAuth2 login with Spotify
-  Streaming Stats: Top Artists, Songs, Albums by time range (Last Day, Week, Month, Year, All Time)
-  Playlist Stats: Analyze your playlists for most/least streamed items, artist distributions, and more
-  Docker-ready and self-hosted at `localhost:6969`

## Requirements

- Docker + Docker Compose
- A Spotify Developer Account and App (for Client ID and Secret)

## Setup

### 1. Clone the Repository

`git clone https://github.com/yourusername/spotistat.git`

`cd spotistat`

### 2. Create a Spotify Developer App

   1. Go to https://developer.spotify.com and login
      
   2. Go to Dashboard ---> Create app
      
   3. For App Name: Spotistat
    
       For App Description: <Anything>
       
       For Redirect URLs:

      `http://<your-local-ip>:6969/callback`
      
   5. Click Save, and paste your client id and client secret somewhere for later

### 3. Build and Run

  1. In the root of Spotistat/ run
    
     `docker compose down --volumes --remove-orphans
docker compose build --no-cache
docker compose up -d`

  2. Open
     
   `http://<your-local-ip>:6969`

### 4. Authenticate

   1. When Prompted, enter Client ID and Client Secret, then Login


### Notes:

  Your client secrets are are passed only during seasion and not stored


MIT License. PRs Welcome!
