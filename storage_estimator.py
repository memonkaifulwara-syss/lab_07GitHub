
print("STORAGE ESTIMATOR")
print("-----------------")

photos = int(input("Enter number of photos: "))
videos = int(input("Enter number of videos: "))
documents = int(input("Enter number of documents: "))

photo_size = photos * 3
video_size = videos * 100
document_size = documents * 1

total = photo_size + video_size + document_size

print("\nStorage Summary")
print("Photos:", photo_size, "MB")
print("Videos:", video_size, "MB")
print("Documents:", document_size, "MB")
print("Total storage required:", total, "MB")
