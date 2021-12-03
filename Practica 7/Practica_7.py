from ftplib import FTP, FTP_PORT
from typing import List


def save_file(con: FTP, remote_file_path: str, local_file_path: str):
    with open(local_file_path, "wb") as local_file:
        con.retrbinary(f"RETR {remote_file_path}", local_file.write)


def get_txt_file(con: FTP, file_path: str) -> List[str]:
    listado: List[str] = []
    con.retrlines(f"RETR {file_path}", listado.append)
    return listado


def list_folder(con: FTP, directory: str):
    print(directory)
    listado: List[str] = []
    con.retrlines(f"LIST {directory}", listado.append)
    return listado


def get_file_dir(con: FTP, directory: str):
    listado = list_folder(con, directory)
    return [file_info for file_info in listado if file_info.startswith("-")], [
        file_info for file_info in listado if not file_info.startswith("-")
    ]


def get_file_name(file_info: str) -> str:
    return "".join(file_info.split()[8:])


def connect_ftp(
    host: str, port: int = FTP_PORT, usr: str = "anonymous", pwd: str = "", save_path: str = ""
):
    connection = FTP()
    connection.connect(host=host, port=port, timeout=3)
    connection.login(usr, pwd)
    actual_path = ""
    l_file, l_dir = get_file_dir(connection, actual_path)
    files_info = "\n".join(l_file)
    dirs_info = "\n".join(l_dir)
    print(f"files:\n{files_info}\ndirs:\n{dirs_info}")
    for file_info in l_file:
        file_name = get_file_name(file_info)
        print(file_name)
    for dir_info in l_dir:
        l_subdir = list_folder(connection, get_file_name(dir_info))
        print(l_subdir)

    connection.close()


if __name__ == "__main__":
    connect_ftp(host="ftp.heanet.ie",
                save_path="C:\Users\migue\OneDrive\Escritorio\Practicas\Practica_7")
