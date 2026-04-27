from functions.get_file_content import get_file_content


def main():

    lorem_result = get_file_content("calculator", "lorem.txt")
    print("Result for lorem.txt:")
    print(f"Length: {len(lorem_result)}")
    print(f"End of content: {lorem_result[-100:]}")
    print("")


    cases = [
        ("Result for 'pkg' directory:", "calculator", "main.py"),
        ("Result for 'pkg' directory:", "calculator", "pkg/calculator.py"),
        ("Result for '/bin' directory:", "calculator", "/bin/cat"),
        ("Result for '../' directory:", "calculator", "pkg/does_not_exist.py"),
    ]

    for header, working_dir, file_path in cases:
        print(header)
        print(get_file_content(working_dir, file_path))
        print("")


if __name__ == "__main__":
    main()