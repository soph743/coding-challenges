import os
import argparse

class fileOrganizer():
    # constructor
    def __init__(self, top_folder_path):
        self.top_folder_path = top_folder_path

    def get_statistics(self, argument):
        if argument == False:
            self.show_all_stats()
        else:
            self.show_summary()

    def show_all_stats(self):
        rootdir = self.top_folder_path

        indent = ""
        base_slashes = self.get_slashes(rootdir)

        for (root, _, files) in os.walk(rootdir):

            videos = 0
            images = 0
            text = 0
            data = 0
            models = 0
            other = 0
            
            for f in files:
                if f.endswith(".mp4"):
                    videos = videos + 1

                elif f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"):
                    images = images + 1

                elif f.endswith(".txt") or f.endswith(".md") or f.endswith(".docx") or f.endswith(".pdf"):
                    text = text + 1

                elif f.endswith(".xlsx") or f.endswith(".csv") or f.endswith(".json"):
                    data = data + 1

                elif f.endswith(".yaml") or f.endswith(".pt") or f.endswith(".pth") or f.endswith(".h5"):
                    models = models + 1

                else:
                    other = other + 1

            indent = "      " * (self.get_slashes(root) - base_slashes)
            
            folderpath = root.split('/')
            foldername = folderpath[-1]

            print(indent + "/" + foldername + " statistics")
            print(indent + "    videos: " + str(videos))
            print(indent + "    images: " + str(images))
            print(indent + "    text: " + str(text))
            print(indent + "    data: " + str(data))
            print(indent + "    models: " + str(models))
            print(indent + "    other: " + str(other))
            print('\n')

    def show_summary(self):
        rootdir = self.top_folder_path

        videos = 0
        images = 0
        text = 0
        data = 0
        models = 0
        other = 0
        
        for (root, _, files) in os.walk(rootdir):
            
            for f in files:
                if f.endswith(".mp4"):
                    videos = videos + 1

                elif f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"):
                    images = images + 1

                elif f.endswith(".txt") or f.endswith(".md") or f.endswith(".docx") or f.endswith(".pdf"):
                    text = text + 1

                elif f.endswith(".xlsx") or f.endswith(".csv") or f.endswith(".json"):
                    data = data + 1

                elif f.endswith(".yaml") or f.endswith(".pt") or f.endswith(".pth") or f.endswith(".h5"):
                    models = models + 1

                else:
                    other = other + 1

        folderpath = rootdir.split('/')
        foldername = folderpath[-1]

        print("/" + foldername + " summary statistics for all files and subfolders")
        
        print("     videos: " + str(videos))
        print("     images: " + str(images))
        print("     text: " + str(text))
        print("     data: " + str(data))
        print("     models: " + str(models))
        print("     other: " + str(other))

    def get_slashes(self, currdir):
        path = currdir.split('/')
        return len(path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder')
    parser.add_argument('--summary', action='store_true')
    args = parser.parse_args()

    stats = fileOrganizer(args.folder)
    stats.get_statistics(args.summary)



if __name__ == '__main__':
    main()