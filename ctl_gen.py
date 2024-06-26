import os

# Название сервиса
service_name = "chatgptapi"

# Путь к виртуальному окружению
venv_path = "venv"

# Путь к исполняемому файлу Python
python_path = os.path.join(venv_path, "bin", "python")

# Путь к скрипту
script_path = "main"

# Команда для запуска скрипта
command = f"uvicorn {script_path}:app --host 0.0.0.0 --port 8790"

# Создание systemd сервиса
with open(f"/etc/systemd/system/{service_name}.service", "w") as f:
    f.write(f"""
[Unit]
Description={service_name} service
After=network.target

[Service]
User=root
WorkingDirectory={os.getcwd()}
ExecStart=source {venv_path}/bin/activate && {command}
Restart=on-failure
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
    """)

# Перезагрузка systemd
os.system("systemctl daemon-reload")

# Запуск сервиса
os.system(f"systemctl enable {service_name}")
os.system(f"systemctl start {service_name}")

print(f"Сервис {service_name} успешно создан и запущен.")
