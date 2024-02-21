import requests

video_url = "https://files.heygen.ai/aws_pacific/avatar_tmp/5975289e1d3043838143c8714d8220ce/bfe42400-337d-42ad-ba16-5eb1740b5fbd.mp4?Expires=1709011530&Signature=iUx8HJg6xjeGb~ftAaib9tJ10ZjO9nnckpyYVbc0SKdecHMixj~fCVB8rqGTlCBFicze-HxijBTFOLcheBcr9tFH9lF3II3aRh4ID6sCu9tvYvPN5bkB1uTiOgEhABNtob~MosClZTBrZ1o4J8S99VBTvlaoyDeRSmCFmIhjgrG4d2NbKcW4Hb6YKwIEfIuvl-sBjhvQ5fGHUvYvHfve-ziPNhm64aJstS~PsrOHO6EPem2stYJz7tXWlgi9tznNNy9qC59EnIL-y7ITucl1mtKOwJGnLfbz-Nyabr13t0vXDKxa5YZocseOrTgKOvdTAjFKn2BGKsNgns8JyXwOIA__&Key-Pair-Id=K49TZTO9GZI6K"

response = requests.get(video_url)
if response.status_code == 200:
    with open("downloaded_video.mp4",'wb') as video_file:
        video_file.write(response.content)
    print("Video downloaded successfully")
else:
    print("Failed to download video. Status code: ",response.status_code)
