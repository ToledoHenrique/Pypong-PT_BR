import cx_Freeze
executables = [cx_Freeze.Executable(
    script="Pypong.py", icon="assets/pong.ico")]

cx_Freeze.setup(
    name="PyPong",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets","sounds"]
                           }},
    executables=executables
)