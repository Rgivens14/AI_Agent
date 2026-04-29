import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs


        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'


        file_list = []
        for target in os.listdir(target_dir):
            full_path = os.path.join(target_dir, target)
            if os.path.isdir(full_path):
                is_dir = True
            else:
                is_dir = False

            filename = target
            files_size = os.path.getsize(full_path)
            
            file_list.append(f"- {filename}: file_size={files_size} bytes, is_dir={is_dir}")
        return "\n".join(file_list)
    except Exception as e:
        return f"Error: {e}"