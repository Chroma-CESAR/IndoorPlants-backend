main:
    #!/bin/bash
    choice=$(gum choose "start-server" "install-requirements")
    if ! [ "$choice" ]; then
        echo "Nothing choosed"
    else
        just "$choice"
    fi

start-server:
    #!/bin/bash
    venv/Scripts/python.exe -m uvicorn app.main:app --reload

install-requirements:
    #!/bin/bash
    if ! [ -d ./venv ]; then
        just create-venv
    fi
    venv/Scripts/python.exe -m pip install --upgrade pip
    venv/Scripts/python.exe -m pip install -r ./requirements.txt

create-venv:
    #!/bin/bash
    python -m venv venv