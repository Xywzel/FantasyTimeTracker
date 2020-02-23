import os

class File:
    def __init__(self, fullpath):
        self.friendly_name = os.path.basename(fullpath)
        self.relpath = os.path.relpath(fullpath, os.path.join(os.getcwd(), "data", "files"))
        self.child = []
        if os.path.isdir(fullpath):
            self.type = "dir"
            for filename in os.listdir(fullpath):
                newfile = os.path.join(fullpath, filename)
                self.child.append(File(newfile))
        else:
            self.type = self.friendly_name.split(".")[1]
        if self.type == "md":
            self.link = "http://127.0.0.1:5000/markdown/" + self.relpath
        elif "creatures/" in self.relpath and self.type == "json":
            self.link = "http://127.0.0.1:5000/" + self.relpath.replace("creatures", "creature")
        else:
            self.link = "http://127.0.0.1:5000/file/" + self.relpath
        self.child.sort(key= lambda x: (x.type, x.friendly_name))

    def __repr__(self):
        return "File %s %s %s %s" % (self.friendly_name, self.relpath, self.type, self.link)

    def __cmp__(self, other):
        return self.type.__cmp__(other.type)

