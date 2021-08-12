from pytube import YouTube
print("Welcoe to Youtube Downloader")

url = "https://www.youtube.com/watch?v=WtHnT73NaaQ&list=PLwP4ObPL5GY940XhCtAykxLxLEOKCu0nT" #input("Youtube link :")
yt = YouTube(url)

location = "D:\Siber Güvenlik\Egitim\WebHack" #input("Path Location:")


print("Downloading:", yt.title)
yt.streams.get_highest_resolution().download(output_path=location)
print("Download: ", yt.title)



