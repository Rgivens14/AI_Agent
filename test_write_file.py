from functions.write_file import write_file


def main():

    cases = [
        ("Result for 'pkg' directory:", "calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("Result for 'pkg' directory:", "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("Result for 'pkg' directory:", "calculator", "/tmp/temp.txt", "wait, this should not be allowed")
    ]

    for header, working_dir, file_path, content in cases:
        print(header)
        print(write_file(working_dir, file_path, content))
        print("")


if __name__ == "__main__":
    main()