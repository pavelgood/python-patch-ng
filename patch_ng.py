__version__ = "1.18.0"
        # git-format-patch with --full-index generates full blob index, which is 40 symbols length
        # shortcut index length may vary, seems to depend on the project size
            and re.match(b'(?:index \\w{7,40}..\\w{7,40} \\d{6}|new file mode \\d*)', p.header[idx+1])):