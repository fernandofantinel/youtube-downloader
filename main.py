from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download()
    except:
        print("There has been an error in downloading this Youtube video.")
    print("The download has completed!")
    
link = input("Put a valid Youtube link here. URL: ")
Download(link)
