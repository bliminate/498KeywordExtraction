import os

def get_annotations(text_name):
    text_name = text_name.split('/')[1]
    text_id = text_name[:-4]
    annotations = set()
    files = []
    teams = os.walk("teams")
    for dirpath, dirnames, filenames in teams:
        for filename in filenames:
            file_id = filename.split('.')
            if file_id[0] == text_id:
                files.append(os.sep.join([dirpath, filename]))
    for file in files:
        with open(file, 'r') as datafile:
            text = datafile.read()
            datalines = text.split('\n')
            for dataline in datalines:
                if dataline: 
                    dataline = dataline.split(" ", 1)
                    annotations.add(dataline[1].lower())
    return annotations

def get_input_files():
    names = []
    documents = os.walk("documents")
    for dirpath, dirnames, filenames in documents:
        for filename in filenames:
            if filename.endswith(".txt"):
                filename = os.sep.join([dirpath, filename])
                names.append(filename)
    return names

#print get_text_files()
#annotations = get_annotations("287.txt")
#blah = [('Index', 342), ('fdsa', 342)]
#print get_accuracy(blah, annotations)
# observed = ['blah', 'Index', 'Keywords']
# accuracy = get_accuracy(observed, annotations)
# print accuracy