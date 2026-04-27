from functions.get_files_info import get_files_info


def main():
    cases = [
        ("Result for current directory:", "calculator", "."),
        ("Result for 'pkg' directory:", "calculator", "pkg"),
        ("Result for '/bin' directory:", "calculator", "/bin"),
        ("Result for '../' directory:", "calculator", "../"),
    ]

    for header, working_dir, directory in cases:
        print(header)
        print(get_files_info(working_dir, directory))
        print("")


if __name__ == "__main__":
    main()