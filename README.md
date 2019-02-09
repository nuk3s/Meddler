# Meddler


  This is a quick proof-of-concept script that is capable of manipulating pigeonhole.at polls that don't have any selective filtering turned on.  These polls are common a group gatherings as it allows the organizers to solicit anonymous feedback or questions from the audience and then answer or engage with the most popular.  pigeonhole.at appears to use each unique session as the means to keep track of who has voted and who has not, often just restarting you browser will allow you to vote again.  This script simply automates that process.
  
## Getting Started
  
  You will want to download the latest geckodriver at https://github.com/mozilla/geckodriver/releases and then export it's location to the path with the following:
    
   `export PATH=$PATH:/path/to/geckodriver`
   
  Next, you will want to install selenium with:
  
    pip install selenium
    
  Finally, install firefox if you dont already have it:
  
    apt install firefox
  
  ## Usage
  
    python meddler.py invitecode
